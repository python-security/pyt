from taskManager.misc import store_uploaded_file

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