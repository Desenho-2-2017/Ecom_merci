from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .apps import UsersConfig
from .views import (CustomerUserRegistrationView,
                    CustomerUserDelectionView,
                    CustomerUserUpdateView,
                    CustomerUserListView,
                    CustomerUserDetailView,
                    LoginView,
                    LogoutView,)


app_name = UsersConfig.name

urlpatterns = [
    url(r'^$', CustomerUserListView.as_view(),
        name='list_view'),
    url(r'^sign_up/$', CustomerUserRegistrationView.as_view(),
        name='sign_up'),
    url(r'^excluir_conta/$',
        login_required(CustomerUserDelectionView.as_view()),
        name='excluir_conta'),
    url(r'^(?P<id>\d+)/edit/$',
        login_required(CustomerUserUpdateView.as_view()), name='edit'),
    url(r'^(?P<pk>\d+)/$', login_required(CustomerUserDetailView.as_view()),
        name='detail'),
    url(r'^login/$', LoginView.as_view(),
        name='login'),
    url(r'^logout/$', login_required(LogoutView.as_view()),
        name='logout'),
]
