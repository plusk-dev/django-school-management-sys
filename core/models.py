from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
	phone = models.CharField(default='Not Provided', max_length=20)
	address = models.TextField(default='Not Provided')
	std = models.IntegerField(default=1)
	is_teacher = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

class Question(models.Model):
	title = models.CharField(max_length=256)
	asker = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='questions')
	date = models.DateTimeField(auto_now_add=True)
	std = models.IntegerField()
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title + str(self.asker)

class Homework(models.Model):
	title = models.CharField(max_length=256)
	asker = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='hws')
	date = models.DateTimeField(auto_now_add=True)
	std = models.IntegerField()
	url = models.URLField()
	description = models.TextField(blank=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.title + '|  by  |' + str(self.asker)

class Submission(models.Model):
	submitter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='submissions')
	hw = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='hw_submissions')
	date = models.DateTimeField(auto_now_add=True)
	answer = models.TextField()
	url = models.URLField(blank=True)
	status = models.BooleanField(default=False)
	def __str__(self):
		return self.tile + '| by |' + str(self.submitter)

class Answer(models.Model):
	author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='answers')
	que = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
	answer = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField()

	def __str__(self):
		return self.que + '|  -  |' + str(self.author)

class Room(models.Model):
	title = models.CharField(max_length=69)
	link = models.URLField()
	meeting_id = models.CharField(max_length=256, blank=True)
	password = models.CharField(max_length=256, blank=True)
	std = models.IntegerField()
	to_start = models.CharField(max_length=256, default='Not Provided / May Start Anytime')
	host = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='room')

	def __str__(self):
		return self.title

class Announcement(models.Model):
	title = models.CharField(max_length=256)
	date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	public = models.BooleanField(default=False)
	def __str__(self):
		return self.title