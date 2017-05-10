from django.conf.urls import url
from django.contrib import admin
from cmdb import views


urlpatterns = [
    url(r'^/', views.login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^detail/', views.detail, name='detail'),
    url(r'^del_host/', views.del_host, name='del_host'),
]
