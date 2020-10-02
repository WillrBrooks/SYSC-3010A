import sqlite3

#connect to database created in part 2
dbconnect = sqlite3.connect("lab3Test.db")

#row_factory = sqlite3.Row so that wew can fetch a column by its name
dbconnect.row_factory = sqlite3.Row;

#create a cursor to work with the database
cursor = dbconnect.cursor();

#using the cursor defined above we can then enter regular sqlite commands to
#be executed

try:
	#create new table in the database
	cursor.execute('''CREATE TABLE lab4 (sensorID NUMERIC PRIMARY KEY, type TEXT, zone TEXT);''')
except:
	print("table already exists.  Continuing with existing table")

#add data to database.  The OR IGNORE prevents a duplicate primary key being entered
cursor.execute('''INSERT OR IGNORE INTO lab4 values(1, "door", "kitchen");''')
cursor.execute('''INSERT OR IGNORE INTO lab4 values(2, "temperature", "kitchen");''')
cursor.execute('''INSERT OR IGNORE INTO lab4 values(3, "door", "garage");''')
cursor.execute('''INSERT OR IGNORE INTO lab4 values(4, "motion", "garage");''')
cursor.execute('''INSERT OR IGNORE INTO lab4 values(5, "temperature", "garage");''')

#commit the change to the database
dbconnect.commit()


print('\nThe sensors that are in the kitchen are:\n')

#to fetch something from the database
cursor.execute('''SELECT * FROM lab4 WHERE zone="kitchen";''')

#to print the fetched data
for row in cursor:
	print(row['sensorID'], "\t", row['type'], "\t", row['zone'])

print('\n\n----------------------------------------\n\n')

print('The door sensors are:\n')


cursor.execute('''SELECT * FROM lab4 WHERE type="door";''')

for row in cursor:
	print(row['sensorID'], "\t", row['type'], "\t", row['zone'])


print('\n')

dbconnect.close()
