from django.urls import path, re_path
from .views import normURL, reURL, paraName, manyPara, download, renderpra, redione, reditwo, viewpara, methodpara, ProductList

urlpatterns = [ path('<int:year>/<month>/<slug:day>', normURL),
				re_path('(?P<one>[0-9]{4})/(?P<two>[0-9]{2})/', reURL),
				re_path('(?P<three>[0-9]{4})/', paraName, name='threepara'),
				path('', manyPara, {'four':'04', 'five':'05','six':'06'}), 
				path('download', download),
				path('renderpra', renderpra),
				path('redione', redione),
				path('reditwo', reditwo),
				path('viewpara',viewpara),
				path('methodpara', methodpara),
				path('commonview', ProductList.as_view(), {'id':1, 'name':'phone'}),
				path('commonview/<id>.html', ProductList.as_view(),{'name':'phone'}),
				]