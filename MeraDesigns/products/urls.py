from django.urls import path
from .views import index, getCategorys, GetCategory

urlpatterns = [
	path('', index, name='index'),
	path('categorys', getCategorys, name="getCategorys"),
	path('category/<int:categoryId>', GetCategory.as_view())
]
