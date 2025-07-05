from django.urls import path 
from .views import CourseList
urlpatterns=[
    path('courses/',
         CourseList.as_view())
]