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

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['id','type_name']


class PerformerAdmin(admin.ModelAdmin):
	list_display = ['id','name','nationality','masterpiece']

admin.site.register(Performer, PerformerAdmin)