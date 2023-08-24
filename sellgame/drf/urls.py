from django.urls import path, re_path
from drf import views



app_name = 'drf'
urlpatterns = [
    path('v1/newslist/', views.NewsAPIList.as_view()),
]