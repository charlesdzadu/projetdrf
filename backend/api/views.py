from django.http import JsonResponse, HttpRequest
import json



def api_home( request: HttpRequest , *args, **kwargs):
    body = request.body
    data = {}
    data = json.loads(body)
    data['params'] = request.GET
    data['content'] = request.content_type
    data['headers'] = dict(request.headers)
    return JsonResponse(data)
