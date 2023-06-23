from django.urls import path
from .views import UserAPIView


urlpatterns = [
    path('', UserAPIView.as_view(), name="profile")
]