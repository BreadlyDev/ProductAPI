from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.ProductCreateAPIView.as_view()),
    path('all', v.ProductListAPIView.as_view()),
    path('<int:pk>/', v.ProductDetailAPIView.as_view())
]
