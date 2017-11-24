from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class CustomerUser(User):
    """docstring for CustomerUser"""
    cellphone = models.CharField(
        help_text=_("Número de telefone. Preencha apenas com númreos."),
        verbose_name=_("Telefone Celular"),
        max_length=15, null=False, blank=False)

    phone_number = models.CharField(
        help_text=_("Número de telefone. Preencha apenas com númreos."),
        verbose_name=_("Teledone Fixo"),
        max_length=15, null=True, blank=False)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return (self.first_name + " " + self.last_name)


"""
define string CreditCard.verbose_name
"""
credit_card_verbose_name = 'Cartão de Crédito'
credit_card_verbose_name_plural = 'Cartões de Crédito'


class CreditCard(models.Model):
    """docstring for CreditCard"""
    user = models.ForeignKey(CustomerUser)
    owner_name = models.CharField(
        help_text=_("Preencha como está no " + credit_card_verbose_name),
        verbose_name=_("Nome do Titular do " + credit_card_verbose_name),
        max_length=256)
    card_number = models.CharField(
        verbose_name=_("Número do " + credit_card_verbose_name),
        max_length=16)
    security_code = models.CharField(
        verbose_name=_("Código de Segurança do " + credit_card_verbose_name),
        max_length=3)
    expire_date = models.DateField(
        verbose_name=_("Validade do " + credit_card_verbose_name))
    provider = models.CharField(
        verbose_name=_("Bandeira do " + credit_card_verbose_name),
        max_length=20)

    class Meta:
        verbose_name = _(credit_card_verbose_name)
        verbose_name_plural = _(credit_card_verbose_name_plural)

    def __str__(self):
        return ("************" + self.card_number[-4:])


class ShippingAddress(models.Model):
    """docstring for ShippingAddress"""
    customer = models.ForeignKey(CustomerUser)
    country = models.CharField(
        help_text=_(
            "Preencha com o nome completo do país"
            " onde esse endereço se encontra."),
        verbose_name=_("País"),
        max_length=50)
    state = models.CharField(
        help_text=_("Estado ou província onde esse estado se encontra."),
        verbose_name=_("Estado"),
        max_length=50)
    city = models.CharField(
        help_text=_("Cidade onde esse endereço se encontra."),
        verbose_name=_("Cidade"),
        max_length=50)
    zip_code = models.CharField(
        help_text=_("Código de Endereço Postal"),
        verbose_name=_("CEP"),
        max_length=10, null=True, blank=True)
    address = models.CharField(
        help_text=_("Endereço Postal"),
        verbose_name=_("Endereço"),
        max_length=256)
    reference = models.CharField(
        help_text=_(
            "Ponto de Referência nas redondezas."
            " Ex: 'Ao lado da Farmécia'"),
        verbose_name=_("Ponto de Referência."),
        max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = _('Endereço para Envio')
        verbose_name_plural = _('Endereços para Envio')
        ordering = ('country', 'state', 'city', 'zip_code')

    def __str__(self):
        return self.zip_code + ' - ' + self.address
