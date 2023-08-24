from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news import views
from sellgame import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('catalog/', include('catalog.urls', namespace='shop')),
    path('orders/', include('order.urls', namespace='order')),
    path('account/', include('users.urls')),
    path('api/', include('drf.urls', namespace='drf')),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
