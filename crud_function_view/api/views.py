from django.shortcuts import render
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

class Student_API(APIView):
	def get(self,request,id=None,format=None):
		id=id
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu=Student.objects.all()
		serializer=StudentSerializer(stu,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res={"message":"data is created"}
			return Response(res,status=status.HTTP_201_CREATED)
		return Response(serializer.errors)

	def put(self,request,id,format=None):
		id = id
		stu = Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {'message':'data has completely updated'}
			return Response(res)
		return Response(serializer.errors)

	def patch(self,request,id,format=None):
		id = id
		stu = Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'message':'data has partially updated'}
			return Response(res)
		return Response(serializer.errors)

	def delete(self,request,id,format=None):
		id =id 
		stu = Student.objects.get(id=id)
		stu.delete()
		res={"message":'Data deleted'}
		return Response(res)