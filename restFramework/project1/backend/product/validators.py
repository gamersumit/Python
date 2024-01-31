from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product

#1
def validate_title(value):
    queryset = Product.objects.filter(title__iexact=value)
    if queryset.exists() :
        raise serializers.ValidationError(f"{value} is already a product title")
    return value

#2
def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")
    return value

#3
unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup = 'iexact')