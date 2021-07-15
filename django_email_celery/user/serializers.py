from django.contrib.auth import authenticate, models
from rest_framework import exceptions, serializers, fields
from rest_framework_jwt.settings import api_settings

from user import models as user_model

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserRegisterSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(required=False)

    class Meta:
        model = user_model.User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        user = user_model.User.objects.create_user(**validated_data)
        # user_model.Profile.objects.create(
        #     user_id=user,
        #     first_name=profile_data['first_name'],
        #     last_name=profile_data['last_name'],
        #     business_name=profile_data['business_name']
        # )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=128, write_only=True)
    token = fields.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise exceptions.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            models.update_last_login(None, user)
        except user_model.User.DoesNotExist:
            raise exceptions.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
