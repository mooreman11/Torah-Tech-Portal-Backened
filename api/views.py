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
        values = ["First Name", "Middle Name", "Last Name", "Cell Phone", "Email", "Street Address",
                  "Street Address (line 2)", "City", "State", "Zip/Postal Code", "Country", "DOB", "Country of Birth",
                  "Country Issuing Passport", "Citizenship"]
        first_name, middle_name, last_name, cell_phone, email, street_address, street_address_1, city, state, \
        postal_code, country, DOB, country_of_birth, country_issuing_passport, citizenship = \
            (request.data.get(val) for val in values)
        print(first_name, last_name, email, )
        return HttpResponse(status=200)
