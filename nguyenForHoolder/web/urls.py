from django.conf.urls import url
from . import views

urlpatterns = [ 
	url(r'^$', views.firstView,name=''),
	url(r'^save/$', views.Enregistrer,name='save'), 
	url(r'^loginCheck/$', views.loginCheck,name='loginCheck'), 
	url(r'^SignUp/$', views.SignUp,name='SignUp'), 
]
