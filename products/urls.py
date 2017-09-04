from .views import FrontView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', FrontView.as_view(),
        name='index'),
    url(r'^index/$', FrontView.as_view(),
        name='index'),
]
