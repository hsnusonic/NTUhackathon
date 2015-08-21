import time
import sched
import urllib, json
from threading import Timer

url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=190796c8-7c56-42e0-8068-39242b8ec927 "
f = open('data', 'w+')
schedule = sched.scheduler( time.time, time.sleep )

def get_data():
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    f.write(str(data))
    f.write("\n")

while (True):
    #schedule.enter(5, 0, get_data, ())
    get_data()
    time.sleep(15)


get_data()
print "done"



