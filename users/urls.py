from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from .apps import UsersConfig
from .views import (CustomerUserRegistrationView,
                    CustomerUserDelectionView,
                    CustomerUserUpdateView,
                    CustomerUserListView,
                    CustomerUserDetailView,)


app_name = UsersConfig.name

urlpatterns = [
    url(r'^$', CustomerUserListView.as_view(),
        name='list_view'),
    url(r'^sign_up/$', CustomerUserRegistrationView.as_view(),
        name='sign_up'),
    url(r'^excluir_conta/$', CustomerUserDelectionView.as_view(),
        name='excluir_conta'),
    url(r'^(?P<id>\d+)/edit/$', CustomerUserUpdateView.as_view(),
        name='edit'),
    url(r'^(?P<pk>\d+)$', CustomerUserDetailView.as_view(),
        name='detail'),
]
