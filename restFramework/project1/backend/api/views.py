from django.http import JsonResponse
from product.models import Product
import json

def api_home(request, *args, **kwargs):
    # request -> httpRequest from django
    # print(dir(request))
    # request.body 
    # print('function called')
    # print('HTTP Method:', request.method)
    # body = request.body # byte string of JSON data
    # print(body)
    # data = {}

    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data.keys())
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # # content = request.content
    # # print(content, "= content")
    # url = request.get_full_path
    # print(url, "= url")
    # print(data['headers'], "= header")
    # print(data['content_type'], "= content_type")
    # print(request.GET, "= request.GET")
    # print(request.POST, "= request.POST")
    #<----- echo get data commit and commits before it ------->

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data :
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['price'] = model_data.price
        data['content'] = model_data.content
    return JsonResponse(data)