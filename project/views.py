from django.shortcuts import HttpResponse


def flask_health_check(request):
    return HttpResponse('success')
