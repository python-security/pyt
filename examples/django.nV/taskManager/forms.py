#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#           INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

""" forms.py contains various Django forms for the application """

from taskManager.models import Project, Task
from django import forms
from django.contrib.auth.models import User


def get_my_choices_users():
    """ Retrieves a list of all users in the system
        for the user management page
    """

    user_list = User.objects.order_by('date_joined')
    user_tuple = []
    counter = 1
    for user in user_list:
        user_tuple.append((counter, user))
        counter = counter + 1
    return user_tuple


def get_my_choices_tasks(current_proj):
    """ Retrieves all tasks in the system
        for the task management page
    """

    task_list = []
    tasks = Task.objects.all()
    for task in tasks:
        if task.project == current_proj:
            task_list.append(task)

    task_tuple = []
    counter = 1
    for task in task_list:
        task_tuple.append((counter, task))
        counter = counter + 1
    return task_tuple


def get_my_choices_projects():
    """ Retrieves all projects in the system
        for the project management page
    """

    proj_list = Project.objects.all()
    proj_tuple = []
    counter = 1
    for proj in proj_list:
        proj_tuple.append((counter, proj))
        counter = counter + 1
    return proj_tuple

# A2: Broken Authentication and Session Management


class UserForm(forms.ModelForm):
    """ User registration form """
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_active']


class ProjectFileForm(forms.Form):
    """ Used for uploading files attached to projects """
    name = forms.CharField(max_length=300)
    file = forms.FileField()


class ProfileForm(forms.Form):
    """ Provides a form for editing your own profile """
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=300, required=False)
    picture = forms.FileField(required=False)
