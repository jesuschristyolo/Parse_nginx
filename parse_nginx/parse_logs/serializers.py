from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Log, используемый в API.

    Мета-класс:
        model - Модель, которую сериализует данный сериализатор.
        fields - Поля модели, которые должны быть включены в сериализацию.
    """

    class Meta:
        model = Log
        fields = '__all__'
