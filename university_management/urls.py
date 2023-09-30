# management_system/urls.py

from django.urls import path
from management_system import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
]
