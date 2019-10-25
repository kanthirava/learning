from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.BigIntegerField()
    address = models.TextField(default='')
    bank    = models.CharField(default='',max_length=20)
    branch  = models.CharField(default='',max_length=20)
    account_number = models.BigIntegerField(null=True, blank= True)

class bankdetails(models.Model):
    bank_name = models.CharField(max_length=30)
    bank_branch = models.CharField(max_length=30)
    bank_branchcode = models.CharField(max_length=30)
    bank_ifsc = models.CharField(max_length=30)

class AddBen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    beneficiary_name    = models.CharField(default='',max_length=30)
    beneficiary_accno   = models.BigIntegerField(null=True, blank= True)
    ifsc_code           = models.CharField(default='',max_length=20)