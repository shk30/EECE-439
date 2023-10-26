from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    profession1 = models.CharField(max_length=150, default = 'False')
    profession2 = models.CharField(max_length=150, default='False')
    telnumber = models.CharField(max_length=20)
    email = models.EmailField()


    def __str__(self):
        return self.name