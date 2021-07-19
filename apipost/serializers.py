from rest_framework import serializers
from .models import student


class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    reg = serializers.CharField(max_length=50)

    def create(self, vali):
        return student.objects.create(**vali)

    def update(self, instance, vali):
        instance.name = vali.get('name', instance.name)
        instance.reg = vali.get('reg', instance.reg)
        instance.save()
        return instance
