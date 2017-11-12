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
import mimetypes
import os
import codecs

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext
from django.db import connection

from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import Group, User
from django.contrib.auth import logout

from taskManager.models import Task, Project, Notes, File, UserProfile
from taskManager.misc import store_uploaded_file
from taskManager.forms import UserForm, ProjectFileForm, ProfileForm


def manage_tasks(request, project_id):

    user = request.user
    proj = Project.objects.get(pk=project_id)

    if user.is_authenticated():

        if user.has_perm('can_change_task'):

            if request.method == 'POST':

                userid = request.POST.get("userid")
                taskid = request.POST.get("taskid")

                user = User.objects.get(pk=userid)
                task = Task.objects.get(pk=taskid)

                task.users_assigned.add(user)

                return redirect('/taskManager/')
            else:
                return render_to_response(
                    'taskManager/manage_tasks.html',
                    {
                        'tasks': Task.objects.filter(
                            project=proj).order_by('title'),
                        'users': User.objects.order_by('date_joined')},
                    RequestContext(request))

        else:
            return redirect('/taskManager/', {'permission': False})

    return redirect('/taskManager/', {'logged_in': False})


def manage_projects(request):

    user = request.user

    if user.is_authenticated():
        logged_in = True

        if user.has_perm('can_change_group'):

            if request.method == 'POST':

                userid = request.POST.get("userid")
                projectid = request.POST.get("projectid")

                user = User.objects.get(pk=userid)
                project = Project.objects.get(pk=projectid)

                project.users_assigned.add(user)

                return redirect('/taskManager/')
            else:

                return render_to_response(
                    'taskManager/manage_projects.html',
                    {
                        'projects': Project.objects.order_by('title'),
                        'users': User.objects.order_by('date_joined'),
                        'logged_in': logged_in},
                    RequestContext(request))

        else:
            return redirect('/taskManager/', {'permission': False})

    return redirect('/taskManager/', {'logged_in': False})

# A7 - Missing Function Level Access Control


def manage_groups(request):

    user = request.user

    if user.is_authenticated():

        user_list = User.objects.order_by('date_joined')

        if request.method == 'POST':

            post_data = request.POST.dict()

            accesslevel = post_data["accesslevel"].strip()

            if accesslevel in ['admin_g', 'project_managers', 'team_member']:

                # Create the group if it doesn't already exist
                try:
                    grp = Group.objects.get(name=accesslevel)
                except Group.DoesNotExist:
                    grp = Group.objects.create(name=accesslevel)
                specified_user = User.objects.get(pk=post_data["userid"])
                # Check if the user even exists
                if specified_user is None:
                    return redirect('/taskManager/', {'permission': False})
                specified_user.groups.add(grp)
                specified_user.save()
                return render_to_response(
                    'taskManager/manage_groups.html',
                    {
                        'users': user_list,
                        'groups_changed': True,
                        'logged_in': True},
                    RequestContext(request))
            else:
                return render_to_response(
                    'taskManager/manage_groups.html',
                    {
                        'users': user_list,
                        'logged_in': True},
                    RequestContext(request))

        else:
            if user.has_perm('can_change_group'):
                return render_to_response(
                    'taskManager/manage_groups.html',
                    {
                        'users': user_list,
                        'logged_in': True},
                    RequestContext(request))
            else:
                return redirect('/taskManager/', {'permission': False})

    return redirect('/taskManager/', {'logged_in': False})

# A4: Insecure Direct Object Reference (IDOR)


