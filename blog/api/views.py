from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from django.db.models import Q

from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


from rest_framework import generics, viewsets
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response 
from rest_framework.decorators import action

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User
from blog.models import Post, Tag
from blog.api.serializers import (
    PostSerializer,
    UserSerializer,
    PostDetailSerializer,
    TagSerializer,
)

# Model Version is more efficient in our case (compared to ViewSet)
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


    # https://www.django-rest-framework.org/api-guide/viewsets/
    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        # Updated for pagination
        # https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
        tag = self.get_object()
        page = self.paginate_queryset(tag.posts)
        if page is not None:
            post_serializer = PostSerializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(post_serializer.data)
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)
    
    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)

# Example: Setting Django-Filter Backend by applying it to individual views/viewsets 
import django_filters.rest_framework

class PostViewSet(viewsets.ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()


    # User-based Filtering - Restricting Access to unpublished posts
    # Side Note: Changes to get_queryset method apply to all API action methods
    def get_queryset(self):
      if self.request.user.is_anonymous:
        # [published only] - anonymous users get published Posts only
        return self.queryset.filter(published_at__lte=timezone.now())

      if not self.request.user.is_staff:
            # [allow all] - admin/staff users get all Posts
            return self.queryset

      # [own or published] - logged-in users get published Posts or those that they’ve authored
      return self.queryset.filter(
            Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
      )
      # URL-Based Filtering - Filtering posts based on time periods
      # fetch the period_name URL parameter from self.kwargs
      time_period_name = self.kwargs.get("period_name")

      if not time_period_name:
          # no further filtering required
          return queryset
      if time_period_name == "new":
          return queryset.filter(published_at__gte=timezone.now() - timedelta(hours=1))
      elif time_period_name == "today":
          return queryset.filter(published_at__date=timezone.now().date(),)

      elif time_period_name == "week":
          return queryset.filter(published_at__gte=timezone.now() - timedelta(days=7))
          
      else:
          raise Http404(
              f"Time period {time_period_name} is not valid, should be "
              f"'new', 'today' or 'week'"
          )

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer

    
    # Will list only Post objects for which the current user is the author.
    # Caches the response from this view, for 5 min.
    @method_decorator(cache_page(300))
    # vary_on_headers accepts multiple header names as arguments so removed vary_on_cookie to simplify code.
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    # /api/v1/posts/mine
    # Since pagination was implemented, actions need to be fixed 
    # The querysets will be returned in the prior, non-paginated format if theyre not manually paginated
    # more info on pagination: 
    # https://www.django-rest-framework.org/api-guide/pagination/#cursorpagination
    # https://www.django-rest-framework.org/api-guide/pagination/#custom-pagination-styles
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)

        page = self.paginate_queryset(posts)

        if page is not None:
            serializer = PostSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)

    # Caching Rules for Blango Viewsets
    # The list of Posts should be cached for 2 mins, however when fetching a Post detail we should get the latest data from the database.
    # Since Tag objects to change very often; cache both the list and detail views for 5 mins.
    @method_decorator(cache_page(120))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)




class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Adding caching to viewsets is similar, except the decorator(s) 
    # need to be added to the built-in action methods. 
    # Adding caching to the methods that alter data is basically redundant, they do not do anything.
    # With that said, only the list() and retrieve() methods 
    # need caching implemented to add caching to this view.
    # Can be added as pass through methods that call the super call
    @method_decorator(cache_page(300))
    def get(self, *args, **kwargs):
        return super(UserDetail, self).get(*args, *kwargs)