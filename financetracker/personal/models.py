from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class dailyadd(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    grocery=models.CharField(max_length=5000)
    onlinepayment=models.CharField(max_length=5000)
    datetime=models.CharField()
    total=models.CharField()
    
class Monthlyadd(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)
    
    income=models.CharField()
    rent=models.CharField()
    Utilities=models.CharField()
    Subscriptions=models.CharField(max_length=50)
    food=models.CharField()
    transport=models.CharField()
    shopping=models.CharField()
    bank=models.CharField()
    SIP=models.CharField()
    Festival=models.CharField()
    Medical=models.CharField()
    month=models.CharField()
    
    
    totalspent=models.CharField()
    fixed_expenses =models.CharField()
    varaiable_expenses=models.CharField()
    saving=models.CharField()
    sessional=models.CharField()
