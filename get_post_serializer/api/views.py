from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# from rest_framework.views import APIView use for class based api views
# from rest_framework.decorators import api_view use for function based api views
@api_view(['GET','POST','PUT','PATCH','DELETE'])

def student_api(request,id=None):
	if request.method=='GET':
		id=id
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu=Student.objects.all()
		serializer=StudentSerializer(stu,many=True)
		return Response(serializer.data)


	if request.method=="POST":
		serializer=StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res={"message":"data is created"}
			return Response(res,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	if request.method=="PUT":
		id = id
		stu = Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {'message':'data has completely updated'}
			return Response(res)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	if request.method=="PATCH":
		id = id
		stu = Student.objects.get(id=id)
		serializer=StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'message':'data has partially updated'}
			return Response(res)
		return Response(serializer.errors)

	if request.method=='DELETE':
		id =id # id= request.data.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res={"message":'Data deleted'}
		return Response(res,status=status.HTTP_204_NO_CONTENT)