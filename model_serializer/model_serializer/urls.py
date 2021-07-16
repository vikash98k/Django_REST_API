
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
	#path('stuapi/',views.student_api),
	path('studentapi/',views.Student_api.as_view()),
    path('admin/', admin.site.urls),
]
