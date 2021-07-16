from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
	def list(self,request):
		stu = Student.objects.all()
		serializer= StudentSerializer(stu,many=True)
		return Response(serializer.data)

	def retrieve(self,request,pk=None):
		id=pk
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			return Response(serializer.data)

	def create(self,request):
		serializer=StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {"message":"data created"}
			return Response(res,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,pk):
		id=pk
		stu=Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {"message":"data updated"}
			return Response(res)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self,request,pk):
		id=pk
		stu=Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {"message":"data updated partially"}
			return Response(res)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,pk):
		id=pk
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'message':"data deleted"}
		return Response(res)

