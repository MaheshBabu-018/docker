import psycopg2, time
time.sleep(5)  # give Postgres a moment on first run
conn = psycopg2.connect(
    host="my-postgres", database="task_db", user="admin", password="secure123"
)
print("Connected to the database!")
conn.close()