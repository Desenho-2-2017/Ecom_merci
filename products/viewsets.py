from rest_framework.viewsets import ModelViewSet
from .models import (
    ProductCategory,
    Product
    )
from .serializers import (
    ProductCategorySerializer,
    ProductSerializer
    )
from .permissions import (
    ProductPermissions
    )


class ProductCategoryViewSet(ModelViewSet):
    """
    API endpoint that allows category to be\
    viewed, created, deleted or edited.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (ProductPermissions,)


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be\
    viewed, created, deleted or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermissions,)
