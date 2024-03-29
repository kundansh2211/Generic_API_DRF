from django.urls import path
from .views import MobileAPIView, MobileDetailsAPIView

urlpatterns = [
    path('create_list/', MobileAPIView.as_view()),
    path('ud/<int:pk>',  MobileDetailsAPIView.as_view())
]