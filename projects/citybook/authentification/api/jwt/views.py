from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, JWTSignUpSerializer, DummySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = JWTSignUpSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    
    serializer_class = DummySerializer

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
