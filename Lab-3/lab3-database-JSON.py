from urllib.parse import urlencode
from urllib.request import urlopen
import json
import sqlite3
from sqlite3 import OperationalError

#key provided to use
apiKey = "a808bbf30202728efca23e099a4eecc7"

#Get city to look at
city = input("Enter the name of a city whose weather you would like:\n")

#build URL
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

#get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print("\n", url, "\n")

webData = urlopen(url)
results = webData.read().decode('utf-8')
webData.close()


#results is a JSON string
#print("\n" , results + "\n")


#convert results to a dictionary
data = json.loads(results)

current = data["main"]
degreeSym = chr(176)

#print the data under that "main" label
#print("\n", current, "\n")

print("City: %s" % data["name"])
print("Temperature: %d%sF" %  (current["temp"], degreeSym))
print("Humidity: %d%%" % current["humidity"])
print("Pressure: %d" % current["pressure"])

current = data["wind"]
print("Wind: %d" % current["speed"])


#connect to the database for lab 3
dbconnect = sqlite3.connect("lab3Test.db")

#setup to use the database
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor()

try:
	cursor.execute('''CREATE TABLE weather (city TEXT PRIMARY KEY, temperature NUMERIC, wind NUMERIC);''')
except OperationalError:
	#table already exists continue with script
	print("")


#add the data to the database if the data for this city is not already in there
current = data["main"]
t = current["temp"]

current = data["wind"]

#print('''INSERT OR IGNORE INTO weather values(%s, %d, %d);''' % (data["name"], t, current["speed"]))


cursor.execute('''INSERT OR IGNORE INTO weather values("%s", %d, %d);''' % (data["name"], t, current["speed"]))
dbconnect.commit()


dbconnect.close()
