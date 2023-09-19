from rest_framework import serializers
from .models import Messages, Contact ,spamsMessage

class ContactSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Contact
		fields = '__all__'
		
class MessageSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Messages
		fields = '__all__'

class spamsMessageSerializer(serializers.ModelSerializer):
	class Meta: 
		model = spamsMessage
		fields = '__all__' 
