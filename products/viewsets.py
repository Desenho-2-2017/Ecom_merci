from rest_framework.viewsets import ModelViewSet
from .models import (
    ProductCategory,
    Product
    )
from .serializers import (
    ProductCategorySerializerDefault,
    ProductCategorySerializerPOST,
    ProductSerializerDefault,
    ProductSerializerPOST
    )
from .permissions import (
    ProductPermissions
    )


class ProductCategoryViewSet(ModelViewSet):
    """
    API endpoint that allows category to be
    viewed, created, deleted or edited.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializerDefault
    permission_classes = (ProductPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCategorySerializerPOST
        return ProductCategorySerializerDefault

    def list(self, request):
        """
        API endpoint that allows category to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "category_name": "string",
            "father_category": "string"
        }
        ```
        """
        response = super(ProductCategoryViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows category to be created.
        ---
        Body example:
        "father_category" is optional
        ```
        {
            "category_name": "string",
            "father_category": "string"
        }
        ```
        Response example:
        ```
        {
            "pk": "integer",
            "category_name": "string",
            "father_category": "string"
        }
        ```
        """
        response = super(ProductCategoryViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows category to be deleted.
        Receive the ID of product category.
        """
        response = super(ProductCategoryViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows the return\
        of a product category through the method Get.
        Receive the ID of product category.
        ---
        Response example:
        ```
        {
            "id": "integer",
            "category_name": "string",
            "father_category": "string"
        }
        ```
        """
        response = super(ProductCategoryViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows partial update of category.
        ---
        Parameters:
        Category ID and a JSON with one or more attributes of category.
        Example:
        ```
        {
            "category_name": "string"
        }
        ```
        """
        response = super(ProductCategoryViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows category to be updated.
        Parameters:
        Cart ID and a JSON with all with all required attributes.
        Example:
        ```
        {
            "category_name": "string"
        }
        ```
        """
        response = super(ProductCategoryViewSet, self).update(
            request, pk, **kwargs
            )
        return response


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be\
    viewed, created, deleted or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializerDefault
    permission_classes = (ProductPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductSerializerPOST
        return ProductSerializerDefault

    def list(self, request):
        """
        API endpoint that allows product to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "product_name": "string",
            "stock_quantity": "integer",
            "price": "integer",
            "weight": "integer",
            "width": "integer",
            "height": "integer",
            "product_type": "string",
            "illustration": "path",
            "category_id": "integer"
        }
        ```
        """
        response = super(ProductViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows product to be created.
        Body example:
        ```
        {
            "stock_quantity": "integer",
            "product_name": "string",
            "price": "integer",
            "width": "integer",
            "height": "integer",
            "category_id": "string",
            "product_type": "string",
            "illustration": "string",
            "weight": "integer"
        }
        ```
        ---
        Response example:
        ```
        {
            "id": "integer",
            "product_name": "string",
            "stock_quantity": "integer",
            "price": "integer",
            "weight": "integer",
            "width": "integer",
            "height": "integer",
            "product_type": "string",
            "illustration": "path",
            "category_id": "integer"
        }
        ```
        """
        response = super(ProductViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows product to be deleted.
        """
        response = super(ProductViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows allow the return\
        of a product through the method Get.
        Receive the ID of product.
        ---
        Receive
        Response example:
        ```
        {
            "id": "integer",
            "product_name": "string",
            "stock_quantity": "integer",
            "price": "integer",
            "weight": "integer",
            "width": "integer",
            "height": "integer",
            "product_type": "string",
            "illustration": "path",
            "category_id": "integer"
        }
        ```
        """
        response = super(ProductViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows product to be updated.
        ---
        Parameters:
        Cart ID and a JSON with one or more attributes of product.
        Full updade:
        ```
        {
            "stock_quantity": "integer",
            "product_name": "string",
            "price": "integer",
            "width": "integer",
            "height": "integer",
            "category_id": "string",
            "product_type": "string",
            "illustration": "string",
            "weight": "integer"
        }
        ```
        ---
        Partial updade:
        ```
        {
            "stock_quantity": "integer",
            "product_name": "string",
            "price": "integer",
            "illustration": "string",
            "weight": "integer"
        }
        ```
        """
        response = super(ProductViewSet, self).\
            partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows category to be updated.
        ---
        Parameters:
        Product ID and a JSON with all required attributes.
        ```
        {
            "stock_quantity": "integer",
            "product_name": "string",
            "price": "integer",
            "category_id": "string",
            "illustration": "string"
        }
        ```
        """
        response = super(ProductViewSet, self).update(
            request, pk, **kwargs
            )
        return response
