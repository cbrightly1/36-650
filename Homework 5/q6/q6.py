# q6
def create_table():
    import psycopg2
    conn = psycopg2.connect(host="localhost", 
                            port="5432", 
                            user="postgres", 
                            password="DataScienceSQL4!", 
                            database="postgres"
                        )
    cur = conn.cursor()
    cur.execute("CREATE TABLE employees (id SERIAL, fname varchar(10), lname varchar(10));")
    conn.commit()
    cur.close()
    conn.close()

create_table()