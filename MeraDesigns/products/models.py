import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	type = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	imgPath = models.CharField(max_length=100)
	created_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	updated_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	def __str__(self):
		return self.type
	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class FrontViewType(models.Model):
	type = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	imgPath = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	updated_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	def __str__(self):
		return self.type
	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class BodyType(models.Model):
	type = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	imgPath = models.CharField(max_length=100)
	created_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	updated_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	def __str__(self):
		return self.type
	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class OccasionType(models.Model):
	type = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	imgPath = models.CharField(max_length=100)
	created_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	updated_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	def __str__(self):
		return self.type
	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class ClothType(models.Model):
	type = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	imgPath = models.CharField(max_length=100)
	created_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	updated_at = models.DateTimeField(default=datetime.datetime.now,blank=True)
	def __str__(self):
		return self.type
	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)
