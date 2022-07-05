from api.models import Profile
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class Test(APIView):
    def get(self, request):
        return Response("working", status=200)

    def post(self, request):
        print(request.data)
        return Response("working", status=200)


class Forms(APIView):
    def get(self, request):
        return Response("working", status=200)

    def post(self, request):
        print(request.data)
        values = ["First Name", "Middle Name", "Last Name", "Cell Phone", "Email", "Street Address", "Street Address (line 2)", "City", "State", "Zip/Postal Code", "Country", "DOB", "Country of Birth",
                  "Country Issuing Passport", "Citizenship", "Israeli Citizenship", "Israeli Passport", "Current School", "Synogogue", "High School Transcripts", "Photo", "Resume", "Password"]
        first_name, middle_name, last_name, cell_phone, email, street_address, street_address_1, \
        city, state, postal_code, country, DOB, country_of_birth, country_issuing_passport, citizenship,\
        israeli_citizenship, israeli_passport, current_school, synagogue, hs_transcripts, photo, resume, password = \
            (request.data.get(val) for val in values)
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        print(UserSerializer(user).data)
        profile = Profile.objects.create(middle_name=middle_name, cell_phone=cell_phone, address_1=street_address,
         address_2=street_address_1, city=city, state=state, postal_code=postal_code, country=country, dob=DOB, 
         country_of_birth=country_of_birth, country_issuing_passport=country_issuing_passport, citizenship=citizenship, 
         israeli_citizenship=israeli_citizenship, israeli_passport=israeli_passport, current_school=current_school, 
         synagogue=synagogue, high_school_transcripts=hs_transcripts, photo=photo, resume=resume)
        print(str(profile))
        return HttpResponse(status=200)
