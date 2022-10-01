
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import Product


class ProductSerializer(ModelSerializer):

    # Définir un attribut en lecture seul pour pourvoir changer de nom
    my_discount = SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # La méthode get_my_discount pour lé définir à partir de la méthode get_discount du model 
    def get_my_discount(self, obj):
        return obj.get_discount()
