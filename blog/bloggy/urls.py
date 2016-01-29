from django.conf.urls import patterns, url
from bloggy import views


# Create route for home page.
urlpatterns = patterns(
	'bloggy.views',
	url(r'^$', views.index, name='index'),
	url(r'^add_post', views.add_post, name='add_post'),
)