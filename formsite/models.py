from django.db import models
from datetime import date


    
class FormData(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    names = models.CharField(max_length=100)
    birthdate = models.DateField(default=date.today)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    national_id = models.CharField(max_length=30, unique=False)
    phone_number = models.CharField(max_length=20, default="")
    province = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default = "")
    sector = models.CharField(max_length=100, default="")
    cellule = models.CharField(max_length=100, default="")
    species = models.CharField(max_length=100, default="")
    initial_qts = models.CharField(max_length = 100 ,default="0")
    villages = models.CharField(max_length=100, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names