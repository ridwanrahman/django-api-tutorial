from django.db import models

# Create your models here.
class data(models.Model):
	name = models.CharField(max_length=120, null=True, blank=True)
	number = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name
