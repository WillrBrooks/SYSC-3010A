import urllib.request
import http.client
import json

key = "BKWV1FP1YQA38QHK"
url = "https://api.thingspeak.com/update?api_key="

#"CHANNELS/1160079/feeds.json?results=2"

header = "&results=2"

newurl = url+key+header




print(newurl)

#cannot get this line to work in python3
get_data=urllib.request.get(newurl).json()

channel_id=get_data['channel']['id']

field_1 = get_data['feeds']

list = []

for x in field_1:
	list.append(x['field1'])

print(list)
