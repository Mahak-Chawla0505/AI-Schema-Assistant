import mysql.connector

def insert_into_mysql(df, ddl, table_name, db_config):
    ddl = ddl.replace(f"CREATE TABLE {table_name}", f"CREATE TABLE `{table_name}`")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")
    cursor.execute(ddl)

    cols = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_sql = f"INSERT INTO `{table_name}` ({cols}) VALUES ({placeholders})"

    data = [tuple(row) for row in df.itertuples(index=False)]
    cursor.executemany(insert_sql, data)
    conn.commit()
    cursor.close()
    conn.close()

    
