import psycopg2

query = 'select * from student'
connection = psycopg2.connect(database='Python_Database', user='postgres', password='1575', host='localhost',
                              port='5432')
cur = connection.cursor()
cur.execute(query)
rows = cur.fetchall()
for i, j, k, l in rows:
    print('Id:', i, 'First_Name: ', j, 'Last_Name: ', k, 'Roll_No : ', l)
print("Database has been successfully retrieved")
cur.close()
connection.close()
