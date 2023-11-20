from django.shortcuts import render
from rest_framework.authtoken.models import Token  # Token 모델 import

# 로그인에 필요한 import start
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import (
    ParseError,
    NotFound,
    PermissionDenied,
    NotAuthenticated,
    ValidationError,
)
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


class ListViewForUser(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateViewForUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def template_test(request):
    # 컨텍스트 변수
    context = {
        "message": "안녕하세요, Django!",
    }

    # 템플릿 렌더링 및 HTTP 응답 반환
    return render(request, "accounts/my_template.html", context)


# 로그인에 필요한 import end
User = get_user_model()


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        username_missing = username is None
        password_missing = password is None

        if username_missing or password_missing:
            missing_fields = []

            if username_missing:
                missing_fields.append("username")
            if password_missing:
                missing_fields.append("password")

            return Response(
                {
                    "status": "fail",
                    "message": f"필요한 정보 누락 for {', '.join(missing_fields)}",
                },
                status=400,
            )

        if user := authenticate(request, username=username, password=password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    "status": "success",
                    "message": "Welcome!",
                    "user_name": user.username,
                    "access_token": access_token,
                }
            )
        else:
            return Response(
                {
                    "status": "fail",
                    "message": "유효하지 않은 인증 정보입니다.",
                },
                status=401,
            )


class LogoutView(APIView):
    def post(self, request):
        print("request.user at logout: ", request.user)
        # logout(request)
        return Response({"logout_success": True})


class CheckViewForLogin(APIView):
    def get(self, request):
        print("request.user : ", request.user)
        if not request.user.is_authenticated:
            return Response(
                {"message": "로그인이 필요합니다.", "status": "is_not_authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        print("user : ", request.user)
        # serializer = UserProfileSerializer(user)
        return Response({"message": "login success"}, status=status.HTTP_200_OK)
