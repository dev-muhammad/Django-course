from django.urls import path
from .views import LoginView, SignUpView, LogoutView, UserAPIView

urlpatterns = [
    path('profile/', UserAPIView.as_view(), name="profile"),
    path('signup/', SignUpView.as_view(), name='token-signup'),
    path('login/', LoginView.as_view(), name='token-login'),
    path('logout/', LogoutView.as_view(), name='token-logout'),
]
