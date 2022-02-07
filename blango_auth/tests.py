from django.test import TestCase

# Create your tests here.
from blango_auth.models import User
  
from rest_framework.authtoken.models import Token

class TokenAuthTestCase(TestCase):
  u = User.objects.get(pk=3)
  k = 'f27bbf86d23506d56104f1ccc826d1045791afc2'

  def test_user_token_creation(self):
      #t = Token.objects.create(user=u)
      #assertEquals(t, IntegrityError)
      self.assertEquals(t.key, k)

  def test_user_retrieval(self):
    self.assertEquals(self.u.email, 'soad@gmail.com')