from django.conf.urls import url, include
from rest_framework import routers
from .apps import UsersConfig
from .views import (CustomerUserRegistrationView,
                    CustomerUserDelectionView,
                    CustomerUserUpdateView,
                    CustomerUserListView,
                    CustomerUserDetailView,
                    LoginView,
                    LogoutView,)

from .viewsets import (
    CustomerUserViewSet,
    PhoneNumberViewSet,
    CreditCardViewSet,
    ShippingAddressViewSet
    )
app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'customer', CustomerUserViewSet)
router.register(r'phoneNumber', PhoneNumberViewSet)
router.register(r'creditCard', CreditCardViewSet)
router.register(r'shippingAddress', ShippingAddressViewSet)

urlpatterns = [
    url(r'^$', CustomerUserListView.as_view(),
        name='list_view'),
    url(r'^sign_up/$', CustomerUserRegistrationView.as_view(),
        name='sign_up'),
    url(r'^excluir_conta/$', CustomerUserDelectionView.as_view(),
        name='excluir_conta'),
    url(r'^(?P<id>\d+)/edit/$',
        CustomerUserUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', CustomerUserDetailView.as_view(),
        name='detail'),
    url(r'^login/$', LoginView.as_view(),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/', include(router.urls))
]
