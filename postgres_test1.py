import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="test1_db",
    user="pos0"
         "tgres",
    password="postgresAK82@"
)
cur = conn.cursor()
cur.execute("SELECT * FROM osoby;")
print(cur.fetchall())

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()

