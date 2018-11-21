import sqlite3

conn = sqlite3.connect('dev-database.sqlite')

print("Opened database successfully")

c = conn.cursor()
c.execute('''CREATE TABLE SURVEYS 
    (SVID TEXT PRIMARY KEY NOT NULL,
	SVNAME TEXT NOT NULL,
	SVDESC TEXT,
	SVDATE timestamp,
	SVSTATUS TEXT,
	SVSTIME timestamp,
	SVETIME timestamp);''')
conn.commit();
print("Table SURVEYS created successfully")
conn.close();




