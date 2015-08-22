from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Status

import urllib, json
import datetime
import os


def update_all():
    url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=190796c8-7c56-42e0-8068-39242b8ec927 "
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    station_list = [ station for station in data['result']['results']]

    for station in station_list:
        index = int(station["_id"].encode('utf-8'))
        try:
            s = Status.objects.get(index=index)
        except:
            s = Status(index=index)

        s.update_date = station['update_date'].encode('utf-8')
        s.update_time = station['update_time'].encode('utf-8')
        s.qua_id    = station["qua_id"].encode('utf-8')
        s.name      = station["code_name"].encode('utf-8')
        s.longitude = float(station["longitude"].encode('utf-8'))
        s.latitude  = float(station["latitude"].encode('utf-8'))
        s.qua_cntu  = float(station["qua_cntu"].encode('utf-8'))
        s.qua_cl    = float(station["qua_cl"].encode('utf-8'))
        s.qua_ph    = float(station["qua_ph"].encode('utf-8'))
        s.save()

# Create your views here.
def index(request):
    update_all()
    status_list = Status.objects.all()
    context = {'status_list': status_list}
    return render(request, 'station/index.html', context)

def detail(request, status_id):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'history.json')
    content = {}
    with open(file_path, 'r') as f:
        data = json.load(f)
        cntu = data[status_id]["cntu"]
        ph   = data[status_id]["ph"]
        cl   = data[status_id]["cl"]
        content["cntu"] = cntu
        content["ph"] = ph
        content["cl"] = cl
    return render(request, 'station/details.html', content) 

def update(request):
    update_all()
    return redirect('index')
