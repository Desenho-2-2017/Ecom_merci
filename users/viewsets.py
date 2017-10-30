from rest_framework.viewsets import ModelViewSet
from .models import (
    CustomerUser,
    PhoneNumber,
    CreditCard,
    ShippingAddress
    )
from .serializers import (
    CustomerUserSerializer,
    PhoneNumberSerializer,
    CreditCardSerializer,
    ShippingAddressSerializer
    )


class CustomerUserViewSet(ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer


class PhoneNumberViewSet(ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class CreditCardViewSet(ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer


class ShippingAddressViewSet(ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
