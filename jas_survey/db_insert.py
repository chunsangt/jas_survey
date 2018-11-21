import sqlite3

conn = sqlite3.connect('dev-database.sqlite')

print("Opened database successfully")

c = conn.cursor()
c.execute("INSERT INTO SURVEYS (SVID,SVNAME,SVDESC,SVDATE,SVSTATUS,SVSTIME,SVETIME) \
    VALUES ('energy2018','Asia Energy and Utilities Conference 2018','<div><img src=\"/upload/att/2018/asiaenergy/banner.jpg\" /></div>','2018-11-19','Active','2018-11-19 16:00:00','2018-11-19 17:00:00')")
c.execute("INSERT INTO SURVEYS (SVID,SVNAME,SVDESC,SVDATE,SVSTATUS,SVSTIME,SVETIME) \
    VALUES ('koreaconf','UBS Have your say: Korea Conference 2018','<div></div>','2018-11-20','Active','2018-11-20 16:00:00','2018-11-20 17:00:00')")
conn.commit()
print("Records created successfully")
conn.close()
