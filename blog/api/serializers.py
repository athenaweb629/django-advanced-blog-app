from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from blog.models import Post, Tag, Comment
from blango_auth.models import User


# UserSerializer must be first
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")

# New Tag Serializers for API endpoints ~ using viewsets and routers
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]

# PostSerializer must come after UserSerializer and CommentSerializer
class PostSerializer(serializers.ModelSerializer):
    # Option to fetch thumbnail image 
    # full_size option included because its already generated and basically 'free' to include
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ],
        read_only=True,
    )
    # Tags as string objects - unqiue (They were ints previously)
    tags = serializers.SlugRelatedField(
        slug_field="value", 
        many=True, 
        queryset=Tag.objects.all()
        )
    # serializes a related object to a URL at which we can retrieve the full detail of the object
    # Requires name of view 
    # https://www.django-rest-framework.org/api-guide/relations/#custom-hyperlinked-fields
    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail",
        lookup_field="email",
        )

    class Meta:
        model = Post
        exclude = ["ppoi"]
        readonly = ["modified_at", "created_at"]

# PostDetailSerializer Must come at the end, below User, Comment, and Post. TagSerializer's order does not matter.
class PostDetailSerializer(PostSerializer):
    # One extra size option for a cropped 200x200 image
    # https://django-versatileimagefield.readthedocs.io/en/latest/overview.html
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("square_crop", "crop__200x200"),
        ],
        read_only=True,
    )
    comments = CommentSerializer(many=True)

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments")

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()

        return instance