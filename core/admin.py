from django.contrib import admin
from .models import Person, Question,Homework, Submission, Answer, Room, Announcement
# Register your models here.
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Homework)
admin.site.register(Submission)
admin.site.register(Answer)
admin.site.register(Room)
admin.site.register(Announcement)