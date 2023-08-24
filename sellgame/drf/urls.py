from django.urls import path, re_path, include
from drf.views import *

app_name = 'drf'
urlpatterns = [
    path('v1/news/', NewsAPIList.as_view()),
    path('v1/drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/news/<int:pk>/', NewsAPIUpdate.as_view()),
    path('v1/newsdelete/<int:pk>/', NewsAPIDestroy.as_view()),
    path('v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]
