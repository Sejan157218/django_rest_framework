import django
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.




@api_view(['GET'])
def apiOverviews(request):
    api_url={
        'users':'/api/users',
        'user-details':'/api/user-details/<str:pk',
        'create':'/api/user/create',
        'update':'/api/user-update/<str:pk>',
        'delete':'/api/user-delete/<str:pk>',
            }
    return Response(api_url)
    