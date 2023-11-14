import psycopg2
query1='SELECT first_name, SUM(roll_no) as Total from student GROUP BY first_name'
#query  = 'select student_id, first_name from student'
connection = psycopg2.connect(database= 'Python_Database', user = 'postgres',
                              password = '1575', host = 'localhost', port = '5432' )

cur = connection.cursor()
cur.execute(query1)

rows = cur.fetchall()
print(rows)
for i, j in rows:
   # if i == 26:
        print('Province Name ', i, 'Total_Roll no', j)
    #print('Id:', i, 'First_Name: ', j, 'Last_Name: ', k, 'Roll_No : ', l)
print("Database has been successfully retrived")
cur.close()
connection.close()