import urllib.request
import requests
import json

key = 'BKWV1FP1YQA38QHK'

#read channel field
url = 'https://api.thingspeak.com/channels/1160079/fields/1.json?api_key='

#read channel feed
#url = 'https://api.thingspeak.com/channels/1160079/feeds.json?api_key='

#the number of results to be returned
header = '&results=10'

newurl = url+key+header

print(newurl, "\n\n")

get_data = requests.get(newurl).json()

print(get_data, "\n\n")

channel_id=get_data['channel']['id']

field_1 = get_data['feeds']

list = []

for x in field_1:
	list.append(x['field1'])

print(list, "\n\n")
