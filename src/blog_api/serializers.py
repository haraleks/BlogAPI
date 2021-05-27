from rest_framework import serializers

from blog_api.models import BlogPost


class BlogPostSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = super().create(validated_data)
        user = self.context['request'].user
        instance.created_by = user
        instance.save()
        return instance

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text', 'created_by', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_by', 'created_at']
