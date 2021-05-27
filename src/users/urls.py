from django.urls import path

from users.views import UserRegistration, ChangePasswordUser

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
    path('create_user/', UserRegistration.as_view({'post': 'create'}), name='create_user'),
    path('change_password/', ChangePasswordUser.as_view({'put': 'update'}), name='change_pass')
]