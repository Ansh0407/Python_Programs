
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Empty path for the homepage
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
]

