from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from products.views import (addProductToCartView,
                            categoryDetailView,
                            categoryIndexView,
                            productDetailView,
                            productIndexView)

urlpatterns = [
    url(r'^index/', productIndexView, name='productIndexView'),
    url(r'^(?P<product_id>[0-9]+)/details/$', productDetailView,
        name='productDetailView'),

    url(r'^list/', categoryIndexView, name='categoryIndexView'),
    url(r'^(?P<category_id>[0-9]+)/products_list/$', categoryDetailView,
        name='productDetailView'),
    url(r'^(?P<product_id>[0-9]+)/add_to_cart/$',
        login_required(addProductToCartView),
        name='addProductToCart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
