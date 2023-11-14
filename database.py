import psycopg2
database = 'Python_Database'
user = 'postgres'
password = '1575'
host = 'localhost'
port = '1575'
sql = """ SELECT * FROM student"""
conn = psycopg2.connect(database, user, host, password, port)
cursor = conn.cursor()

cursor.execute(sql)

conn.commit()

cursor.close()

