from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
<<<<<<< HEAD
import products.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(products.urls)),
=======

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls')),
>>>>>>> cf021265a29dfb3c9202872360b492ab391da7c0
]
