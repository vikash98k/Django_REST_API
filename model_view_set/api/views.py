from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer