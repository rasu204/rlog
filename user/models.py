from django.db import models

# Create your models here.

class User(models.Model):
    # UserID = models.IntegerField(primary_key = True)
    FullName = models.TextField(null = True)
    UserType = models.TextField(null = True)
    UserDescription = models.TextField(null = True)
    UserCompany = models.TextField(null = True)
    UserStatus = models.TextField(max_length = 1, null = True)
    UserReportsTo = models.ForeignKey('self', null = True, on_delete = models.RESTRICT, blank = True)
    Password = models.TextField(null = True)
    CreatedOn = models.DateField(auto_now_add = True, null = True)
    Role = models.TextField(null = True)
    Designation = models.TextField(null = True)
    Phone = models.IntegerField(null = True)
    EmailID = models.EmailField(null = True)
    Department = models.TextField(blank = True)
    ValidTill = models.DateField(null = True)
