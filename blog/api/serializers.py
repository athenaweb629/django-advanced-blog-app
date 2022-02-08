from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    # To make tags 'readonly' - simplest way of serializing relationships
    tags = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # Alternatively StringRelatedfield will call the __str__() method of the object:
    tags = serializers.StringRelatedfield(many=True)
    # Another altnerative: SlugRelatedField - intended to work with a SlugField of a related object although it can work with any unique field. 
    tags = serializers.SlugRelatedField(slug_field="value", many=True, queryset=Tag.objects.all())
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
