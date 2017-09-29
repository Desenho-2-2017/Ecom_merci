from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from .views import (CustomerUserRegistrationView,
                    CustomerUserDelectionView,
                    CustomerUserUpdateView)

urlpatterns = [

    url(r'^sign_up/$', CustomerUserRegistrationView.as_view(),
        name='sign_up'),
    url(r'^excluir_conta/$', CustomerUserDelectionView.as_view(),
        name='excluir_conta'),
    url(r'^(?P<id>\d+)/edit/$', CustomerUserUpdateView.as_view(),
        name='edit')
]
