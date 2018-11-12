from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def model_index(request, id):
	if request.method == 'GET':
		instance = Product.objects.filter(id=id)
		if instance:
			product = ProductModelForm(instance=instance[0])
		else:
			product = ProductForm()
		return render(request, 'index.html', locals())
	else:
		product = ProductModelForm(request.POST)
		if product.is_valid():
			weight = product.cleaned_data['weight']
			product_db = product.save(commit=False)
			product_db.name = 'my iphone'
			product_db.save()
			return HttpResponse('提交成功，清洗的数据为：'+weight)
		else:
			error_msg = product.errors.as_json()
			print(error_msg)
			return render(request, 'index.html', locals())

def index(request):
	return HttpResponse('this is the fuck!')