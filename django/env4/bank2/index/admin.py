from django.contrib import admin

# Register your models here.
from .models import UserAccount, bankdetails

admin.site.register(bankdetails)