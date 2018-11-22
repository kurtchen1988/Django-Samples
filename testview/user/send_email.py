from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def send():
	from_email = settings.DEFAULT_FROM_EMAIL
	send_mail('MyDjango', 'This is Django', from_email, ['554301449@qq.com'])
	message1 = ('MyDjango','This is Django', from_email, ['554301449@qq.com'])
	message2 = ('MyDjango','Hello Django', from_email, ['554301449@qq.com'])
	send_mass_mail((message1, message2), fail_silently=False)
	content = '<p>This is an <strong>important</strong> email</p>'
	msg = EmailMultiAlternatives('MyDjango',content,from_email,['554301449@qq.com'])
	msg.content_subtype = 'html'
	msg.attach_alternative('<strong>This is from Django</strong>','text/html')
	msg.attach_file('files')
	msg.send()