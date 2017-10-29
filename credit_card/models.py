from django.db import models

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
