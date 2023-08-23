from django.urls import path, re_path, include
from sellgame import settings
from django.conf.urls.static import static
from users.views import Register, profile_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/', profile_views, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
