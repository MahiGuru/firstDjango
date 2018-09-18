from django.contrib import admin
from .models import Category, BodyType,ClothType,FrontViewType,OccasionType
# Register your models here.
admin.site.register(Category)
admin.site.register(FrontViewType)
admin.site.register(BodyType)
admin.site.register(ClothType)
admin.site.register(OccasionType)