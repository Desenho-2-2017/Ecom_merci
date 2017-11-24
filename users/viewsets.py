from rest_framework.viewsets import ModelViewSet
from .models import (
    CustomerUser,
    CreditCard,
    ShippingAddress
    )
from .serializers import (
    # CustomerUserSerializer,
    # CreditCardSerializer,
    CreditCardSerializerPOST,
    CreditCardSerializerDefault,
    ShippingAddressSerializerDefault,
    CustomerUserSerializerDefault,
    CustomerUserSerializerPOST,
    )
from .permissions import (
    CustomerUserPermissions,
    DefaultUserItemsPermissions,
)


class CustomerUserViewSet(ModelViewSet):
    """Description:CustomerUserViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """
    permission_classes = (CustomerUserPermissions,)
    queryset = CustomerUser.objects.all()
    # serializer_class = CustomerUserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerUserSerializerPOST
        return CustomerUserSerializerDefault

    def list(self, request):
        """
        API endpoint that allows all users to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "last_login": "date_time",
            "is_superuser": "boolean",
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string@email.com",
            "is_staff": "boolean",
            "is_active": "boolean",
            "date_joined": "date_time",
            "groups": [],
            "user_permissions": [],
            "cellphone": "integer",
            "phone_number": "integer"
        }
        ```
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
            "password": "string",
            "cellphone": "string",
            "phone_number": "string"
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
            "cellphone": "string",
            "phone_number": "string"
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
        API endpoint that allows allow the return\
        of a user through the method Get.
        ---
        Response example:
        ```
        {
            "id": "integer",
            "last_login": "date_time",
            "is_superuser": "boolean",
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string@email.com",
            "is_staff": "boolean",
            "is_active": "boolean",
            "date_joined": "date_time",
            "groups": [],
            "user_permissions": [],
            "cellphone": "integer",
            "phone_number": "integer"
        }
        ```
        """
        response = super(CustomerUserViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be partial edited.
        ---
        Parameters:
        User ID and a JSON with one or more attributes of user

        Example:
        ```
        {
            "last_login": "date_time",
            "is_staff": "boolean",
            "user_permissions": [],
            "cellphone": "integer",
            "phone_number": "integer"
        }
        ```
        """
        response = super(CustomerUserViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be edited.
        ---
        Parameters:
        User ID and a JSON with at least username,
        telephone and password of user
        Example:
        ```
        {
            "username": "string",
            "password": "string",
            "cellphone": "integer"
        }
        ```
        """
        response = super(
            CustomerUserViewSet,
            self).update(
            request,
            pk,
            **kwargs
            )
        return response


class CreditCardViewSet(ModelViewSet):
    """
    API endpoint that allows credit cards to be
    viewed, created, deleted or edited.
    """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializerDefault
    permission_classes = (DefaultUserItemsPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreditCardSerializerPOST
        return CreditCardSerializerDefault

    def list(self, request):
        """
        API endpoint that allows credit cards to be viewed
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "owner_name": "string",
            "card_number": "string",
            "security_code": "string",
            "expire_date": "date_time",
            "provider": "string",
        }
        ```
        """
        response = super(CreditCardViewSet, self).list(request)
        return response

    # def create(self, request):
    #     """
    #     API endpoint that allows credit cards to be created.
    #     ---
    #     Body example:
    #     ```
    #     {
    #         "owner_name": "string",
    #         "card_number": "string",
    #         "security_code": "string",
    #         "expire_date": "date_time",
    #         "provider": "string",
    #     }
    #     ```
    #     """
    #     response = super(CreditCardViewSet, self).create(request)
    #     return response


class ShippingAddressViewSet(ModelViewSet):
    """
    API endpoint that allows shipping adresses to be
    viewed, created, deleted or edited.
    """
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializerDefault
    permission_classes = (DefaultUserItemsPermissions,)
