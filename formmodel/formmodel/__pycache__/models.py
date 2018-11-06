# models.py
class Type(models.Model):
	id = models.AutoField(primary_key=True)
	type_name = models.CharField(max_length=20)
	# 设置返回值，若不设置，则默认返回Type对象
	def __str__(self):
		return self.type_name