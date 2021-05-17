# Подробнее: https://blog.stroganov.pro/mysql-django-и-кириллические-проблемы

from django.db import connection

cursor = connection.cursor()
cursor.execute('SHOW TABLES')
results=[]

for row in cursor.fetchall():
    results.append(row)

for row in results:
    cursor.execute(f'ALTER TABLE {row[0]} CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;')