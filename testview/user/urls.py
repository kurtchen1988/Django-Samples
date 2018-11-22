from django.urls import path
from . import views

urlpatterns = [
	path('login.html', views.loginView, name='login'),
	path('register.html', views.registerView, name='register'),
	path('setpassword.html', views.setpasswordView, name = 'setpassword'),
	path('login.html', views.logoutView, name='logout'),
	path('', views.index),
	path('findPassword.html', views.findPassword, name='findPassword'),
	#path('findPasswordVeri.html', views.findPasswordVeri, name='findPasswordVeri')
]