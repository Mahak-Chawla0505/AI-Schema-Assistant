from app.file_loader import load_file
from app.ddl_generator import generate_create_table_sql
from app.mysql_ingestor import insert_into_mysql
from dotenv import load_dotenv
import os

df = load_file("data/sample.csv")
ddl = generate_create_table_sql(df, "my_table")

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}


insert_into_mysql(df, ddl, "my_table", db_config)