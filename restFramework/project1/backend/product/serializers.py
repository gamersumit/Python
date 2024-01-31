from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from api.serializers import UserPublicSerializer
from .validators import validate_title, unique_product_title, validate_title_no_hello




class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True,
    )
    title = serializers.CharField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only = True)
    related_products = ProductInlineSerializer(source = 'user.product_set.all', read_only = True, many=True)
    discount = serializers.SerializerMethodField(read_only=True)  # discount will only be defined during serializaton it will not be defined during deserialization
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',
    )
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])
    name = serializers.CharField(source = 'title', read_only = True)
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'url',
            'owner',
            'related_products',
            # 'user',
            #'email',
            'edit_url',
            'title',
            'name',
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
    
    # custom validation :
    # override property validation method validate_property()
    
    # def validate_title(self, value):
    #     request = self.context.request('request')
    #     user = request.user
    #     queryset = Product.objects.filter(user = user, title__iexact=value)
    #     if queryset.exists() :
    #         raise serializers.ValidationError(f"{value} is already a product title")
    #     return value
    
