#from django.conf.urls import url
from django.urls import path, include
from django.urls import include, re_path
from . import views

app_name = 'app'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^index/$', views.index_teste, name='index_teste')
]