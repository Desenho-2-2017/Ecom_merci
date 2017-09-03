from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductCategory(models.Model):
    """docstring for Category"""
    category_name = models.CharField(
        help_text=_("Nome da categoria de produtos"),
        verbose_name=_("Categoria de Produto"),
        max_length=100, null=False, blank=False
    )

    class Meta:
        verbose_name = _('Categoria de Produtos')
        verbose_name_plural = ('Categorias de produtos')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """docstring for Products"""
    product_name = models.CharField(
        help_text=_("Nome completo do Produto"),
        verbose_name=_("Nome do produto"),
        max_length=100, null=False, blank=False
    )
    category_id = models.ForeignKey(ProductCategory)
    stock_quantity = models.IntegerField(
        help_text=_("Quantidade do produto em estoque"),
        verbose_name=_("Quandtidade do produto"),
        null=False, blank=False
    )
    price = models.IntegerField(
        help_text=_("Preço atual do produto"),
        verbose_name=_("Preço do produto"),
        null=False, blank=False
    )

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = ('Produtos')
        ordering = ('product_name', 'category_id', 'stock_quantity', 'price')

    def __str__(self):
        return self.product_name
