from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from .views import (CustomerUserRegistrationView)


urlpatterns = [
    url(r'^sign_up/$', CustomerUserRegistrationView.as_view(),
        name='sign_up'),
]
