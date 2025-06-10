import oracledb

# === 1. Define your Oracle DB credentials ===
username = "bank_reviews"       # e.g., system
password = "secure_pass"
dsn = "localhost/XE"             # Default XE connection string

# === 2. Read the SQL file ===
import os

base_dir = os.path.dirname(__file__)
sql_path = os.path.join(base_dir, "schema_dump.sql")

with open(sql_path, "r") as file:
    sql_script = file.read()

# === 3. Connect to Oracle DB and execute ===
try:
    with oracledb.connect(user=username, password=password, dsn=dsn) as connection:
        with connection.cursor() as cursor:
            # Split script into individual statements if needed
            for statement in sql_script.split(";"):
                if statement.strip():  # Skip empty lines
                    cursor.execute(statement)
        connection.commit()
        print("SQL dump executed successfully.")
except Exception as e:
    print("Error occurred while executing SQL dump:", e)
