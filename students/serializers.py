from rest_framework import serializers
from .models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
    
   
        
    
    def update(self,instance,validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance
    
    