from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)  # discount will only be defined during serializaton it will not be defined during deserialization
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
           # 'my_discount', instead i want to call it discount
            'discount',
        ]
    
    def get_discount(self, obj):
        if(isinstance(obj,Product)) :
            return obj.my_discount()
        return None