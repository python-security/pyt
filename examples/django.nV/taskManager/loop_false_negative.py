import os

from tempfile import NamedTemporaryFile

from django.shortcuts import redirect
from django.http import HttpResponse

def download(request):
    response = HttpResponse("Hi.")
    fork_list = request.POST.getlist('fork_list')
    if request.POST and len(fork_list) > 0:
        tmp_file = NamedTemporaryFile()
        cmd = "tar -czvf %s -C %s " % (tmp_file.name,DOWNLOADS)
        for item in fork_list:
            cmd += item + " "
        os.system(cmd)

        response = HttpResponse(content_type='application/x-gzip')
        response['Content-Disposition'] = 'attachment; filename="%s.tar.gz"' % tmp_file.name
        response.write(tmp_file.file.read())
    else:
        response = redirect("/list/")
    return response
