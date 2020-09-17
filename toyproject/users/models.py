from django.db import models

class User(models.Model):
	email = models.CharField(max_length = 25, primary_key = True)
	nickname = models.CharField(max_length = 30)
	created_date = models.DateField(auto_now_add = True)