from django.shortcuts import render, render_to_response, redirect


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