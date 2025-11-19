from app.type_inferer import infer_column_type

def generate_create_table_sql(df, table_name):
    ddl = f"CREATE TABLE {table_name} (\n"
    for col in df.columns:
        col_type = infer_column_type(df[col])
        ddl += f"  `{col}` {col_type},\n"
    ddl = ddl.rstrip(",\n") + "\n);"
    return ddl