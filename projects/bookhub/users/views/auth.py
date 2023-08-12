from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework import generics
from ..serilizers.auth import SignUpSerializer, LoginSerializer, DummySerializer
from ..models import CustomUser

class LoginView(APIView):

    serializer_class = LoginSerializer
    permission_classes = []
    authentication_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = authenticate(request, email=email, password=password)
            token, _ = Token.objects.get_or_create(user=user)
            if user is not None:
                return Response(
                    {
                        "email": user.email,
                        "token": user.auth_token.key
                    }, 
                    status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SignUpView(generics.CreateAPIView):

    permission_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer


class LogoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = DummySerializer

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
