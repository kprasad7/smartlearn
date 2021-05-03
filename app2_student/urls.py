from django.urls import path
from app2_student import views
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
path('studentlogin', LoginView.as_view(template_name='student/slogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path("student-main" , views.student_main , name="studentmain"),
path('student-exam', csrf_exempt(views.student_exam_view),name='student-exam'),
path('student-exam1', csrf_exempt(views.student_exam_view1),name='student-exam1'),
path('student-exam2', csrf_exempt(views.student_exam_view2),name='student-exam2'),
path('student-exam3', csrf_exempt(views.student_exam_view3),name='student-exam3'),
path('student-exam5', csrf_exempt(views.student_exam_view5),name='student-exam5'),
path('student-exam4', csrf_exempt(views.student_exam_view4),name='student-exam4'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('calculate-marks', csrf_exempt(views.calculate_marks_view),name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),

]