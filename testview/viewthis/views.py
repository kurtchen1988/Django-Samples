from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product
from django.views.generic import ListView
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
# Create your views here.
def normURL(request, year, month, day):
	return HttpResponse('Hello world | '+str(year)+' | '+str(month)+' | '+str(day))

def reURL(request, one, two):
	return HttpResponse('Hello world by RE | '+str(one)+' | '+str(two))


def paraName(request, three):
	threepara = three
	return render(request, 'three.html', locals())

def manyPara(request, four, five, six):
	fourpara = four
	fivepara = five
	sixpara = six
	return render(request, 'many.html', locals())

def download(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	writer = csv.writer(response)
	writer.writerow(['First row', 'A','B','C'])
	return response


def renderpra(request):
	a = {'threepara':'renderpra'}
	return render(request=request, template_name='three.html', context=a, content_type=None, status =500, using=None)

def redione(request):
	return redirect('/')

def reditwo(request):
	return redirect('http://127.0.0.1:8000/')

def viewpara(request):
	type_list = Product.objects.values('type')
	name_list = Product.objects.values('name','type')
	context = {'title':'首页','type_list':type_list, 'name_list':name_list}
	return render(request, 'viewpara.html', context=context,status=200)

def methodpara(request):

	if request.method=='POST':
		name = request.POST.get('name')
		return redirect('/')
	else:
		if request.GET.get('name'):
			name = request.GET.get('name')
		else:
			name = 'Everyone'
		return HttpResponse('this is a get method')

def filterFunc(request):
	context = {}
	context['title'] ='test'
	context['okok'] ='ok'
	context['manman'] = 'men'
	context['woman'] = 'women'
	context['name_list'] = ['sd','sdf','wer','rtb']
	context['ok_list'] = {'ds':'sdf'}
	return render(request,'filter.html',context=context)

def inherite(request):
	return render(request, 'inherite.html')

@cache_page(timeout=10, cache='MyDjango', key_prefix='MyDjangoView')
@login_required(login_url='/user/login')
def ShoppingCarView(request):
	pass
	return render(request, '', locals())

from django.views.generic import ListView

class ProductList(ListView):

	context_object_name = 'type_list'
	template_name = 'index_view.html'

	queryset = Product.objects.values('type').distinct()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name_list'] = Product.objects.values('name','type')
		return context

	def get_queryset(self):
		if self.kwargs['id']:
			print(self.kwargs['id'])
		print(self.kwargs['name'])
		print(self.request.method)
		type_list = Product.objects.values('type').distinct()
		return type_list

