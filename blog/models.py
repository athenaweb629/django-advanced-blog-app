from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField


class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)
    # Add ording to Tags model for Pagination so the ordering
    # doesnt change between pages
    class Meta:
        ordering = ["value"]

    def __str__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,  db_index=True)
    modified_at = models.DateTimeField(auto_now=True,  db_index=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)

    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()

    tags = models.ManyToManyField(Tag, related_name="posts")
    comments = GenericRelation(Comment)

    hero_image = VersatileImageField(
        upload_to="hero_images", 
        ppoi_field="ppoi", 
        null=True, 
        blank=True
    )
    # https://django-versatileimagefield.readthedocs.io/en/latest/model_integration.html#model-integration
    
    ppoi = PPOIField(null=True, blank=True)
    # https://django-versatileimagefield.readthedocs.io/en/latest/specifying_ppoi.html#the-ppoifield

    def __str__(self):
        return self.title
# AuthorProfile as to separate info from the User Auth Model
# Allowing for a separation of concerns
# And added security.
class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"