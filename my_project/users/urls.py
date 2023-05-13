
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserLogIn

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/login/', UserLogIn.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 