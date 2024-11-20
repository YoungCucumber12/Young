import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="12345",
    port=5432,
    dbname="newso"
)
if conn:
    print("Подключено")

    cursor = conn.cursor()
title = input("Введите что нибудь:")
sql = f"INSERT INTO newso(title) VALUES ('{title}')"
cursor.execute(sql)
conn.commit()

delete_query = "DELETE FROM newso(title) WHERE  IN %s"
ids_to_delete = (4)

cursor.execute("SELECT * FROM newso")
result = cursor.fetchall()
print(result)
