from django.shortcuts import render, redirect
from django.views import View
from .models import Person
from .forms import RoomForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class CreateRoom(LoginRequiredMixin, View):
    template_name = 'room.html'

    def get(self, request):
        user = request.user
        person = Person.objects.get(user=user)
        if person and person.is_teacher:
            form = RoomForm()
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('index')

    def post(self, request):
        user = request.user
        person = Person.objects.get(user=user)
        if person and person.is_teacher:
            form = RoomForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Room Created')
                return redirect('teacher_dashboard')
            else:
                messages.warning(
                    request, 'Unable to create room. Please try again.')

#more coming here soon

