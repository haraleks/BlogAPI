from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users.serializers import UserRegistrationSerializer, ChangePasswordUserSerializer

User = get_user_model()


class UserRegistration(GenericViewSet, CreateModelMixin):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    @swagger_auto_schema(query_serializer=UserRegistrationSerializer,
                         operation_description='Register user',
                         responses={201: UserRegistrationSerializer})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        show_serializer = self.get_serializer(instance)
        return Response(show_serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class ChangePasswordUser(GenericViewSet, UpdateModelMixin):
    serializer_class = ChangePasswordUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    @swagger_auto_schema(query_serializer=ChangePasswordUserSerializer,
                         operation_description='Change password user',
                         responses={200: "'status': 'success', 'message': 'Password updated successfully'"})
    def update(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data,
                                         context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response(instance)
