from django.urls import path, re_path

from blog_api.views import BlogPostViews

as_view_common = {
    'get': 'list',
    'post': 'create'
}

as_view_with_pk = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}


urlpatterns = [
    path('blog_posts/', BlogPostViews.as_view(as_view_common), name='blogs_post'),
    path('blog_posts/<int:pk>/', BlogPostViews.as_view(as_view_with_pk), name='blogs_detail'),
]
