from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import products.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(products.urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls')),

]
