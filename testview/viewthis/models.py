from django.utils.html import format_html
from django.db import models

# Create your models here.
class Type(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	type_name = models.CharField(verbose_name='产品类型',max_length=20)

	def __str__(self):
		return self.type_name

class Product(models.Model):
	id = models.AutoField('序号',primary_key=True)
	name = models.CharField('名称',max_length=50)
	weight = models.CharField('重量',max_length=20)
	size = models.CharField('尺寸',max_length=20)
	type = models.ForeignKey(Type, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '产品信息'
		verbose_name_plural = '产品信息'

	def get_readonly_fields(self, request, obj=None):
		if request.user.is_superuser:
			self.readonly_fields = []
		return self.readonly_fields

	def colored_type(self):
		if 'V1' in self.type.type_name:
			color_code = 'red'
		elif 'V2' in self.type.type_name:
			color_code = 'blue'
		elif 'V3' in self.type.type_name:
			color_code = 'Blue'
		else:
			color_code = 'Yellow'
		return format_html('<span style="color: {};">{}</span>', color_code, self.type,)

	colored_type.short_description='带颜色的产品类型'

class Performer(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=20)
	nationality = models.CharField(max_length=20)
	masterpiece = models.CharField(max_length=50)

class Performer_info(models.Model):
	id = models.IntegerField(primary_key=True)
	performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
	birth = models.CharField(max_length=20)
	elapse = models.CharField(max_length=20)

class Program(models.Model):
	id = models.IntegerField(primary_key=True)
	performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)

class ProgramAnother(models.Model):
	id = models.IntegerField(primary_key=True)
	performer = models.ManyToManyField(Performer)