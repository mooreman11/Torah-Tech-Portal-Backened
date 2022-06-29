from django.db import models


# Create your models here.

class HealthForm(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(max_length=5, upload_to="health_forms/")


class DisclosureAgreement(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(max_length=5, upload_to="disclosure_agreement/")
