from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


from rest_framework import generics, viewsets
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response 
from rest_framework.decorators import action

from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blog.models import Post
from blango_auth.models import User

# Example Viewset that allows listing all Tag objects ~ assuming TagSerializer has been implemented
class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)
# Model Version is more efficient in this case
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer