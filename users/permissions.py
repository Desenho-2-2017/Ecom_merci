from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from .models import CreditCard, ShippingAddress


class DefaultPermission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        permission = super().has_permission(request, view)

        try:
            if permission and request.user.is_active:
                permission = True
        except ObjectDoesNotExist:
            permission = False

        return permission


class CustomerUserPermissions(permissions.BasePermission):

    def __init__(self):
        self.permission = False
        self.request = None
        self.user_id = ''
        self.user_request_id = ''
        self.authorized_user = False

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        elif 'customer_users' in request.path:
            self.request = request
            self.user_id = str(self.request.user.id)
            self.user_request_id = \
                self.request.path.split('/customer_users/')[1][:-1]
            if (self.request.method == 'POST' and
                    self.request.user.is_anonymous):
                self.permission = True

            if self.user_id == self.user_request_id:
                self.authorized_user = True

            if self.request.method != 'DELETE' and self.authorized_user:
                self.permission = True
        else:
            self.permission = True

        return self.permission


class DefaultUserItemsPermissions(permissions.BasePermission):

    def __init__(self):
        self.permission = False
        self.request = None
        self.user_id = ''
        self.card_id = ''
        self.card_user_id = ''
        self.address_id = ''
        self.address_user_id = ''
        self.authorized_user = False

    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return False

        elif request.user.is_superuser:
            return True

        elif 'credit_cards' in request.path:
            self.request = request
            self.user_id = str(self.request.user.id)
            self.card_id = self.request.path.split('/credit_cards/')[1][:-1]

            if self.request.method == 'POST':
                self.permission = True

            try:
                card = CreditCard.objects.filter(pk=int(self.card_id))
                self.card_user_id = str(card[0].user.pk)
            except:
                pass

            if self.user_id == self.card_user_id:
                self.authorized_user = True

            if self.authorized_user:
                self.permission = True

        elif 'shipping_addresses' in request.path:
            self.request = request
            self.user_id = str(self.request.user.id)
            self.address_id = \
                self.request.path.split('/shipping_addresses/')[1][:-1]

            if self.request.method == 'POST':
                self.permission = True

            try:
                address = \
                    ShippingAddress.objects.filter(pk=int(self.address_id))
                self.address_user_id = str(address[0].customer.pk)
            except:
                pass

            if self.user_id == self.address_user_id:
                self.authorized_user = True

            if self.authorized_user:
                self.permission = True

        else:
            self.permission = True

        return self.permission
