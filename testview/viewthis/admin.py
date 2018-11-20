from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Product)

admin.site.site_title = 'Django后台管理'
admin.site.site_header = 'MyDjango'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','name','weight','size','type']
	search_fields = ['id','name','type__typename']
	list_filter = ['name','type__type_name']
	ordering = ['id']
	fields = ['name','weight','size','type']
	# readonly_fields=['name']
	list_display.append('colored_type')

	def get_queryset(self, request):
		qs = super(ProductAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(id__lt=6)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'type':
			if not request.user.is_superuser:
				kwargs["queryset"] = Type.objects.filter(id__lt=4)
		return super(admin.ModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def save_model(self, request, obj, form, change):
		if change:
			user = request.user
			name = self.model.objects.get(pk=obj.pk).name
			weight = form.cleaned_data['weight']
			f = open('MyDjango_log.txt','a')
			f.write('产品: '+str(name)+', 被用户：'+str(user)+' 修改 '+'\r\n')
			f.close()
		else:
			pass
		super(ProductAdmin, self).save_model(request, obj, form, change)

	def delete_model(self, request, obj):
		pass
		super(ProductAdmin, self).delete_model(request, obj)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['id','type_name']


class PerformerAdmin(admin.ModelAdmin):
	list_display = ['id','name','nationality','masterpiece']

admin.site.register(Performer, PerformerAdmin)