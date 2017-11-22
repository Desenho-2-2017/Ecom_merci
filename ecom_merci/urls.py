from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import HomeView
from rest_framework import routers
from users.viewsets import (
    CustomerUserViewSet,
    CreditCardViewSet,
    ShippingAddressViewSet
    )
from products.viewsets import (
    ProductCategoryViewSet,
    ProductViewSet
)
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

schema_view = get_swagger_view(title='Ecom_merci API')

router = routers.DefaultRouter()
router.register(r'customer_users', CustomerUserViewSet)
router.register(r'credit_cards', CreditCardViewSet)
router.register(r'shipping_addresses', ShippingAddressViewSet)
router.register(r'category', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^category/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^$', HomeView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', schema_view),
    url(r'^api/tokens/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
