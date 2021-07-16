from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('stu_info/',views.StudentList.as_view()),
    #path('stu_info/',views.StudentCreate.as_view()),
    #path('stu_info/<int:pk>/',views.StudentUpdate.as_view()),
    #path('stu_info/<int:pk>/',views.StudentDestroy.as_view()),
    #path('stu_info/<int:pk>/',views.StudentRetrieve.as_view()),
    path('stu_info/',views.StudentListCreateAPIView.as_view()),
    path('stu_info/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view())

]