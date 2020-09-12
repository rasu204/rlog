from django.db import models


# Create your models here.
class Mandates(models.Model):
    JDCode = models.TextField(unique=True)
    VacancyCode = models.TextField(null=True)
    Title = models.TextField(null=True)  # Job Title
    Location = models.TextField(null=True)
    HiringManager = models.TextField(null=True)
    RequisitionManager = models.TextField(blank=True)
    KeySkills = models.TextField(null=True)
    Role = models.TextField(blank=True)
    DesiredExperience = models.TextField(blank=True)
    Education = models.TextField(null=True)
    MinExpRange = models.IntegerField(null=True)
    MaxExpRange = models.IntegerField(null=True)
    CTC = models.IntegerField(blank=True)
    NoticePeriod = models.IntegerField(blank=True)
    Status = models.TextField(max_length=1)
    Openings = models.IntegerField(null=True)
    No_Filled = models.IntegerField(null=True)
    HiringMgrContact = models.IntegerField(null=True)
    HiringMgrEmail = models.TextField(null=True)
    RecruiterAssignedTo = models.ForeignKey('user.User', on_delete=models.RESTRICT)
    AssignedDate = models.DateField(null=True)
    ClientID = models.ForeignKey('records.Client', on_delete=models.RESTRICT)
