from django.urls import path

from blog.api_views import post_list, post_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    # trailing '/' removed to avoid URLs like 'http://*site*/api/v1/posts/5/.json'
    path("posts/<int:pk>", post_detail, name="api_post_detail"),
]

# Enables JSON data for a Post with a url like 'http://*site*/api/v1/3.json'
# even from a browser.
# It is passed a list of URL patterns, and adds extra patterns with a suffix. 
urlpatterns = format_suffix_patterns(urlpatterns)