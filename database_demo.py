import psycopg2
#host = 'localhost'

query = "INSERT INTO student (student_id, first_name, last_name, roll_no) " \
          "VALUES (29, 'sushant_1', 'Subedi_1', 23)," \
          "(30, 'nischal_1', 'subedi_1', 24);"

connection = psycopg2.connect(database= 'Python_Database', user = 'postgres',
                              password = '1575', host = 'localhost', port = '5432' )#, password )



# Creating Cursor
cur = connection.cursor()

cur.execute(query)
cur.close()
connection.close()
print("Database Content has been successfully updated")




