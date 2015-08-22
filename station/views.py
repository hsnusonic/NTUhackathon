from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Status

import urllib, json

# Create your views here.
def index(request):
    status_list = Status.objects.all()
    context = {'status_list': status_list}
    return render(request, 'station/index.html', context)

def detail(request, status_id):
    return HttpResponse("Status number %s" % status_id)

def update(request):
    url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=190796c8-7c56-42e0-8068-39242b8ec927 "
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    station_list = [ station for station in data['result']['results']]

    # Remove all previous data
    for station in Status.objects.all():
        station.delete()

    # Save the new one
    for station in station_list:
        s = Status(
            update_date = station["update_date"].encode('utf-8'),
            update_time = station["update_time"].encode('utf-8'),
            qua_id    = station["qua_id"].encode('utf-8'),
            name      = station["code_name"].encode('utf-8'),
            longitude = station["longitude"].encode('utf-8'),
            latitude  = station["latitude"].encode('utf-8'),
            qua_cntu  = station["qua_cntu"].encode('utf-8'),
            qua_cl    = station["qua_cl"].encode('utf-8'),
            qua_ph    = station["qua_ph"].encode('utf-8')
        )
        s.save()
    return redirect('index')
