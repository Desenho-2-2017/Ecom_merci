from rest_framework import permissions


class ProductPermissions(permissions.BasePermission):

    def __init__(self):
        self.permission = False

    def has_permission(self, request, view):

        if 'products' in request.path or 'categories' in request.path:
            if request.method == 'GET':
                self.permission = True

        elif request.user.is_superuser:
            self.permission = True

        else:
            self.permission = True

        return self.permission
