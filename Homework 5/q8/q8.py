#q8
def print10_data():
    import psycopg2
    conn = psycopg2.connect(host="localhost", 
                            port="5432", 
                            user="postgres", 
                            password="DataScienceSQL4!", 
                            database="postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees limit 10;")
    for row in cur:
        print(row)
    cur.close()
    conn.close()

print10_data()