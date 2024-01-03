
from rest_framework import serializers
from .models import Meseros

class MeserosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ('nombre', 'edad', 'pais', 'nacionalidad')