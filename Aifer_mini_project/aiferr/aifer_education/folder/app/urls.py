from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.student_register, name='student_register'),
    path('eligible-courses/<int:student_id>/', views.eligible_courses,
         name='eligible_courses'),
]
