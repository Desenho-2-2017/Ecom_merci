from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import (
    Cart,
    Item
    )
from .serializers import (
    CartSerializerDefault,
    ItemSerializerDefault
    )


class CartViewSet(ModelViewSet):
    """
    API endpoint that allows Cart to be
    viewed, created, deleted or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializerDefault
    permission_classes = (IsAuthenticated,)


class ItemViewSet(ModelViewSet):
    """
    API endpoint that allows Item to be
    viewed, created, deleted or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializerDefault
    permission_classes = (IsAuthenticated,)