def upload(request, project_id):

    if request.method == 'POST':

        proj = Project.objects.get(pk=project_id)
        form = ProjectFileForm(request.POST, request.FILES)

        if form.is_valid():
            name = request.POST.get('name', False)
            upload_path = store_uploaded_file(name, request.FILES['file'])

            #A1 - Injection (SQLi)
            curs = connection.cursor()
            curs.execute(
                "insert into taskManager_file ('name','path','project_id') values ('%s','%s',%s)" %
                (name, upload_path, project_id))

            return redirect('/taskManager/' + project_id +
                            '/', {'new_file_added': True})
        else:
            form = ProjectFileForm()
    else:
        form = ProjectFileForm()
    return render_to_response(
        'taskManager/upload.html', {'form': form}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def download(request, file_id):

    file = File.objects.get(pk=file_id)
    abspath = open(
        os.path.dirname(
            os.path.realpath(__file__)) +
        file.path,
        'rb')
    response = HttpResponse(content=abspath.read())
    response['Content-Type'] = mimetypes.guess_type(file.path)[0]
    response['Content-Disposition'] = 'attachment; filename=%s' % file.name
    return response


def download_profile_pic(request, user_id):

    user = User.objects.get(pk=user_id)
    filepath = user.userprofile.image
    if len(filepath) > 1:
        return redirect(filepath)
    else:
        return redirect('/static/taskManager/uploads/default.png')
    #filename = user.get_full_name()+"."+filepath.split(".")[-1]
    # try:
    #	abspath = open(filepath, 'rb')
    # except:
    #	abspath = open("./taskmanager"+filepath, 'rb')
    #response = HttpResponse(content=abspath.read())
    #response['Content-Type']= mimetypes.guess_type(filepath)[0]
    # return response

# A4: Insecure Direct Object Reference (IDOR)


def task_create(request, project_id):

    if request.method == 'POST':

        proj = Project.objects.get(pk=project_id)

        text = request.POST.get('text', False)
        task_title = request.POST.get('task_title', False)
        now = timezone.now()
        task_duedate = timezone.now() + datetime.timedelta(weeks=1)
        if request.POST.get('task_duedate') != '':
            task_duedate = datetime.datetime.fromtimestamp(
                int(request.POST.get('task_duedate', False)))

        task = Task(
            text=text,
            title=task_title,
            start_date=now,
            due_date=task_duedate,
            project=proj)

        task.save()
        task.users_assigned = [request.user]

        return redirect('/taskManager/' + project_id +
                        '/', {'new_task_added': True})
    else:
        return render_to_response(
            'taskManager/task_create.html', {'proj_id': project_id}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def task_edit(request, project_id, task_id):

    proj = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':

        if task.project == proj:

            text = request.POST.get('text', False)
            task_title = request.POST.get('task_title', False)
            task_completed = request.POST.get('task_completed', False)

            task.title = task_title
            task.text = text
            task.completed = True if task_completed == "1" else False
            task.save()

        return redirect('/taskManager/' + project_id + '/' + task_id)
    else:
        return render_to_response(
            'taskManager/task_edit.html', {'task': task}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def task_delete(request, project_id, task_id):
    proj = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)
    if proj is not None:
        if task is not None and task.project == proj:
            task.delete()

    return redirect('/taskManager/' + project_id + '/')

# A4: Insecure Direct Object Reference (IDOR)


def task_complete(request, project_id, task_id):
    proj = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)
    if proj is not None:
        if task is not None and task.project == proj:
            task.completed = not task.completed
            task.save()

    return redirect('/taskManager/' + project_id)


def project_create(request):

    if request.method == 'POST':

        title = request.POST.get('title', False)
        text = request.POST.get('text', False)
        project_priority = int(request.POST.get('project_priority', False))
        now = timezone.now()
        project_duedate = timezone.make_aware(datetime.datetime.fromtimestamp(
            int(request.POST.get('project_duedate', False))))

        project = Project(title=title,
                          text=text,
                          priority=project_priority,
                          due_date=project_duedate,
                          start_date=now)
        project.save()
        project.users_assigned = [request.user.id]

        return redirect('/taskManager/', {'new_project_added': True})
    else:
        return render_to_response(
            'taskManager/project_create.html',
            {},
            RequestContext(request))


# A4: Insecure Direct Object Reference (IDOR)
def project_edit(request, project_id):

    proj = Project.objects.get(pk=project_id)

    if request.method == 'POST':

        title = request.POST.get('title', False)
        text = request.POST.get('text', False)
        project_priority = int(request.POST.get('project_priority', False))
        project_duedate = datetime.datetime.fromtimestamp(
            int(request.POST.get('project_duedate', False)))

        proj.title = title
        proj.text = text
        proj.priority = project_priority
        proj.due_date = project_duedate
        proj.save()

        return redirect('/taskManager/' + project_id + '/')
    else:
        return render_to_response(
            'taskManager/project_edit.html', {'proj': proj}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def project_delete(request, project_id):
    # IDOR
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('/taskManager/dashboard')

# A10: Open Redirect


def logout_view(request):
    logout(request)
    return redirect(request.GET.get('redirect', '/taskManager/'))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Redirect to a success page.
                    return redirect('/taskManager/')
                else:
                    # Return a 'disabled account' error message
                    return redirect('/taskManager/', {'disabled_user': True})
            else:
                # Return an 'invalid login' error message.
                return render(request,
                              'taskManager/login.html',
                              {'failed_login': False})
        else:
            return render(request,
                          'taskManager/login.html',
                          {'invalid_username': False})
    else:
        return render_to_response(
            'taskManager/login.html',
            {},
            RequestContext(request))


def register(request):

    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)

            # add user to lowest permission group

            #grp = Group.objects.get(name='team_member')
            # user.groups.add(grp)

            user.userProfile = UserProfile.objects.create(user=user)
            user.userProfile.save()
            user.save()

            # Update our variable to tell the template registration was
            # successful.
            registered = True

        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'taskManager/register.html',
        {'user_form': user_form, 'registered': registered},
        context)


