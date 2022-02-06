from rest_framework import permissions

# Permissions to make sure any user can get the post detail but only the author can make changes or delete the post.
class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return request.user == obj.author
