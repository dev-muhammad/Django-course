from django.urls import path
from .views import LoginView, SignUpView, LogoutView, UserAPIView
from activity.views import FavoriteApiView, ReviewApiView

urlpatterns = [
    path('profile/', UserAPIView.as_view(), name="profile"),
    path('profile/favorites/', FavoriteApiView.as_view({'get': 'list'}), name="user-favorites"),
    path('profile/reviews/', ReviewApiView.as_view({'get': 'list'}), name="user-reviews"),
    path('signup/', SignUpView.as_view(), name='token-signup'),
    path('login/', LoginView.as_view(), name='token-login'),
    path('logout/', LogoutView.as_view(), name='token-logout'),
]
