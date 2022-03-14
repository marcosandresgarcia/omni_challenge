from .models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    units = serializers.CharField(source='get_units', read_only=True)

    class Meta:
        model = Products
        exclude = ("created_at", "updated_at", "delete_at", "state")


class UnitsProductSerializer(serializers.Serializer):
    units = serializers.IntegerField()


