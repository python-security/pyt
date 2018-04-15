from django.shortcuts import render


def xss1(request, param):
    return render(request, 'templates/xss.html', {'param': param})
