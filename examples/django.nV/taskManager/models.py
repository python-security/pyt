#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

import datetime

from django.contrib.auth.models import User

from django.utils import timezone
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.CharField(max_length=3000, default="")
    reset_token = models.CharField(max_length=7, default="")
    reset_token_expiration = models.DateTimeField(default=timezone.now)

class Project(models.Model):
    title = models.CharField(max_length=50, default='Default')
    text = models.CharField(max_length=500)
    start_date = models.DateTimeField('date started')
    due_date = models.DateTimeField(
        'date due',
        default=(
            timezone.now() +
            datetime.timedelta(
                weeks=1)))
    users_assigned = models.ManyToManyField(User)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def was_created_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)

    def is_overdue(self):
        return self.due_date <= timezone.now()

    def percent_complete(self):
        counter = 0
        for task in self.task_set.all():
            counter = counter + (1 if task.completed else 0)
        try:
            return round(float(counter) / self.task_set.count() * 100)
        except ZeroDivisionError:
            return 0


class Task(models.Model):
    project = models.ForeignKey(Project, default=1)
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="N/A")
    start_date = models.DateTimeField('date created')
    due_date = models.DateTimeField(
        'date due',
        default=(
            timezone.now() +
            datetime.timedelta(
                weeks=1)))
    completed = models.NullBooleanField(default=False)
    users_assigned = models.ManyToManyField(User)

    def __str__(self):
        return self.text

    def was_created_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)

    def is_overdue(self):
        return self.due_date <= timezone.now()

    def percent_complete(self):
        return 100 if self.completed else 0


class Notes(models.Model):
    task = models.ForeignKey(Task, default=1)
    title = models.CharField(max_length=200, default="N/A")
    text = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default='ancestor')

    def __str__(self):
        return self.text


class File(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=300, default="")
    path = models.CharField(max_length=3000, default="")

    def __str__(self):
        return self.name
