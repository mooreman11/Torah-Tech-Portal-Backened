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
        return Response("working", status=200)
