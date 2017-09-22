from __future__ import unicode_literals
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
    weight = models.IntegerField(
        help_text=_("Peso do produto atual"),
        verbose_name=_("Peso do produto"),
        null=False, blank=False
    )
    width = models.IntegerField(
        default=0,
        help_text=_("Largura da Imagem"),
        verbose_name=_("Largura da Imagem")
    )
    height = models.IntegerField(
        default=0,
        help_text=_("Altura da Imagem"),
        verbose_name=_("Altura da Imagem")
    )
    illustration = models.ImageField(null=False, blank=False,
                                     default='default_product.jpg',
                                     width_field="width",
                                     height_field="height",
                                     help_text=_("Ilustração"),
                                     verbose_name=_("Imagem"),
                                     )

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = ('Produtos')
        ordering = ('product_name', 'category_id', 'stock_quantity', 'price')

    def __str__(self):
        return self.product_name
