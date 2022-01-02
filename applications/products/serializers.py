from applications.users.models import User
from django.db.models import fields
from rest_framework import serializers

from .models import Product

class CRUD_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "create_by",
            "event",
        )
    
class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'is_active',
        )