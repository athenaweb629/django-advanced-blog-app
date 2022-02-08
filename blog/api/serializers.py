from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    # serializes a related object to a URL at which we can retrieve the full detail of the object
    # Requires name of view 
    tags = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail"
        )
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
