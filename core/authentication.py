from django.shortcuts import render, redirect
from django.views import View
from .models import Person
from django.contrib.auth.models import User
from .forms import LoginForm, MoreNewStudentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class StudentLoginView(View):
    template_name = 'student_login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            password = data['password']
            user = authenticate(username=name, email=email, password=password)
            person_user = User.objects.get(username=name, email=email)
            person = Person.objects.get(user=person_user)
            if user is not None and person is not None:
                print(person.is_teacher, person.is_admin)
                if not person.is_teacher and not person.is_admin:
                    login(self.request, user)
                    messages.success(request, "Logged In.")
                    return redirect('student_dashboard')
                else:
                    messages.warning(request, 'Invalid Details.')
                    return redirect('student_login')
            else:
                messages.warning(request, 'Fill in the correct credentials.')
                return redirect('student_login')
        else:
            messages.warning(request, 'An error occured. Please retry.')
            return redirect('student_login')


class TeacherLogin(View):
    template_name = 'teacher_login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            password = data['password']
            user = authenticate(username=name, email=email, password=password)
            person_user = User.objects.get(username=name, email=email)
            person = Person.objects.get(user=person_user)
            if user is not None and person is not None:
                print(person.is_teacher, person.is_admin)
                if person.is_teacher:
                    login(self.request, user)
                    messages.success(request, "Logged In.")
                    return redirect('teacher_dashboard')
                else:
                    messages.warning(request, 'Invalid Details.')
                    return redirect('teacher_login')
            else:
                messages.warning(request, 'Fill in the correct credentials.')
                return redirect('teacher_login')
        else:
            messages.warning(request, 'An error occured. Please retry.')
            return redirect('teacher_login')


class AdminLogin(View):
    template_name = 'admin_login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            password = data['password']
            user = authenticate(username=name, email=email, password=password)
            person_user = User.objects.get(username=name, email=email)
            person = Person.objects.get(user=person_user)
            if user is not None and person is not None:
                print(person.is_teacher, person.is_admin)
                if person.is_admin:
                    login(self.request, user)
                    messages.success(request, "Logged In.")
                    return redirect('admin_dashboard')
                else:
                    messages.warning(request, 'Invalid Details.')
                    return redirect('admin_login')
            else:
                messages.warning(request, 'Fill in the correct credentials.')
                return redirect('admin_login')
        else:
            messages.warning(request, 'An error occured. Please retry.')
            return redirect('admin_login')
