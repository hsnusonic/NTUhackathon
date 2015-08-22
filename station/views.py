from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Status

import urllib, urllib2, json
import datetime
import os


def update_all():
    url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=190796c8-7c56-42e0-8068-39242b8ec927 "
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
    print "update"
    station_list = [ station for station in data['result']['results']]

    # Update data from Taipei Goverment
    for station in station_list:
        index = int(station["_id"].encode('utf-8'))
        try:
            s = Status.objects.get(index=index)
        except:
            s = Status(index=index)

        s.update_date = station['update_date'].encode('utf-8')
        s.update_time = station['update_time'].encode('utf-8')
        s.qua_id    = str(station["qua_id"].encode('utf-8'))
        s.name      = str(station["code_name"].encode('utf-8'))
        s.longitude = float(station["longitude"].encode('utf-8'))
        s.latitude  = float(station["latitude"].encode('utf-8'))
        s.qua_cntu  = float(station["qua_cntu"].encode('utf-8'))
        s.qua_cl    = float(station["qua_cl"].encode('utf-8'))
        s.qua_ph    = float(station["qua_ph"].encode('utf-8'))

        s.normal    = True 
        s.save()


    # Retrive Score from Azure machine learning
    send_data =  {
        "Inputs": {
            "input1": {
                "ColumnNames": ["id", "code_name", "qua_cntu", "qua_cl", "qua_ph"],
                 "Values": [
                     [ str(status.index), "name", 
                       str(status.qua_cntu), 
                       str(status.qua_cl), 
                       str(status.qua_ph) ] for status in Status.objects.all() 
                 ]
             },        
        },
        "GlobalParameters": {}
    }

    body = str.encode(json.dumps(send_data))

    ml_url = 'https://ussouthcentral.services.azureml.net/workspaces/0d1e347f8a834f018cd92151562305f3/services/75b32010854644098fd1b40215c3dc82/execute?api-version=2.0&details=true'
    api_key = 'Zm2UWiqJcgjohS3HFlL+sTgS1KpoGbD2FAcbS1K4zIt5ZbBZb53WG4yV6gS6Fd4LWGFNL9qpHrNl5XMeU2WArg==' 
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(ml_url, body, headers) 

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
         
        result_json = json.loads(result)


        for each in result_json["Results"]["output1"]["value"]["Values"]:
            index2 = each[0]
            score = each[5]
            #print index2, score
            

    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))                 


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
    s = Status.objects.get(index=status_id)
    content["name"] = s.name
    return render(request, 'station/details.html', content) 

def update(request):
    #update_all()
    return redirect('index')
