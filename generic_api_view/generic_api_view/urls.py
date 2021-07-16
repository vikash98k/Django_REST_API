from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('stu_info/',views.student_api),
    #path('stu_info/<int:id>/',views.student_api),
    #path('stu_info/',views.StudentList.as_view()),
    #path('stu_info/',views.StudentCreate.as_view()),
    #path('stu_info/<int:pk>/',views.StudentRetrieve.as_view()),
    #path('stu_info/<int:pk>/',views.StudentUpdate.as_view()),
    #path('stu_info/<int:pk>/',views.StudentDestroy.as_view()),
    
    path('stu_info/',views.LCStudentAPI.as_view()),
    path('stu_info/<int:pk>/',views.RUDStudentAPI.as_view()),

]