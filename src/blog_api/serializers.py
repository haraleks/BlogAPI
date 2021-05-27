from rest_framework import serializers

from blog_api.models import BlogPost


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text', 'created_by', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_by', 'created_at']
