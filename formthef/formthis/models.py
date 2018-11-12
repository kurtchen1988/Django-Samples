from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 20, verbose_name = '名字')
	weight = models.CharField(max_length = 20, verbose_name = '重量')
	size = models.CharField(max_length = 20, verbose_name = '尺寸')
	type = models.CharField(max_length = 20, verbose_name = '产品类型')

class Type(models.Model):
	id = models.AutoField(primary_key = True)
	type_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.type_name