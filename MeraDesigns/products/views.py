from django.shortcuts import render
from django.http import HttpResponse
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