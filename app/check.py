import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_Password",
    database="ai_schema_db"
)

print("Connected successfully!")

conn.close()
