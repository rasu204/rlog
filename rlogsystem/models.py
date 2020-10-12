from django.db import models


# Create your models here.

class CandidateStatus(models.Model):
    TYPE = [('SELECT', 'Select'),
            ('REJECT', 'Reject')]

    CompanyID = models.IntegerField(null=True)
    StageID = models.IntegerField(unique=True, null=True)
    StageName = models.TextField(null=True)
    StageType = models.CharField(null=True, choices=TYPE, max_length=6)


class Agency(models.Model):
    AgencyName = models.TextField(null=True)
    Location = models.TextField(null=True)
    Website = models.TextField(null=True)
    ContractStartedOn = models.DateField(null=True)
    ContractValidTill = models.DateField(null=True)
    KCName = models.TextField(null=True)
    KCEmail = models.EmailField(null=True)
    KCPhone = models.IntegerField(null=True)

    def __str__(self):
        return self.AgencyName
