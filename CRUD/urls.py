from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_form, name='insert_student'),
    path('student/<int:id>/', views.student_form, name='update_student'),
    path('student/delete/<int:id>/', views.student_delete, name='delete_student'),
    path('student/list/', views.StudentList.as_view(), name='list_student')
]
