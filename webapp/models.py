from django.db import models
# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField(max_length=20)
    mob=models.IntegerField()
    password = models.CharField(max_length=8)

    def __str__(self):
        return str(self.id)