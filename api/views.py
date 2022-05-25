import django
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AddProductsSerializer

from api.models import AddProduct

from api import serializers
# Create your views here.




@api_view(['GET'])
def apiOverviews(request):
    api_url={
        'users':'/api/product',
        'user-details':'/api/product-details/<str:pk',
        'create':'/api/product-create',
        'update':'/api/product-update/<str:pk>',
        'delete':'/api/product-delete/<str:pk>',
            }
    return Response(api_url)



@api_view(['GET'])
def Products(request):
    productAll=AddProduct.objects.all()
    serializers=AddProductsSerializer(productAll,many=True)
    return Response(serializers.data)



@api_view(['GET'])
def SingleProducts(request,pk):
    product=AddProduct.objects.get(id=pk)
    serializers=AddProductsSerializer(product,many=False)
    return Response(serializers.data)



@api_view(['POST'])
def CreateProduct(request):
    serializers = AddProductsSerializer(data = request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)




@api_view(['POST'])
def ProductUpdate(request,pk):
    product=AddProduct.objects.get(id=pk)
    serializers = AddProductsSerializer(instance=product, data = request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)



@api_view(['DELETE'])
def ProductDelete(request,pk):
    product=AddProduct.objects.get(id=pk)

    product.delete()

    return Response("Its Successfully delete!")