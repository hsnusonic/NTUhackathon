from django.shortcuts import render
from django.http import HttpResponse

from .models import Status

# Create your views here.
def index(request):
    status_list = Status.objects.all()
    context = {'status_list': status_list}
    return render(request, 'station/index.html', context)

def detail(request, status_id):
    return HttpResponse("Status number %s" % status_id)


