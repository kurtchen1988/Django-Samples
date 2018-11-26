from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, permission_required
from .form import MyUserCreationForm
import random
from .models import MyUser
# Create your views here.
def loginView(request):
	title = '登陆'
	unit_2 = '/user/register.html'
	unit_2_name = '立即注册'
	unit_1 = '/user/setpassword.html'
	unit_1_name = '修改密码'
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if User.objects.filter(username=username):
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
				return redirect('/user')
			else:
				tips='账号密码错误，请重新输入'
		else:
			tips = '用户不存在，请注册'
	return render(request, 'user.html', locals())

def index(request):
	username = request.user.username
	return render(request,'index.html',locals())

@login_required(login_url='/user/loginPerm')
@permission_required(perm='indexPerm.visit_Product', login_url='/user/loginPerm')
def indexPerm(request):
	user = request.user
	if user.has_perm('indexPerm.visit_Product'):
		return render(request, 'indexPerm.html', locals())
	else:
		return redirect('login.html')

def registerView(request):
	title = '注册'
	unit_2 = '/user/login.html'
	unit_2_name = '立即登陆'
	unit_1 = '/user/setpassword.html'
	unit_1_name = '修改密码'
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if User.objects.filter(username=username):
			tips = '用户已存在'
		else:
			user = User.objects.create_user(username=username, password=password)
			user.save()
			tips = '注册成功，请登陆'
	return render(request, 'user.html', locals())

def registerFormView(request):
	if request.method == 'POST':
		user = MyUserCreationForm(request.POST)
		if user.is_valid():
			user.save()
			tips = '注册成功'
			user = MyUserCreationForm()
	else:
		user = MyUserCreationForm()
	return render(request, 'userForm.html', locals())

def setpasswordView(request):
	title = '修改密码'
	unit_2 = '/user/login.html'
	unit_2_name = '立即登陆'
	unit_1 = '/user/register.html'
	unit_1_name = '立即注册'
	new_password = True
	if request.method == 'POST':
		username = request.POST.get('username','')
		old_password = request.POST.get('password','')
		new_password = request.POST.get('new_password','')
		if User.objects.filter(username=username):
			user = authenticate(username=username, password=old_password)
			user.set_password(new_password)
			user.save()
			tips = '密码修改成功'
		else:
			tips = '用户不存在'
	return render(request, 'user.html', locals())

def setpasswordView_1(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		old_password = request.POST.get('password','')
		new_password = request.POST.get('new_password','')

		user = User.objects.filter(username=username)
		if User.objects.filter(username=username):
			user = authenticate(new_password,None,'pbkdf2_sha256')
			user.password=dj_ps
			huser.save()
	return render(request, 'user.html', locals())


def logoutView(request):
	logout(request)
	return redirect('/user')

def findPassword(request):
	button = '获取验证码'
	new_password = False
	if request.method == 'POST':
		username = request.POST.get('username','root')
		VerificationCode = request.POST.get('VerificationCode','')
		password = request.POST.get('password','')
		user = User.objects.filter(username=username)

		if not user:
			tips = '用户' + username + '不存在'
		else:
			if not request.session.get('VerificationCode',''):
				button = '重置密码'
				tips = '验证码已发送'
				new_password = True
				VerificationCode = str(random.randint(1000,9999))
				request.session['VerificationCode'] = VerificationCode
				print(VerificationCode)
				#user[0].email_user('找回密码',VerificationCode)
			elif VerificationCode == request.session.get('VerificationCode'):
				dj_ps = make_password(password, None, 'pbkdf2_sha256')
				user[0].password = dj_ps
				user[0].save()
				del request.session['VerificationCode']
				tips = '密码已重置'
			else:
				tips = '验证码错误，请重新获取'
				new_password = False
				del request.session['VerificationCode']
	return render(request,'userPara.html',locals())

def loginPerm(request):
	tips = '请登录'
	title = '用户登录'
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if MyUser.objects.filter(username=username):
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
				return redirect('/user/indexPerm')
			else:
				tips = '账号密码错误，请重新输入'
		else:
			tips = '用户不存在，请注册'
	return render(request, 'userPerm.html', locals())

def registerPerm(request):
	title = '用户注册'
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if MyUser.objects.filter(username=username):
			tips = '用户已存在'
		else:
			user = MyUser.objects.create_user(username=username, password=password)
			user.save()
			permission = Permission.objects.filter(codename='visit_Product')[0]
			user.user_permissions.add(permission)
			return redirect('/user/login.html')
	return render(request, 'userPerm.html', locals())

def logoutPerm(request):
	logout(request)
	return redirect('/user/indexPerm')