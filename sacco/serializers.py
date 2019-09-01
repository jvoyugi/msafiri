from rest_framework import serializers
from .models import Sacco


class SaccoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sacco
        fields = '__all__'
