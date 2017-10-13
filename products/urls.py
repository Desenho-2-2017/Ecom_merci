from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from products.views import (productIndexView,
                            productDetailView,
                            categoryIndexView,
                            categoryDetailView,
                            addProductToCartView)

urlpatterns = [
    url(r'^index/', productIndexView, name='productIndexView'),
    url(r'^(?P<product_id>[0-9]+)/details/$', productDetailView,
        name='productDetailView'),

    url(r'^list/', categoryIndexView, name='categoryIndexView'),
    url(r'^(?P<category_id>[0-9]+)/products_list/$', categoryDetailView,
        name='productDetailView'),
    url(r'^(?P<product_id>[0-9]+)/add_to_cart/$', addProductToCartView,
        name='addProductToCart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
