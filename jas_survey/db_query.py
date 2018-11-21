import sqlite3

conn = sqlite3.connect('dev-database.sqlite')

print("Opened database successfully")

c = conn.cursor()
cursor = c.execute("SELECT * FROM SURVEYS")
for row in cursor:
	print("SVID = ", row[0])
	print("SVNAME = ", row[1])
	print("SVDESC = ", row[2])
	print("SVDATE = ", row[3])
	print("SVSTATUS = ", row[4])
	print("SVSTIME = ", row[5])
	print("SVETIME = ", row[6], "\n")
	
print("Operation done successfully")