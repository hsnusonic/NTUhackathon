import json

history = {}
for index in range(1, 65):
    history[index] = {'cntu':[], 'ph':[], 'cl':[]}

with open('data_label.csv', 'r') as f:
    for line in f:
        data = line.split(',')
        if data[0] == "id":
            continue
        index = int(data[0])

        history[index]['cntu'].append( float(data[2]) )
        history[index]['cl'].append( float(data[3]) )
        history[index]['ph'].append( float(data[4]) )

    with open('history.json', 'w') as out:
        json.dump(history, out)


