from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics
from authentification.api.token.serializers import SignUpSerializer, LoginSerializer, DummySerializer


class LoginView(APIView):

    serializer_class = LoginSerializer
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                return Response(
                    {
                        "username": user.username,
                        "email": user.email,
                        "token": user.auth_token.key
                    }, 
                    status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SignUpView(generics.CreateAPIView):

    permission_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = SignUpSerializer


class LogoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = DummySerializer

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
