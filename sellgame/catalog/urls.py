from django.urls import path, re_path
from catalog import views
from sellgame import settings
from django.conf.urls.static import static


app_name = 'catalog'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
