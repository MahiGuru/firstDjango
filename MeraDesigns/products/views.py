from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Category, FrontViewType,BodyType, OccasionType,ClothType
# Create your views here.
def index(request):
	# return HttpResponse("Hello World")
	return render(request, 'category.html')

def getCategorys(request):
	categorys = Category.objects.all()
	context = {}
	context['categorys'] = categorys
	return render(request, 'category.html', context)

class GetCategory(View):
	def get(self, request, categoryId):
		print(categoryId)
		context = {}
		return render(request, 'categoryOne.html', context)