from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class PostCommentTestCase(TestCase):
  p=Post.objects.first()
  u=User.objects.first()

  def test_comment_on_post(self):
    c1=Comment(creator=self.u, content="What a great test case!", content_object=self.p)

    self.assertEqual(c1.content_object, self.p)

  def test_comment_on_user(self):
    c2=Comment(creator=self.u, content="I'm the other comment test", content_object=self.u)
    self.assertEqual(c2.content_object, self.u)


