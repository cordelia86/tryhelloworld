from django.conf.urls import url
from . import views

''' 현재 폴더의 views 파일의 index로 정의된 것으로 보내줘'''
app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates)
]
