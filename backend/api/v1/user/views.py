from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.v1.user.examples import login_examples
from api.v1.user.serializers import (
    UserLoginSerializer,
    UserMeSerializer,
    UserRegisterSerializer,
    UserSerializer,
)
from app.user.models import User


@extend_schema_view(
    me=extend_schema(summary="유저 조회"),
    login=extend_schema(summary="유저 로그인", examples=login_examples),
    register=extend_schema(summary="유저 회원가입"),
)
class UserViewSet(
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == "me":
            return UserMeSerializer
        elif self.action == "login":
            return UserLoginSerializer
        elif self.action == "register":
            return UserRegisterSerializer
        raise Exception

    def get_permissions(self):
        if self.action in ["me", "logout"]:
            return [IsAuthenticated()]
        return []

    def _create(self, request, *args, **kwargs) -> object:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _update(self, request, *args, **kwargs) -> object:
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @action(methods=["GET", "PUT"], detail=False)
    def me(self, request, *args, **kwargs):
        if request.method == "GET":
            serializer = self.get_serializer(self.request.user)
        else:
            return self._update(request, *args, **kwargs)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def login(self, request, *args, **kwargs):
        return self._create(request, *args, **kwargs)

    @action(methods=["POST"], detail=False)
    def register(self, request, *args, **kwargs):
        return self._create(request, *args, **kwargs)
