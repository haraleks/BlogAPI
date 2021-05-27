from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from blog_api.models import BlogPost
from blog_api.serializers import BlogPostSerializers


class BlogPostViews(ModelViewSet):
    serializer_class = BlogPostSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = BlogPost.objects.all()
