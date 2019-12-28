from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateDeleteAPIView

urlpatterns = format_suffix_patterns([
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateDeleteAPIView.as_view()),
])
