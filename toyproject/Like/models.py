from django.db import models
from django.conf import settings

class Like(models.Model):
	reviewlike_id = models.IntegerField(primary_key = True)
	review_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	email = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	
  