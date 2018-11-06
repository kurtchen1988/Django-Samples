# views.py的视图函数model_index
from django.shortcuts import render
from django.http import HttpResponse
from .from import *
def model_index(request, id):
	if request.method == 'GET':
		instance = Product.objects.filter(id=id)
		# 判断数据是否存在
		if instance:
			product = ProductModelForm(instance = instance[0])
		else:
			product = ProductModelForm()
			if product.is_valid():
				# 获取weight的数据，并通过clean_weight进行清洗，转换成Python数据类型
				weight = product.cleaned_data['weight']
				# 数据保存方法一
				# 直接将数据保存到数据库
				# product.save()
				# 数据保存方法二
				# save方法设置commit = False，将生成数据库对象product_db，然后对该对象的属性值修改并保存
				product_db = product.save(commit=False)
				product_db.name = '我的iphone'
				product_db.save()
				# 数据保存方法三
				# save_m2m()方法用于保存ManyToMany的数据模型
				# product.save_m2m()
				return HttpResponse('提交成功！weight清洗后的数据为：'+weight)
			else:
				# 将错误信息输出，error_msg是将错误信息以json格式输出
				error_msg = product.error_msg.as_json()
				print(error_msg)
				return render(request, 'data_form.html', locals())