from rest_framework import generics, permissions, status, response as res
from . import models as m, serializers as s


class OrderListAPIView(generics.ListAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer
