from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from user.models import MyUser

permission = Permission.objects.get(codename='visit_Product')
group = Group.objects.get(id=1)
group.permissions.add(permission)
group.permissions.remove(permission)
group.permissions.clear()

user = MyUser.objects.get(username='kurt2')
group = Group.objects.get(id=1)