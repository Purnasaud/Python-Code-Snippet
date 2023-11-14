import psycopg2
query = "CREATE TABLE projects( project_id INT , name VARCHAR(100) NOT NULL, start_date DATE, end_date DATE, PRIMARY KEY(project_id));"

# Creating Connection
connection = psycopg2.connect(database= 'University', user = 'postgres',
                              password = '1575', host = 'localhost', port = '5432' )#, password )

# Creating Cursor
cur = connection.cursor()
cur.execute(query)
cur.close()
print('Your Database Has Been Updatedd Successfully')
connection.close()