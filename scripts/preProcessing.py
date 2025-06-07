import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data_issues(df):
    """
    Visualize missing values and check for duplicate entries.
    """
    print("🔍 Checking for Duplicates:")
    print(f"→ Total Duplicates: {df.duplicated().sum()}")

    print("\n📊 Visualizing Missing Data:")
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.isnull(), cbar=False, cmap="YlOrRd")
    plt.title("Missing Values Heatmap")
    plt.show()


def clean_reviews_data(df):
    """
    Handle preprocessing: remove duplicates, handle missing data, normalize date format.
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows with missing review text or rating
    df = df.dropna(subset=["review_text", "rating"])

    # Normalize date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df = df.dropna(subset=["date"])

    return df.reset_index(drop=True)
import re

def clean_review_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
    return text

def preprocess_text_column(df, column="review_text"):
    df[column] = df[column].astype(str).apply(clean_review_text)
    return df
def plot_ratings_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='rating', palette='viridis')
    plt.title('⭐ Ratings Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Number of Reviews')
    plt.show()