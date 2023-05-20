from django.urls import path
from .views import SignUpView, LoginView, LogoutView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='token-signup'),
    path('login/', LoginView.as_view(), name='token-login'),
    path('logout/', LogoutView.as_view(), name='token-logout'),
]