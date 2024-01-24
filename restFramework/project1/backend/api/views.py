from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request -> httpRequest from django
    # print(dir(request))
    # request.body 
    body = request.body # byte string of JSON data
    print(body)
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse({"message": "hii there, this is your Django API response!!"})