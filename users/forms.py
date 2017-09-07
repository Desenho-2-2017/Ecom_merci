from django import forms
from .models import CustomerUser
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist


class CustomerUserRegistrationForm(forms.ModelForm):
    """
    Class for CustomerUser registration form.
    """
    username = forms.CharField(label=_("Nome de usuário"))
    first_name = forms.CharField(label=_("Nome"))
    last_name = forms.CharField(label=_("Sobrenome"))
    email = forms.CharField(label=_("E-mail"), validators=[validate_email])
    password = forms.CharField(label=_("Senha"), widget=forms.PasswordInput)
    password_validation = forms.CharField(label=_("Confirmação de senha"), widget=forms.PasswordInput)

    class Meta:
        model = CustomerUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(CustomerUserRegistrationForm, self).clean()

        # Password validation
        password = cleaned_data.get('password')
        password_validation = cleaned_data.get('password_validation')

        password_error_message = _("A senha deve ser igual à confirmação de senha.")
        if password and password_validation:
            if password != password_validation:
                self.add_error('password', forms.ValidationError(password_error_message))

        # Username UNIQUE constraint validation
        username = cleaned_data.get('username')

        username_error_message = _("Este nome de usuário não está disponível.")
        try:
            customer_user = CustomerUser.objects.get(username=username)
            self.add_error('username', forms.ValidationError(username_error_message))
        except ObjectDoesNotExist:
            pass

        return cleaned_data
