from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)  # discount will only be defined during serializaton it will not be defined during deserialization
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',
    )

    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'url',
            'email',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
           # 'my_discount', instead i want to call it discount
            'discount',
        ]
    # overriding create method of Serializers
    # def create(self, validated_data):
    #   #  email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #    # print(email, obj)
    #     return obj
    
    def get_discount(self, obj):
        if(isinstance(obj,Product)) :
            return obj.my_discount()
        return None
    
    def get_url(self, obj):
        request = self.context.get('request')
        if not request :
            return None
        
        return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)