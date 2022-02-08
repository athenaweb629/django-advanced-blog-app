from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    # Tags as string objects - unqiue (They were ints previously)
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True, queryset=Tag.objects.all()
        )
    # serializes a related object to a URL at which we can retrieve the full detail of the object
    # Requires name of view 
    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail",
        lookup_fields="email",
        )
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
