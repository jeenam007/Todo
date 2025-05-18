
from rest_framework import serializers
from todoapp.models import Todos
class todoSerializer(serializers.Serializer):
    task_name=serializers.CharField()
    status=serializers.CharField()
    user=serializers.CharField()
    date=serializers.DateField()

    def create(self, validated_data):
            # Create a new todo object
        return Todos.objects.create(**validated_data)
    