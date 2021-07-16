from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin,CreateModelMixin,
									RetrieveModelMixin,UpdateModelMixin,
									DestroyModelMixin)

# list and create pk is not required so it can be work as in one class
#class StudentList(GenericAPIView,ListModelMixin):
	#queryset = Student.objects.all()
	#serializer_class = StudentSerializer

	#def get(self,request,*args,**kwargs):
	#	return self.list(request,*args,**kwargs)

class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

# retrieve update destroy in one class
class RUDStudentAPI(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)