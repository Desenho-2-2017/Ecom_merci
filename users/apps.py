from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'users'
    label = 'users'
    verbose_name = _('Usuário')
    verbose_name_plural = _('Usuários')
