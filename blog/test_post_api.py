from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from pytz import UTC
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from blog.models import Post

class PostApiTestCase(TestCase):
    def setUp(self):
        self.u1 = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )

        self.u2 = get_user_model().objects.create_user(
            email="test2@example.com", password="password2"
        )

        posts = [
            Post.objects.create(
                author=self.u1,
                published_at=timezone.now(),
                title="Post 1 Title",
                slug="post-1-slug",
                summary="Post 1 Summary",
                content="Post 1 Content",
            ),
            Post.objects.create(
                author=self.u2,
                published_at=timezone.now(),
                title="Post 2 Title",
                slug="post-2-slug",
                summary="Post 2 Summary",
                content="Post 2 Content",
            ),
        ]

        # let us look up the post info by ID
        self.post_lookup = {p.id: p for p in posts}

        # override test client
        self.client = APIClient()
        token = Token.objects.create(user=self.u1)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    # Queries the Post objects that were inserted in setUp using the API,
    # Then checks that their data matches expected data.
    def test_post_list(self):
        resp = self.client.get("/api/v1/posts/")
        data = resp.json()
        self.assertEqual(len(data), 2)

        for post_dict in data:
            post_obj = self.post_lookup[post_dict["id"]]
            self.assertEqual(post_obj.title, post_dict["title"])
            self.assertEqual(post_obj.slug, post_dict["slug"])
            self.assertEqual(post_obj.summary, post_dict["summary"])
            self.assertEqual(post_obj.content, post_dict["content"])
            self.assertTrue(
                post_dict["author"].endswith(f"/api/v1/users/{post_obj.author.email}")
            )
            self.assertEqual(
                post_obj.published_at,
                datetime.strptime(
                    post_dict["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ).replace(tzinfo=UTC),
            )



    def test_unauthenticated_post_create(self):
        # unset credentials so we are an anonymous user
        self.client.credentials()
        post_dict = {
            "title": "Test Post",
            "slug": "test-post-3",
            "summary": "Test Summary",
            "content": "Test Content",
            "author": "http://testserver/api/v1/users/test@example.com",
            "published_at": "2021-01-10T09:00:00Z",
        }
        resp = self.client.post("/api/v1/posts/", post_dict)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(Post.objects.all().count(), 2)



    # Creates a post through the API then queries and checks the database for it, using Post.id (that was returned after creating it)
    def test_post_create(self):
        post_dict = {
            "title": "Test Post",
            "slug": "test-post-3",
            "summary": "Test Summary",
            "content": "Test Content",
            "author": "http://testserver/api/v1/users/test@example.com",
            "published_at": "2021-01-10T09:00:00Z",
        }
        resp = self.client.post("/api/v1/posts/", post_dict)
        post_id = resp.json()["id"]
        post = Post.objects.get(pk=post_id)
        self.assertEqual(post.title, post_dict["title"])
        self.assertEqual(post.slug, post_dict["slug"])
        self.assertEqual(post.summary, post_dict["summary"])
        self.assertEqual(post.content, post_dict["content"])
        self.assertEqual(post.author, self.u1)
        self.assertEqual(post.published_at, datetime(2021, 1, 10, 9, 0, 0, tzinfo=UTC))