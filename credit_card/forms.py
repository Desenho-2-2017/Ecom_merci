from django import forms
from .models import CreditCard

class CreditCardRegisterForm(forms.ModelForm):
    """
    Class for CreditCard registration form.
    """

    owner_name = forms.CharField(label=_("Nome do titular"))
    card_number =  forms.CharField(label=_("Número do cartão"))
    security_code = forms.CharField(label=_("Código de segurança"))
    expire_date = forms.CharField(label=_("Data de vencimento"))
    provider = forms.CharField(label=_("Bandeira"))

    class Meta:
        model = CustomerUser
        fields = ['owner_name', 'card_number', 'security_code', 'security_code',
         'expire_date', 'provider']
