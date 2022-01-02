from rest_framework.generics import (CreateAPIView,ListAPIView,UpdateAPIView)

from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import Product
from .serializers import (CRUD_ProductSerializer, DeleteSerializer)
# Create your views here.


class CreateProduct(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CRUD_ProductSerializer
    queryset = Product.objects.all()

class List_ProductEvent(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CRUD_ProductSerializer

    def get_queryset(self):
        idEvent = self.kwargs['idEvent']

        return Product.objects.product_event(
            idEvent=idEvent
        ).filter(is_active=True)

class DeleteProduct(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeleteSerializer
    queryset = Product.objects.all()