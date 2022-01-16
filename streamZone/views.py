from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render


def Homepage(request):
    return HttpResponseRedirect(reverse('App_video:homepage'))

def errorpage(request):
    return render(request, 'errorpage.html')
def handler_not_found(request, exception):
    return render(request, 'errorpage.html')