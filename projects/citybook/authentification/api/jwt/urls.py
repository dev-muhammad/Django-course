from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

from .views import LoginView, SignUpView, LogOutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='jwt-login'),
    path('logout/', LogOutView.as_view(), name='jwt-logout'),
    path('signup/', SignUpView.as_view(), name='jwt-signup'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
]
