from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Person, Answer, Room, Submission
from django.contrib.auth import logout

@login_required
def deleteRoom(request, pk):
    person = Person.objects.get(user=request.user)
    if person.is_teacher:
        room = Room.objects.get(id=pk)
        room.delete()
        messages.success(request, 'Deleted Room')
        return redirect('teacher_dashboard')
    else:
        messages.warning(request, 'You are not authorized to do so.')
        return redirect('index')

@login_required
def deleteAnswer(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()
    messages.success(request, 'Deleted')
    return redirect('student_dashboard')

# at this moment, its 1:26AM and idk why but i don't feel sleepy, ig its cuz i slept in the afternoon but who cares, i gotta do my homework after adding the mark as correct thingy


@login_required
def markCorrect(request, pk):
    user = request.user
    person = Person.objects.get(user=user)
    if person.is_teacher:
        answer = Answer.objects.get(id=pk)
        answer.status = True
        answer.save()
        messages.success(request, 'Marked as correct.')
        return redirect('teacher_dashboard')
    else:
        messages.warning(
            request, 'You are not authorized to mark answers. Multiple attempts may result in legal issues.')
        return redirect('index')


@login_required
def markHWCorrect(request, pk):
    user = request.user
    person = Person.objects.get(user=user)
    if person and person.is_teacher:
        submission = Submission.objects.get(id=pk)
        submission.status = True
        submission.save()
        messages.success(request, 'Marked as Correct')
        return redirect('teacher_dashboard')
    else:
        messages.warning(
            request, 'You are not authorized to mark answers. Multiple attempts may result in legal issues.')
        return redirect('index')


@login_required
def deletePerson(request, pk):
    person = Person.objects.get(user=request.user)
    if person and person.is_admin:
        to_delete = User.objects.get(id=pk)
        to_delete.delete()
        messages.warning(request, 'Deleted Successfully.')
        return redirect('admin_dashboard')
    else:
        messages.warning(
            request, 'You are not authorized to do so. Numerous attempts to do so may result in in legal actions.')
        return redirect('index')


@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Logged Out.')
    return redirect('index')
