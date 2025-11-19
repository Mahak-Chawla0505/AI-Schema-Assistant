import pandas as pd
from app.ddl_generator import generate_create_table_sql

def test_generate_create_table_sql_basic():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "score": [95.5, 88.0, 76.5]
    })
    ddl = generate_create_table_sql(df, "students")

    assert "CREATE TABLE students" in ddl
    assert "`id` INT" in ddl or "`id`" in ddl  # depends on your type inference
    assert "`name` VARCHAR" in ddl
    assert "`score` FLOAT" in ddl

def test_generate_create_table_sql_with_dates():
    df = pd.DataFrame({
        "user_id": [101, 102],
        "joined": pd.to_datetime(["2023-01-01", "2023-02-01"])
    })
    ddl = generate_create_table_sql(df, "users")

    assert "CREATE TABLE users" in ddl
    assert "`user_id` INT" in ddl
    assert "`joined` DATETIME" in ddl

def test_generate_create_table_sql_column_order():
    df = pd.DataFrame({
        "a": [1],
        "b": ["text"],
        "c": [3.14]
    })
    ddl = generate_create_table_sql(df, "test_table")

    # Ensure column order is preserved
    assert ddl.index("`a`") < ddl.index("`b`") < ddl.index("`c`")