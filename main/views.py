from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceList(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceDetailAndDelete(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']

        try:
            course_instance = CourseInstance.objects.get(
                year=year, semester=semester, course_id=course_id)
            return course_instance
        except CourseInstance.DoesNotExist:
            return Response(
                {'detail': 'Course instance not found'},
                status=status.HTTP_404_NOT_FOUND
            )
