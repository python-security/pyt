"""From django.nV, views.py"""

name = request.POST.get('name', False)
upload_path = store_uploaded_file(name, request.FILES['file'])

#A1 - Injection (SQLi)
curs = connection.cursor()
curs.execute(
    "insert into taskManager_file ('name','path','project_id') values ('%s','%s',%s)" %
    (name, upload_path, project_id))