
from django.contrib import admin
from django.urls import path
from shop.views import catalog, create_order, orders, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', catalog, name='catalog'),
    path('create_order/<int:id>/', create_order, name='create_order'),
    path('orders/', orders, name='orders'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)