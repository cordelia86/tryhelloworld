from django.conf.urls import url
from . import views

''' 현재 폴더의 views 파일의 index로 정의된 것으로 보내줘'''
urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$', views.areas)
]
