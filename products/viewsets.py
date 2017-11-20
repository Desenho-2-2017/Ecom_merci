from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import (
    ProductCategory,
    Product
    )
from .serializers import (
    ProductCategorySerializer,
    ProductSerializer
    )

class ProductCategoryViewSet(ModelViewSet):
    """
    API endpoint that allows phone numbers to be
    viewed, created, deleted or edited.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAuthenticated,)


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows credit cards to be
    viewed, created, deleted or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
