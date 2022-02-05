from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# DRF Login URL
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
]