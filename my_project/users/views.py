from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer, UserUpdateSerializer, CustomAuthTokenSerializer


class UserViewSet(GenericViewSet, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'post', 'delete']
    

    @action(detail=False, methods=["patch"], url_path="me/update")
    def custom_update(self, request, *args, **kwargs):
        instance = request.user
        serializer = UserUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
        #return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=["delete"], url_path="deactivate")
    def deactivate(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save()
        return Response({"message":"You have been deacticated"}, status=201)


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'nickname': user.nickname
        })