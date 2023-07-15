from django.urls import path
from .views import hello, user, fullname, ClassBasedView, DispatchView

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('user/<str:name>/<str:phone>/', user, name='hello'),
    path('user/fullname/<str:first_name>/<str:last_name>/', fullname, name='fullname'),
    path('class/', ClassBasedView.as_view(), name='class-based'),
    path('dispatch/', DispatchView.as_view(), name="dispatch"),
]
