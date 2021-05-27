from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, *args, **kwargs):
        user = User.objects.create_user(email=self.validated_data['email'], password=self.validated_data['password'])
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": ["Password doesn't match"]})
        return super().validate(attrs)


class ChangePasswordUserSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError("Old password is not the same")
        if attrs['new_password'] == attrs['old_password']:
            raise serializers.ValidationError("You entered your old password")
        return super().validate(attrs)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        user.set_password(validated_data['new_password'])
        user.save()
        res = {'status': 'success',
               'message': 'Password updated successfully'}
        return res
