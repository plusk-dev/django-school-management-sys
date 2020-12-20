from django import forms
from .models import Person, Question, Homework, Submission, Answer, Room, Announcement
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#from .models import Person

class LoginForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control', 'placeholder': 'Email Address'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control', 'placeholder': 'Password'}))

class NewStudentForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email')

class MoreNewStudentForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('phone','std','address', 'is_teacher')

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('__all__')
		widgets = {
			'asker': forms.TextInput(attrs={'id': 'bruh', 'type': 'hidden'}),
		}

class HomeworkForm(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ('__all__')
		widgets = {
			'asker': forms.TextInput(attrs={'id':'asker', 'type': 'hidden'}),
			'status': forms.TextInput(attrs={'type': 'hidden'})
		}

class SubmitForm(forms.ModelForm):
	class Meta:
		model = Submission
		fields = ('__all__')
		widgets = {
			'submitter': forms.TextInput(attrs={'id': 'submitter','type': 'hidden'}),
			'hw': forms.TextInput(attrs={'id': 'hw','type': 'hidden'}),
		}

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('__all__')
		widgets = {
			'author': forms.TextInput(attrs={'id': 'author','type': 'hidden'}),
			'que': forms.TextInput(attrs={'id': 'question','type': 'hidden'}),
			'status': forms.TextInput(attrs={'type': 'hidden'})
		}

class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ('__all__')
		widgets = {
			'host': forms.TextInput(attrs={'id': 'host', 'type': 'hidden'})
		}

class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = '__all__'
		