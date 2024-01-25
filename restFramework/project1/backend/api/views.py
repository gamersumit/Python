from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request -> httpRequest from django
    # print(dir(request))
    # request.body 
    print('function called')
    print('HTTP Method:', request.method)
    body = request.body # byte string of JSON data
    print(body)
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # content = request.content
    # print(content, "= content")
    url = request.get_full_path
    print(url, "= url")
    print(data['headers'], "= header")
    print(data['content_type'], "= content_type")
    print(request.GET, "= request.GET")
    print(request.POST, "= request.POST")
    return JsonResponse(data)