from rest_framework import serializers
from .models import schoolregister
from students.models  import student

class schoolregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=schoolregister
        exclude = ('access', 'refresh')
        read_only_fields = ('access', 'refresh')


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

    def update(self,instance,validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance