from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('student_registration/',views.student_register,name='student_register')
]