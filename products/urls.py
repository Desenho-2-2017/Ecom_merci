from .views import FrontView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', FrontView.as_view(),
        name='homepage'),
    url(r'^homepage/', FrontView.as_view(),
        name=''),
]
