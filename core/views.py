from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewStudentForm, QuestionForm, HomeworkForm, SubmitForm, AnswerForm, RoomForm, AnnouncementForm
from .models import Person, Homework, Question, Submission, Answer, Room, Announcement
import datetime
from .quotes import quote


class AnnouncementsView(View):
    template_name = 'announcements.html'
    def get(self,request):
        announcements = Announcement.objects.filter(public=True).order_by('-date')
        return render(request, self.template_name, {'anns': announcements})

class PrivateAnnouncements(LoginRequiredMixin, View):
    template_name = 'pvt_announcements.html'

    def get(self, request):
        announcements = Announcement.objects.filter(public=False).order_by('-date')
        return render(request, self.template_name, {'anns': announcements})


#******************DASHBOARDS******************#
class StudentDashboard(LoginRequiredMixin, View):
    template_name = 'sdash.html'

    def get(self, request):
        person = Person.objects.get(user=request.user)
        if person and not person.is_teacher and not person.is_admin:
            hws_list = Homework.objects.filter(std=person.std).order_by('-date')
            ques_list = Question.objects.all().order_by('-date')
            subs = Submission.objects.filter(submitter=person).order_by('-date')
            date_today = datetime.datetime.now().date()
            ques = []
            for n in ques_list:
                if n.date.date() == date_today:
                    ques.append(n)
                    print(ques)
            hws = []
            for i in hws_list:
                if i.date.date() == date_today:
                    hws.append(i)
                    print(hws)
            rooms = Room.objects.filter(std=person.std)
            return render(request, self.template_name, {'hws': hws, 'ques': ques, 'subs': subs, 'allhw': hws_list, 'allques': ques_list, 'rooms': rooms, 'quote': quote()[0]})
        else:
            messages.warning(request, 'You are not authorized to login as a student.')
            return redirect('index')

class SingleQuestion(LoginRequiredMixin, View):
    template_name = 'question.html'

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        form = AnswerForm()
        answers = Answer.objects.filter(que=question)
        if question.date.date() == datetime.datetime.now().date():
            print('ITS TODAY')
        return render(request, self.template_name, {"form": form, 'que': question, 'answers': answers})

    def post(self, request, pk):
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')


class TeacherDashboard(LoginRequiredMixin, View):
    template_name = 'tdash.html'

    def get(self, request):
        date_today = datetime.datetime.now().date()
        person = Person.objects.get(user=request.user)
        if person and person.is_teacher:
            hws_list = Homework.objects.filter(asker=person).order_by('-date')
            ques_list = Question.objects.filter(asker=person).order_by('-date')
            ques = []
            rooms = Room.objects.filter(host=person)
            for n in ques_list:
                if n.date.date() == date_today:
                    ques.append(n)
                    print(ques)
            hws = []
            for i in hws_list:
                if i.date.date() == date_today:
                    hws.append(i)
                    print(hws)

            form = QuestionForm()
            hw_form = HomeworkForm()
            return render(request, self.template_name, {'hws': hws, 'ques': ques, 'form': form, 'hwform': hw_form, 'allhw': hws_list, 'allques': ques_list, 'rooms': rooms, 'quote': quote()[0]})
        else:
            messages.warning(request, 'You are not authorized to login as a teacher.')
            return redirect('index')

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asked Successfully.')
            return redirect('teacher_dashboard')
        else:
            messages.warning(
                request, "The Question could not be asked. Please try again.")
            return redirect('teacher_dashboard')


class CreateHomework(LoginRequiredMixin, View):
    def post(self, request):
        person = Person.objects.get(user=request.user)
        if person and person.is_teacher:
            form = HomeworkForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Homework Created.')
                return redirect('teacher_dashboard')




class SubmitHW(LoginRequiredMixin, View):
    template_name = 'submithw.html'

    def get(self, request, pk):
        homework = Homework.objects.get(id=pk)
        submissions = Submission.objects.filter(hw=homework)
        form = SubmitForm()
        return render(request, self.template_name, {'hw': homework, 'subs': submissions, 'form': form})

    def post(self, request, pk):
        person = Person.objects.get(user=request.user)
        homework = Homework.objects.get(id=pk)
        form = SubmitForm(request.POST)
        if form.is_valid():
            data = dict(form.data)
            print(data)
            Submission.objects.create(
                submitter=person, hw=homework, answer=data['answer'][0], url=data['url'][0], status=False)
            messages.success(request, 'Submitted Successfully')
            return redirect('student_dashboard')


class AdminDashboard(LoginRequiredMixin, View):
    template_name = 'adash.html'

    def get(self, request):
        users = User.objects.all().order_by('-date_joined')
        person = Person.objects.all()
        logger = Person.objects.get(user=request.user)
        if logger and logger.is_admin:
            form = NewStudentForm()
            more = MoreNewStudentForm()
            announcement_form = AnnouncementForm()
            return render(request, self.template_name, {'users': users, 'form': NewStudentForm, 'more': MoreNewStudentForm, 'annform': announcement_form})
        else:
            messages.warning(request, 'You are not authorized to log in as an administrator.')
            return redirect('index')

    def post(self, request):
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement Made Successfully')
            return redirect('admin_dashboard')

class CreatePerson(LoginRequiredMixin, View):
    def post(self, request):
        person = Person.objects.get(user=request.user)
        if person and person.is_admin:
            form = NewStudentForm(request.POST)
            more = MoreNewStudentForm(request.POST)
            for n in User.objects.all():
                if n.username == str(form.data['username'][0]):
                    messages.warning(
                        request, 'A user with that username already exists. Please Try a different username.')
                    return redirect('admin_dashboard')
            if form.is_valid():
                data = dict(form.data)
                more_data = dict(more.data)
                name = str(data['username'][0])
                email = str(data['email'][0])
                phone = str(more_data['phone'][0])
                address = str(more_data['address'][0])
                password = str(data['password1'][0])
                std = str(data['std'][0])
                #this try/except statement can be polished
                try:
                    approval = str(more_data['is_teacher'])
                    User.objects.create_user(name, email, password)
                    print(data['username'], data['email'], data['password1'])
                    made = User.objects.get(username=str(data['username'][0]))
                    make_person = Person.objects.create(
                        user=made, phone=phone, address=address, std=std)
                    make_person.is_teacher = True
                    make_person.std = int(std)
                    make_person.save()
                    messages.warning(request, 'Teacher Created Successfully.')
                    return redirect('admin_dashboard')
                except KeyError:
                    User.objects.create_user(name, email, password)
                    print(data['username'], data['email'], data['password1'])
                    made = User.objects.get(username=str(data['username'][0]))
                    make_person = Person.objects.create(
                        user=made, phone=phone, address=address)
                    make_person.std = int(std)
                    make_person.save()
                    messages.warning(request, 'Student Created Successfully.')
                    return redirect('admin_dashboard')

