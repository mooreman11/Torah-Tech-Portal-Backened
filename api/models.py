from django.db import models


# Create your models here.

# class HealthForm(models.Model):
#     name = models.CharField(max_length=128)
#     file = models.FileField(max_length=5, upload_to="health_forms/")


# class DisclosureAgreement(models.Model):
#     name = models.CharField(max_length=128)

def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'v5/{instance.user.first_name}_{ instance.user.last_name}'

class Profile(models.Model):
    middle_name = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dob = models.DateField()
    country_of_birth = models.CharField(max_length=255)
    country_issuing_passport = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    israeli_citizenship = models.BooleanField()
    israeli_passport = models.BooleanField()
    current_school = models.CharField(max_length=255)
    synagogue = models.CharField(max_length=255)
    high_school_transcripts = models.FileField(upload_to=f'{user_directory_path}/high_school_transcripts')
    photo = models.ImageField()
    resume = models.FileField(upload_to=f'{user_directory_path}/resume')
