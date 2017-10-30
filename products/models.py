from __future__ import unicode_literals
import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinValueValidator
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
    stock_quantity = models.PositiveIntegerField(
        help_text=_("Quantidade do produto em estoque"),
        verbose_name=_("Quantidade do produto"),
        null=False, blank=False
    )
    price = models.FloatField(
        help_text=_("Preço atual do produto"),
        verbose_name=_("Preço do produto"),
        null=False, blank=False,
        validators=[MinValueValidator(0.1)],
    )
    weight = models.FloatField(
        default=0,
        help_text=_("Peso do produto atual"),
        verbose_name=_("Peso do produto"),
        null=False, blank=False,
        validators=[MinValueValidator(0.1)],
    )
    width = models.PositiveIntegerField(
        default=500,
        help_text=_("Largura da Imagem"),
        verbose_name=_("Largura da Imagem")
    )
    height = models.PositiveIntegerField(
        default=500,
        help_text=_("Altura da Imagem"),
        verbose_name=_("Altura da Imagem")
    )
    PRODUCT_TYPES = (
        ('PAD', 'Anuncio'),     # PAD, Product Advertising
        ('STD', 'Padrao'),      # STD, Standard Product
    )
    product_type = models.CharField(default='Padrao', max_length=3,
                                    choices=PRODUCT_TYPES
                                    )
    illustration = models.ImageField(null=False, blank=False,
                                     width_field='width',
                                     height_field='height',
                                     help_text=_("Ilustração"),
                                     verbose_name=_("Imagem"),
                                     )

    def save(self):
        image = Image.open(self.illustration)
        output = BytesIO()

        image = image.resize((500, 500))
        image.save(output, format='PNG', quality=100)
        output.seek(0)

        self.illustration = InMemoryUploadedFile(output, 'ImageField',
                                                 "%s.png" % self
                                                 .illustration
                                                 .name.split('.')[0],
                                                 'image/jpeg',
                                                 sys.getsizeof(output),
                                                 None)

        super(Product, self).save()

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = ('Produtos')
        ordering = ('product_name', 'category_id', 'stock_quantity', 'price')

    def __str__(self):
        return self.product_name
