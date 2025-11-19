from flask import Blueprint, request, render_template, redirect, url_for, flash
import os
import pandas as pd
from app.file_loader import load_file
from app.ddl_generator import generate_create_table_sql
from app.mysql_ingestor import insert_into_mysql
from app.utils import sanitize_table_name
from dotenv import load_dotenv
import os

main = Blueprint("main", __name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        raw_table_name = request.form.get("table_name", "inferred_table")
        table_name = sanitize_table_name(raw_table_name)

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            df = load_file(file_path)
            ddl = generate_create_table_sql(df, table_name)

            load_dotenv()

            db_config = {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME")
        }


            insert_into_mysql(df, ddl, table_name, db_config)
            flash(f"Table `{table_name}` created and data inserted successfully!", "success")
            return redirect(url_for("main.upload"))

    return render_template("upload.html")