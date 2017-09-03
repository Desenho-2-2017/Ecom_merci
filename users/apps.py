from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'users'
    label = 'usuario'
    verbose_name = _('Usuário')
    verbose_name_plural = _('Usuários')
