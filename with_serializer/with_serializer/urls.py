from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_info/',views.student_api),
    path('stu_info/<int:pk>/',views.student_api),
]