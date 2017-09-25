from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from products.views import (productIndexView, productDetailView)

urlpatterns = [
    url(r'^index/', productIndexView, name='productIndexView'),
    url(r'^(?P<product_id>[0-9]+)/details/$', productDetailView,
        name='productDetailView'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
