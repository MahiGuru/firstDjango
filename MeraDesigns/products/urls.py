from django.urls import path
from .views import index, getCategorys

urlpatterns = [
	path('', index, name='index'),
	path('categorys', getCategorys, name="getCategorys")
]
