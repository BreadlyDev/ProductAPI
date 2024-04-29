from rest_framework import serializers
from . import models as m


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = '__all__'
