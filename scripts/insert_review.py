import oracledb
import pandas as pd
import os
from datetime import datetime

# === Step 1: Read CSV from parent data/ folder ===
csv_path = os.path.join(os.path.dirname(__file__), "../data/final_themed_data.csv")
df = pd.read_csv(csv_path)

# Preview data (optional)
print(df.head())

# === Step 2: Connect to Oracle DB ===
connection = oracledb.connect(
    user="bank_reviews",
    password="secure_pass",        # 🔒 Tip: Use env var in real projects
    dsn="localhost/XEPDB1"
)
cursor = connection.cursor()

# === Step 3: Insert Banks ===
banks = df['app_name'].unique()
bank_id_map = {}

for bank_name in banks:
    # Create a variable to hold the returned bank_id
    bank_id_var = cursor.var(int)
    
    cursor.execute("""
        INSERT INTO banks (bank_name)
        VALUES (:bank_name)
        RETURNING bank_id INTO :bank_id
    """, {
        "bank_name": bank_name,
        "bank_id": bank_id_var
    })
    
    # Get the bank_id from the variable
    bank_id = bank_id_var.getvalue()
    bank_id_map[bank_name] = bank_id

# === Step 4: Insert Reviews ===
for _, row in df.iterrows():
    try:
        # Convert list data to strings
        top_keywords = convert_list_data(row.get('top_keywords_x', ''))
        theme = convert_list_data(row.get('themes', ''))
        
        # Handle date conversion
        date_str = row['date']
        if isinstance(date_str, str):
            date_str = datetime.strptime(date_str.split()[0], "%Y-%m-%d").date()
        
        cursor.execute("""
            INSERT INTO reviews (
                bank_id, review_text, rating, review_date,
                sentiment_score, sentiment_label, cleaned_text,
                top_keywords, theme
            ) VALUES (
                :bank_id, :review_text, :rating, :review_date,
                :sentiment_score, :sentiment_label, :cleaned_text,
                :top_keywords, :theme
            )
        """, {
            "bank_id": bank_id_map[row['app_name']],
            "review_text": row['review_text'],
            "rating": row['rating'],
            "review_date": date_str,
            "sentiment_score": row['bert_score'],
            "sentiment_label": row['bert_label'],
            "cleaned_text": row['cleaned_text'],
            "top_keywords": top_keywords,
            "theme": theme
        })
    except Exception as e:
        print(f"Failed to insert row: {e}")
        print("Problem row:", row)
        continue

# === Step 5: Finalize ===
connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted into Oracle.")