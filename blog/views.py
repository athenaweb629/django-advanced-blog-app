from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from blog.models import Post
from blog.forms import CommentForm
import logging

from django.views.decorators.cache import cache_page

# Logging
logger = logging.getLogger(__name__)

# Index Page for Blog
# Cache the response of Index View Every 5 minutes (300 secs)
# The list of Post objects will only be queried once every 5mins and 
# the template will only be rendered once every 5mins.
# All other responses will come from the cache.
@cache_page(300)
def index(request): 
    #  temporary change to return the current username logged in, 
    # or AnonymousUser if no one is logged in.
    from django.http import HttpResponse
    return HttpResponse(str(request.user).encode("ascii"))

    # Returns Post title, Author, Datetime
    posts = Post.objects.filter(published_at__lte=timezone.now())
    # Log quantity of posts
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html", {"posts": posts})


# Displays Post Detail View ("Read More")

def post_detail(request, slug):
    # Returns the Post Content field
    post = get_object_or_404(Post, slug=slug)
    
    # Create a Comment using the posted form data\
    # Return the comment / post view

    if request.user.is_active:
        # Check for active user. Inactive user means comment_form=None
        if request.method == "POST":
            # If not POST, a blank CommentForm is created.
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                # If POST, create the CommentForm using the posted data. If valid, form will be saved.
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                # log a message when a comment is created (logs directly after saving comment)
                logger.info("Created comment on Post %d for user %s", post.pk, request.user)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})