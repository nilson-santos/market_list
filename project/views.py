from django.shortcuts import HttpResponse


def django_health_check(request):
    return HttpResponse('success')