def index(request):
    sorted_projects = Project.objects.order_by('-start_date')

    admin_level = False

    if request.user.groups.filter(name='admin_g').exists():
        admin_level = True

    list_to_show = []
    for project in sorted_projects:
        if(project.users_assigned.filter(username=request.user.username)).exists():
            list_to_show.append(project)

    if request.user.is_authenticated():
        return redirect("/taskManager/dashboard")
    else:
        return render(
            request,
            'taskManager/index.html',
            {'project_list': sorted_projects,
             'user': request.user,
             'admin_level': admin_level}
        )


def profile_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect("/taskManager/dashboard")

    if request.user.groups.filter(name='admin_g').exists():
        role = "Admin"
    elif request.user.groups.filter(name='project_managers').exists():
        role = "Project Manager"
    else:
        role = "Team Member"

    sorted_projects = Project.objects.filter(
        users_assigned=request.user.id).order_by('title')

    return render(request, 'taskManager/profile_view.html',
                  {'user': user, 'role': role, 'project_list': sorted_projects})


def project_details(request, project_id):
    proj = Project.objects.filter(
        users_assigned=request.user.id,
        pk=project_id)
    if not proj:
        messages.warning(
            request,
            'You are not authorized to view this project')
        return redirect('/taskManager/dashboard')
    else:
        proj = Project.objects.get(pk=project_id)
        user_can_edit = request.user.has_perm('project_edit')

        return render(request, 'taskManager/project_details.html',
                      {'proj': proj, 'user_can_edit': user_can_edit})

# A4: Insecure Direct Object Reference (IDOR)


def note_create(request, project_id, task_id):
    if request.method == 'POST':

        parent_task = Task.objects.get(pk=task_id)

        note_title = request.POST.get('note_title', False)
        text = request.POST.get('text', False)

        note = Notes(
            title=note_title,
            text=text,
            user=request.user,
            task=parent_task)

        note.save()
        return redirect('/taskManager/' + project_id + '/' +
                        task_id, {'new_note_added': True})
    else:
        return render_to_response(
            'taskManager/note_create.html', {'task_id': task_id}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def note_edit(request, project_id, task_id, note_id):

    proj = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)
    note = Notes.objects.get(pk=note_id)

    if request.method == 'POST':

        if task.project == proj:

            if note.task == task:

                text = request.POST.get('text', False)
                note_title = request.POST.get('note_title', False)

                note.title = note_title
                note.text = text
                note.save()

        return redirect('/taskManager/' + project_id + '/' + task_id)
    else:
        return render_to_response(
            'taskManager/note_edit.html', {'note': note}, RequestContext(request))

# A4: Insecure Direct Object Reference (IDOR)


def note_delete(request, project_id, task_id, note_id):
    proj = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)
    note = Notes.objects.get(pk=note_id)
    if proj is not None:
        if task is not None and task.project == proj:
            if note is not None and note.task == task:
                note.delete()

    return redirect('/taskManager/' + project_id + '/' + task_id)


def task_details(request, project_id, task_id):

    task = Task.objects.get(pk=task_id)

    logged_in = True

    if not request.user.is_authenticated():
        logged_in = False

    admin_level = False
    if request.user.groups.filter(name='admin_g').exists():
        admin_level = True

    pmanager_level = False
    if request.user.groups.filter(name='project_managers').exists():
        pmanager_level = True

    assigned_to = False
    if task.users_assigned.filter(username=request.user.username).exists():
        assigned_to = True
    elif admin_level:
        assigned_to = True
    elif pmanager_level:
        project_users = task.project.users_assigned
        if project_users.filter(username=request.user.username).exists():
            assigned_to = True

    return render(request,
                  'taskManager/task_details.html',
                  {'task': task,
                   'assigned_to': assigned_to,
                   'logged_in': logged_in,
                   'completed_task': "Yes" if task.completed else "No"})


def dashboard(request):
    sorted_projects = Project.objects.filter(
        users_assigned=request.user.id).order_by('title')
    sorted_tasks = Task.objects.filter(
        users_assigned=request.user.id).order_by('title')
    return render(request,
                  'taskManager/dashboard.html',
                  {'project_list': sorted_projects,
                   'user': request.user,
                   'task_list': sorted_tasks})


def project_list(request):
    sorted_projects = Project.objects.filter(
        users_assigned=request.user.id).order_by('title')
    user_can_edit = request.user.has_perm('project_edit')
    user_can_delete = request.user.has_perm('project_delete')
    user_can_add = request.user.has_perm('project_add')
    return render(request,
                  'taskManager/project_list.html',
                  {'project_list': sorted_projects,
                   'user': request.user,
                   'user_can_edit': user_can_edit,
                   'user_can_delete': user_can_delete,
                   'user_can_add': user_can_add})


def task_list(request):
    my_task_list = Task.objects.filter(users_assigned=request.user.id)
    return render(request, 'taskManager/task_list.html',
                  {'task_list': my_task_list, 'user': request.user})


