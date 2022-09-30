from email import header
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product

@api_view(["GET"])
def api_home( request: HttpRequest , *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    
    data = model_to_dict(model_data, exclude=['id'])
    data['sale_price'] = model_data.sale_price
    
    return Response(data)
