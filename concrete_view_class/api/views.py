from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView)



class StudentListCreateAPIView(ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
