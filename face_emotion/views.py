from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            params = request.GET.get('sentence')

# def index(request):
#     return HttpResponse({'a':1})
#
#
# def getUserMessage(request):
#     if request.method == 'POST':
#         temp = {}
#         temp['name'] = request.POST.get('name')
#         temp['phone_number'] = request.POST.get('phone_number')
#         temp['email'] = request.POST.get('email')
#         temp['Data'] = request.POST.get('Data')
