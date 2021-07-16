from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_info/',views.Student_API.as_view()),
    path('stu_info/<int:id>/',views.Student_API.as_view()),
]
