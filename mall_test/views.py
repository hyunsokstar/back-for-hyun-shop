from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 1122

class HelloWorldView(APIView):
    def get(self, request):
        return Response("Hello, world!", status=status.HTTP_200_OK)


def payment_new(request):
    return render(request, "mall_test/payment_form.html")