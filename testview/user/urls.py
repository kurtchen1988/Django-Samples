from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	path('login.html', views.loginView, name='login'),
	path('register.html', views.registerView, name='register'),
	path('setpassword.html', views.setpasswordView, name = 'setpassword'),
	path('login.html', views.logoutView, name='logout'),
	path('', views.index),
	path('findPassword.html', views.findPassword, name='findPassword'),
	#path('findPasswordVeri.html', views.findPasswordVeri, name='findPasswordVeri')
	path('admin/', admin.site.urls),
	path('registerForm', views.registerFormView),
	path('loginPerm', views.loginPerm, name='loginPerm'),
	path('registerPerm', views.registerPerm, name='registerPerm'),
	path('logoutPerm', views.logoutPerm, name='logoutPerm'),
	path('indexPerm', views.indexPerm),
]