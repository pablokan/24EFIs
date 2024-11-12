import sqlite3

conn=sqlite3.connect("ensaladas_base.db")
#conn.execute ("CREATE TABLE personas (id INTEGER PRIMARY KEY,nombre TEXT,cantidad INT,precio INT);")
#conn.execute ("insert into personas (nombre,cantidad) values ('rucula','300');")
#conn.execute ("insert into personas (nombre,cantidad) values ('moza','400');")
conn.commit()
conn.close()