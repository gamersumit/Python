from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

#reteriveapiviews 
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#createapiview
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??  --> 'id' of object

    # redefine perform_create method that is automaticatly handled by generics
    def perform_create(self, serilaizer):
        title = serilaizer.validated_data.get('title')
        newcontent = serilaizer.validated_data.get('content') or None
        if not newcontent:
            newcontent = title
        
        # modified perform_create method to set our content equals to title if content is not provided during post api call
        # now save this data to database
        serilaizer.save(content = newcontent) # default  is serializer.save() now we added old/ empty content to the newvontent

#ListAPIView
class ProductListAPIView(generics.ListAPIView):
    '''
    NOT GONNA USE THIS METHOD
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#listcreateapiview
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??  --> 'id' of object


#UpdateAPIview
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serailizer) :
        instance = serailizer.save()
        
        if not instance.content:
            instance.content = instance.title
            instance.save()


#DestroyAPIview
class ProductDeleteAPIView(generics.DestroyAPIView):
    print("deleting")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

#shortnaming
product_create_view = ProductCreateAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_list_view = ProductListAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_delete_view = ProductDeleteAPIView.as_view()





# function api views :

@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method
 
    if method == 'GET' :
        if pk :  # SOME VALUE IS PROVIDED IN URL(OBJECT ID) MEANS USER WANT TO ACCESS GET METHOD FOR DETAILS VIEW
            instance = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(instance, many=False).data
            return Response(data)
        else :
            # if pk is none then return list of all objects as get method
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many = True).data
            return Response(data)
        
    if method == 'POST' :
        # create a new instance
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            newcontent = serializer.validated_data.get('content') or None
            
            if not newcontent:
                newcontent = title
            
            serializer.save(content = newcontent)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status = 404)