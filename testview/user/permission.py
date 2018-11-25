from django.core.management.base import BaseCommand
from user.models import MyUser
from django.contrib.auth.models import Permission


class Command(BaseCommand):
	def handle(self):
		__main__

if __name__ == '__main__':
	user = MyUser.objects.filter(username='kurt2')
	user.has_perm('index.add_product')
	permission = Permission.objects.filter(codename = 'add_product')[0]
	user.user_permissions.add(permission)
	user.has_perm('index.add_product')
	user = MyUser.objects.filter(username='kurt2')[0]
	user.user_permissions.remove(permission)
	user.has_perm('index.add_product')
	user.user_permissions.clear()
	user.user_permissions.add(permission)
	user.user_permissions.values()