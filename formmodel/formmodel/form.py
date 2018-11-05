from django import forms
# from .models import *
from django.core.exceptions import ValidationError

# 定义表单验证方法
def weight_validate(value):
	if not str(value).isdigit():
		raise ValidationError('请输入正确的数量')

class ProductForm(forms.Form):
	name = forms.CharField(max_length = 20, label='名字', widget=forms.widgets.TextInput(attrs={'class':'c1'}), error_messages={'required':'名字不能为空'})
	# 这里的widget是
	# error_messages是字典，然后控制显示
	weight = forms.CharField(max_length = 50, label = '重量')
	size = forms.CharField(max_length = 50, label = '尺寸')
	# form里面支持非常多参数，可以在这里找到：https://docs.djangoproject.com/en/dev/ref/forms/fields/

	# dropdown box
	#choices_list = ['Phone','TV','PC']
	type = forms.ChoiceField(choices=(('ok1','Phone'),('ok2','TV'),('ok3','PC')), label='产品类型')
	# 这里的choices是元组，并且要用两级的，在内部用两个值，第一个值为提交值，第二个值为展示值
	MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
	)
	typeTwo = forms.ChoiceField(choices=MEDIA_CHOICES, label='产品类')
	# 当这里用了三层元组，则第一级元组的元素为分类（Audio，Video，unknown）