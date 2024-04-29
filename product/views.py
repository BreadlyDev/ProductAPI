from rest_framework import generics, permissions, status, response as res

from . import models as m, serializers as s


class ProductListAPIView(generics.ListAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer
