# from django.http import JsonResponse  # instead 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from django.forms.models import model_to_dict
from product.serializers import ProductSerializer
import json

# def api_home(request, *args, **kwargs):
#     # request -> httpRequest from django
#     # print(dir(request))
#     # request.body 
#     # print('function called')
#     # print('HTTP Method:', request.method)
#     # body = request.body # byte string of JSON data
#     # print(body)
#     # data = {}

#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass
#     # print(data.keys())
#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type
#     # # content = request.content
#     # # print(content, "= content")
#     # url = request.get_full_path
#     # print(url, "= url")
#     # print(data['headers'], "= header")
#     # print(data['content_type'], "= content_type")
#     # print(request.GET, "= request.GET")
#     # print(request.POST, "= request.POST")
#     #<----- echo get data commit and commits before it ------->

#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data :
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['price'] = model_data.price
#         # data['content'] = model_data.content
#         # <!----- instead ------->
#         data = model_to_dict(model_data)
#         # also 
#         # data = model_to_dict(model_data, fields = ['id', 'title']) # taking some part/keys of our model
#     return JsonResponse(data)

# <---------- django meodel instance to dictonary coomit ----- >


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """ 
    Django Rest Framework API VIEW

    """
    # model_data = Product.objects.all().order_by("?").first()
    # data = request.data
    data = {}
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        # print("all good")
        instance = serializer.save()
        # print(instance)
        data = ProductSerializer(instance).data
        # print(data)
        # data = serializer.data
        # print(data)
    # #     return Response(serializer.data)
    # # instance = Product.objects.all().order_by("?").first()
    # # data = {}
    # # if instance :
    # #     ## data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
    # #     data = ProductSerializer(instance).data
    return Response(data)
    # return Response({"invalid": "not good data"}, status = 400)
   