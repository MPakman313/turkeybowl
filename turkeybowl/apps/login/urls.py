from django.conf.urls import patterns, url
from apps.login import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<team_id>\d+)/$', views.dashboard, name='dashboard'),
	)