from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from app.user.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "phone", "username", "birth_date"]
        read_only_fields = ["email", "phone", "username", "birth_date"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "phone", "username", "birth_date"]
        read_only_fields = ["phone"]

    @transaction.atomic
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        self.user = authenticate(request=self.context["request"], email=attrs["email"], password=attrs["password"])
        if self.user:
            refresh = self.get_token(self.user)
        else:
            raise ValidationError(["인증정보가 일치하지 않습니다."])

        data = dict()
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data

    @transaction.atomic
    def create(self, validated_data):
        return validated_data


class UserLogoutSerializer(serializers.Serializer):
    uid = serializers.CharField(required=False, help_text="기기의 고유id")

    def create(self, validated_data):
        user = self.context["request"].user
        if validated_data.get("uid"):
            user.disconnect_device(validated_data["uid"])

        return {}


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    password_confirm = serializers.CharField(write_only=True, required=False)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm", None)

        if "password" in User.REGISTER_FIELDS:
            errors = {}
            # 비밀번호 검증
            if password != password_confirm:
                errors["password"] = ["비밀번호가 일치하지 않습니다."]
                errors["password_confirm"] = ["비밀번호가 일치하지 않습니다."]
            else:
                try:
                    validate_password(password)
                except DjangoValidationError as error:
                    errors["password"] = list(error)
                    errors["password_confirm"] = list(error)

            if errors:
                raise ValidationError(errors)

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
        )
        refresh = RefreshToken.for_user(user)

        return {
            "access": refresh.access_token,
            "refresh": refresh,
        }
