from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

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
   


#shortnaming
product_create_view = ProductCreateAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_list_view = ProductListAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()