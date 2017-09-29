from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import products.urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'products/', include(products.urls)),
    url(r'users/', include('users.urls')),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),

]
