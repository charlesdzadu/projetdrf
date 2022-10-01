from email import header
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

from products.models import Product

@api_view(["GET"])
def api_home( request: HttpRequest , *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = ProductSerializer(model_data).data
    
    return Response(data)
