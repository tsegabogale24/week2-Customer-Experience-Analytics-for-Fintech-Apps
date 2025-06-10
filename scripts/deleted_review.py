import oracledb

# Connect to the database
connection = oracledb.connect(
    user="bank_reviews",
    password="secure_pass",
    dsn="localhost/XEPDB1"
)
cursor = connection.cursor()

try:
    # First delete all reviews (child table)
    cursor.execute("DELETE FROM reviews")
    print(f"Deleted {cursor.rowcount} rows from reviews table")
    
    # Then delete all banks (parent table)
    cursor.execute("DELETE FROM banks")
    print(f"Deleted {cursor.rowcount} rows from banks table")
    
    # Commit the changes
    connection.commit()
    print(" All data successfully deleted")
    
except Exception as e:
    connection.rollback()
    print(f"Error during deletion: {e}")
    
finally:
    cursor.close()
    connection.close()