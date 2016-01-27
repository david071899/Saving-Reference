from django.db import models
import ast 
from django.contrib.auth.models import User
# Create your models here.

class Collection(models.Model):
	collecter=models.OneToOneField(User, on_delete=models.CASCADE)

class Art(models.Model):
	name=models.CharField(max_length=255)
	adder=models.ForeignKey(User, on_delete=models.CASCADE)
	collecter=models.ManyToManyField(Collection)
	def  __unicode__(self):
		return self.name

class ListField(models.TextField):
	__metaclass__ = models.SubfieldBase
	description = "Stores a python list"

	def __init__(self, *args, **kwargs):
		super(ListField, self).__init__(*args, **kwargs)

	def to_python(self, value):
		if not value:
			value = []

		if isinstance(value, list):
			return value

		return ast.literal_eval(value)

	def get_prep_value(self, value):
		if value is None:
			return value

		return unicode(value)

	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)

class Tag(models.Model):
	style=ListField()
	description=models.CharField(max_length=255)
	pic_url= ListField()
	art=models.ForeignKey(Art)
