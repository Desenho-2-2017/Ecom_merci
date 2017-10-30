from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import (
    CustomerUser,
    PhoneNumber,
    CreditCard,
    ShippingAddress
    )
from .serializers import (
    # CustomerUserSerializer,
    PhoneNumberSerializer,
    CreditCardSerializer,
    ShippingAddressSerializer,
    CustomerUserSerializerDefault,
    CustomerUserSerializerPOST,
    )


class CustomerUserViewSet(ModelViewSet):
    """Description:CustomerUserViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """

    queryset = CustomerUser.objects.all()
    # serializer_class = CustomerUserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerUserSerializerPOST
        return CustomerUserSerializerDefault

    def list(self, request):
        """Description:list.

        API endpoint that allows all users to be viewed.
        """
        response = super(CustomerUserViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows users to be created.
        ---
        Body example:
        ```
        {
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string@email.com",
            "password": "string"
        }
        ```
        Response example:
        ```
        {
            "pk": 1,
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string@email.com",
            "password": "string"
        }
        ```
        """
        response = super(CustomerUserViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows users to be deleted.
        """
        response = super(CustomerUserViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific user to be viewed.
        """
        response = super(CustomerUserViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be edited.
        """
        response = super(CustomerUserViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be edited.
        """
        response = super(
            CustomerUserViewSet,
            self).update(
            request,
            pk,
            **kwargs
            )
        return response


class PhoneNumberViewSet(ModelViewSet):
    """
    API endpoint that allows phone numbers to be
    viewed, created, deleted or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (IsAuthenticated,)


class CreditCardViewSet(ModelViewSet):
    """
    API endpoint that allows credit cards to be
    viewed, created, deleted or edited.
    """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = (IsAuthenticated,)


class ShippingAddressViewSet(ModelViewSet):
    """
    API endpoint that allows shipping adresses to be
    viewed, created, deleted or edited.
    """
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = (IsAuthenticated,)
