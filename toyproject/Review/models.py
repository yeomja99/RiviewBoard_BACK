from django.db import models
from django.conf import settings

class Review(models.Model):
	review_id = models.IntegerField(primary_key = True)
	email = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	contents = models.TextField(blank = False, null = False)
	created_date = models.DateField() 
	like = models.IntegerField(default = 0)