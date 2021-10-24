# q7
def dummy_data():
    import psycopg2
    conn = psycopg2.connect(host="localhost", 
                            port="5432", 
                            user="postgres", 
                            password="DataScienceSQL4!", 
                            database="postgres")
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (SELECT generate_series(1,500) as id, substr(md5(random()::text),0,10) AS fname, substr(md5(random()::text),0,10) AS lname);")
    conn.commit()
    cur.close()
    conn.close()

dummy_data()