def search(request):
    query = request.GET.get('q', '')

    my_project_list = Project.objects.filter(
        users_assigned=request.user.id).filter(
            title__icontains=query).order_by('title')
    my_task_list = Task.objects.filter(
        users_assigned=request.user.id).filter(
            title__icontains=query).order_by('title')
    return render(request,
                  'taskManager/search.html',
                  {'q': query,
                   'task_list': my_task_list,
                   'project_list': my_project_list,
                   'user': request.user})


def tutorials(request):
    return render(request,
                  'taskManager/tutorials.html',
                  {'user': request.user})


def show_tutorial(request, vuln_id):
    if vuln_id in [
            "injection",
            "brokenauth",
            "xss",
            "idor",
            "misconfig",
            "exposure",
            "access",
            "csrf",
            "components",
            "redirects"]:
        return render(request, 'taskManager/tutorials/' + vuln_id + '.html')
    else:
        return render(request,
                      'taskManager/tutorials.html',
                      {'user': request.user})


def profile(request):
    return render(request, 'taskManager/profile.html', {'user': request.user})

# A4: Insecure Direct Object Reference (IDOR)
# A8: Cross Site Request Forgery (CSRF)


@csrf_exempt
def profile_by_id(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print("made it!")
            if request.POST.get('username') != user.username:
                user.username = request.POST.get('username')
            if request.POST.get('first_name') != user.first_name:
                user.first_name = request.POST.get('first_name')
            if request.POST.get('last_name') != user.last_name:
                user.last_name = request.POST.get('last_name')
            if request.POST.get('email') != user.email:
                user.email = request.POST.get('email')
            if request.POST.get('password'):
                user.set_password(request.POST.get('password'))
            if request.FILES:
                user.userprofile.image = store_uploaded_file(user.username
                + "." + request.FILES['picture'].name.split(".")[-1], request.FILES['picture'])
                user.userprofile.save()
            user.save()
            messages.info(request, "User Updated")

    return render(request, 'taskManager/profile.html', {'user': user})

# A8: Cross Site Request Forgery (CSRF)

@csrf_exempt
def reset_password(request):

    if request.method == 'POST':

        reset_token = request.POST.get('reset_token')

        try:
            userprofile = UserProfile.objects.get(reset_token = reset_token)
            if timezone.now() > userprofile.reset_token_expiration:
                # Reset the token and move on
                userprofile.reset_token_expiration = timezone.now()
                userprofile.reset_token = ''
                userprofile.save()
                return redirect('/taskManager/')

        except UserProfile.DoesNotExist:
            messages.warning(request, 'Invalid password reset token')
            return render(request, 'taskManager/reset_password.html')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password != confirm_password:
            messages.warning(request, 'Passwords do not match')
            return render(request, 'taskManager/reset_password.html')

        # Reset the user's password + remove the tokens
        userprofile.user.set_password(new_password)
        userprofile.reset_token = ''
        userprofile.reset_token_expiration = timezone.now()
        userprofile.user.save()
        userprofile.save()

        messages.success(request, 'Password has been successfully reset')
        return redirect('/taskManager/login')

    return render(request, 'taskManager/reset_password.html')

# Vuln: Username Enumeration

@csrf_exempt
def forgot_password(request):

    if request.method == 'POST':
        t_email = request.POST.get('email')

        try:
            reset_user = User.objects.get(email=t_email)

            # Generate secure random 6 digit number
            res = ""
            nums = [x for x in os.urandom(6)]
            for x in nums:
                res = res + str(x)

            reset_token = res[:6]
            reset_user.userprofile.reset_token = reset_token
            reset_user.userprofile.reset_token_expiration = timezone.now() + datetime.timedelta(minutes=10)
            reset_user.userprofile.save()
            reset_user.save()

            reset_user.email_user(
                "Reset your password",
                "You can reset your password at /taskManager/reset_password/. Use \"{}\" as your token. This link will only work for 10 minutes.".format(reset_token))

            messages.success(request, 'Check your email for a reset token')
            return redirect('/taskManager/reset_password')
        except User.DoesNotExist:
            messages.warning(request, 'Check your email for a reset token')

    return render(request, 'taskManager/forgot_password.html')

# A8: Cross Site Request Forgery (CSRF)

@csrf_exempt
def change_password(request):

    if request.method == 'POST':
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if authenticate(username=user.username, password=old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password Updated')
            else:
                messages.warning(request, 'Passwords do not match')
        else:
            messages.warning(request, 'Invalid Password')

    return render(request,
                  'taskManager/change_password.html',
                  {'user': request.user})


def tm_settings(request):
    settings_list = request.META
    return render(request,
                  'taskManager/settings.html',
                  {'settings': settings_list})
