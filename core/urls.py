from django.urls import path
from .views import TeacherDashboard,StudentDashboard,AdminDashboard,CreatePerson, CreateHomework,SubmitHW, SingleQuestion, AnnouncementsView,PrivateAnnouncements ,CreateExamView

from .home import IndexView, HomeView
from .authentication import StudentLoginView, TeacherLogin, AdminLogin
from .room import CreateRoom
from .general import deleteRoom, deleteAnswer, deletePerson, signout, markCorrect, markHWCorrect

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('home/', HomeView.as_view(), name='home'),
	path('announcements/', AnnouncementsView.as_view(), name='announcements'),
	path('logout/', signout, name='logout'),
	path('student_login/', StudentLoginView.as_view(), name='student_login'),
	path('teacher_login/', TeacherLogin.as_view(), name='teacher_login'),
	path('admin_login', AdminLogin.as_view(), name='admin_login'),
	path('student_dashboard/', StudentDashboard.as_view(), name='student_dashboard'),
	path('teacher_dashboard/', TeacherDashboard.as_view(), name='teacher_dashboard'),
	path('admin_dashboard/', AdminDashboard.as_view(), name='admin_dashboard'),
	path('admin_dashboard/new_student/', CreatePerson.as_view(), name='create_person'),
	path('admin_dashboard/create_exam/', CreateExamView.as_view(), name='create_exam'),
	path('homework/<int:pk>/', SubmitHW.as_view(), name='submit_hw'),
	path('private_announcements/', PrivateAnnouncements.as_view(), name='pvt_announcements'),
	path('question/<int:pk>/', SingleQuestion.as_view(), name='question'),
	path('question/delete/<int:pk>/', deleteAnswer, name='delete_ans'),
	path('question/markCorrect/<int:pk>', markCorrect, name='markCorrect'),
	path('homework/markCorrect/<int:pk>', markHWCorrect, name='markHWCorrect'),
	path('teacher_dashboard/create_room/', CreateRoom.as_view(), name='create_room'),
	path('teacher_dashboard/delete_room/<int:pk>', deleteRoom, name='delete_room'),
	path('admin_dashboard/delete/<int:pk>', deletePerson, name='delete_person'),
	path('teacher_dashboard/create_homework', CreateHomework.as_view(), name='create_homework')
]