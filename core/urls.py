from django.conf.urls import url

from kurokotv.core.views import home

urlpatterns = [
	url(r'^$', home, name='home'),

]