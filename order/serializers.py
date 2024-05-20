from rest_framework import serializers
from . import models as m


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Order
        fields = '__all__'
