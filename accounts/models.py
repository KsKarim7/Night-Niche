from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)], blank=True, null=True)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True,blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return f"Account no: {str(self.account_no)} ({self.user.username})"