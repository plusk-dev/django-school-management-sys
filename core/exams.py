from .models import Exam, Person
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateResultsView(LoginRequiredMixin, View):
    template_name = 'create_results.html'

    def get(self, request, pk):
        person = Person.objects.get(user=request.user)
        if person.is_admin:
            exam = Exam.objects.get(id=pk)
            return render(request, self.template_name)
        else:
            return redirect('index')
        
