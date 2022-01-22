from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User

class PostTestCase(TestCase):
  flds = ["Newest Post","Just a Test","Will p2 be able to pass the test? lets find out...","test"]
  p=Post.objects.first()
  p2=Post(author=self.p.author, title="Newest Post", summary="Just a Test", content="Will p2 be able to pass the test? lets find out...", tags="test")

  def test_new_post_content_type(self):
    self.assertEqual(self.p2.content_type, self.p.content_type)

  def test_new_post_title(self):
    self.assertEqual(self.p2.title, self.flds[0])

class PostCommentTestCase(TestCase):
  p=Post.objects.first()
  u=User.objects.first()

  def test_comment_on_post(self):
    c1=Comment(creator=self.u, content="What a great test case!", content_object=self.p)

    self.assertEqual(c1.content_object, self.p)

  def test_comment_on_user(self):
    c2=Comment(creator=self.u, content="I'm the other comment test", content_object=self.u)
    self.assertEqual(c2.content_object, self.u)


