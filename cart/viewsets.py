from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import (
    Cart,
    Item
    )
from .serializers import (
    CartSerializerDefault,
    CartSerializerPOST,
    ItemSerializerDefault,
    ItemSerializerPOST
    )


class CartViewSet(ModelViewSet):
    """
    API endpoint that allows Cart to be
    viewed, created, deleted or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializerDefault
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CartSerializerPOST
        return CartSerializerDefault

    def list(self, request):
        """
        API endpoint that allows all cart to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "pk": "integer",
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        """
        response = super(CartViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows cart to be created.
        ---
        Body example:
        ```
        {
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        Response example:
        ```
        {
            "pk": 1,
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        """
        response = super(CartViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows cart to be deleted.
        """
        response = super(CartViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows allow the return\
        of a cart through the method Get.
        ---
        Response example:
        ```
        {
            "id": "integer",
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        """
        response = super(CartViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a cart to be edited.
        ---
        Parameters:
        Cart ID and a JSON with one or more attributes of cart
        Example:
        ```
        {
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        """
        response = super(CartViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a cart to be edited.
        ---
        Parameters:
        Cart ID and a JSON with all attributes
        Example:
        ```
        {
            "creation_date": "date",
            "checked_out": "boolean"
        }
        ```
        """
        response = super(
            CartViewSet,
            self).update(
            request,
            pk,
            **kwargs
            )
        return response


class ItemViewSet(ModelViewSet):
    """
    API endpoint that allows Item to be
    viewed, created, deleted or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializerDefault
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return ItemSerializerPOST
        return ItemSerializerDefault

    def list(self, request):
        """
        API endpoint that allows all item to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
            "content_type": "content_type"
        }
        ```
        """
        response = super(ItemViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows item to be created.
        ---
        Body example:
        ```
        {
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
            "content_type": "content_type"
        }
        ```
        Response example:
        ```
        {
            "pk": 1,
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
            "content_type": "content_type"
        }
        ```
        """
        response = super(ItemViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows item to be deleted.
        """
        response = super(CartViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows allow the return\
        of a item through the method Get.
        ---
        Response example:
        ```
        {
            "id": "integer",
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
        }
        ```
        """
        response = super(ItemViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a cart to be edited.
        ---
        Parameters:
        Item ID and a JSON with one or more attributes of item
        Example:
        ```
        {
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
        }
        ```
        """
        response = super(ItemViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a cart to be edited.
        ---
        Parameters:
        Item ID and a JSON with all attributes
        Example:
        ```
        {
            "quantity": "integer",
            "object_id": "integer",
            "unit_price": "integer",
            "cart": "cart",
        }
        ```
        """
        response = super(
            ItemViewSet,
            self).update(
            request,
            pk,
            **kwargs
            )
        return response
