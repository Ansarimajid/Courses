from django.urls import path
from . import views

urlpatterns = [
    path('api/courses/', views.CourseList.as_view()),
    path('api/courses/<int:pk>/', views.CourseDetail.as_view()),
    path('api/instances/', views.CourseInstanceList.as_view()),
    path('api/instances/<int:pk>/', views.CourseInstanceDetail.as_view()),
    path('api/instances/<int:year>/<int:semester>/<int:course_id>/',
        views.CourseInstanceDetailAndDelete.as_view(), name='course-instance-detail-delete'),


]
