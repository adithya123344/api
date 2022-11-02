from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class deskStatus(models.Model):
   
    user_name=models.CharField(max_length=10,default='adi')
    booked_date=models.DateTimeField(auto_now_add=True)
    desk_value=models.CharField(max_length=10,primary_key=True,default='n')
    desk_status=models.IntegerField(default=0)

    def __str__(self):
        return self.desk_value