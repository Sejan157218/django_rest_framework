from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import AddProduct

class AddProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddProduct
        fields='__all__'