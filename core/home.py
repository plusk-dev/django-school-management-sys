from django.shortcuts import render, redirect
from django.views import View
from .models import Person
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            person = Person.objects.get(user=request.user)
            if person:
                if person.is_teacher:
                    return redirect('teacher_dashboard')
                elif person.is_admin:
                    return redirect('admin_dashboard')
                elif not person.is_admin and not person.is_teacher:
                    return redirect('student_dashboard')
        else:
            return render(request, self.template_name)

class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)