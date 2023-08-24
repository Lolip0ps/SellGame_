from django.urls import path, re_path
from drf.views import *

app_name = 'drf'
urlpatterns = [
    path('v1/newslist/', NewsAPIView.as_view()),
    path('v1/newslist/<int:pk>/', NewsAPIView.as_view()),
]
