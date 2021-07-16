from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	# method-1 name=serializers.CharField(read_only=True) # name only read it cannot be changed 
	class Meta:
		model =Student
		fields=['name','roll','city']
		#read_only_fields= ['name'] # method-2
		extra_kwargs={'name':{'read_only':True}}