from django.conf.urls import url
from django.contrib import admin
from cmdb import views


urlpatterns = [
    url(r'^/', views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^add_host/', views.add_host),
    url(r'^del_host/', views.del_host),
    url(r'^edit_host/', views.edit_host),
]
