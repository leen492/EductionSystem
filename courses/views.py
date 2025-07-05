from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
class CourseList (APIView):
    def get(self,request):
        mycourses= Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
