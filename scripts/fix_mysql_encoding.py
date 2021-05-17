#! /usr/bin/env python
import MySQLdb

host = 'localhost'
password = '0905'
username = 'ceaser'
dbname = 'csrweb'

db = MySQLdb.connect(host=host, user=username, passwd=password, db=dbname)
cursor = db.cursor()

cursor.execute(f"ALTER DATABASE `{dbname}` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'")

cursor.execute(f"SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '{dbname}'")

for row in cursor.fetchall():
  cursor.execute(f"ALTER TABLE `{row[0]}` convert to character set DEFAULT COLLATE DEFAULT")
  
db.close()