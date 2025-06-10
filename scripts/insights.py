import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def analyze_sentiment_by_bank(df):
    """Display sentiment distribution by bank"""
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='app_name', hue='bert_label', palette='coolwarm')
    plt.title("Sentiment by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Review Count")
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()

def analyze_rating_distribution(df):
    """Display rating distribution by bank"""
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='app_name', y='rating', palette='pastel')
    plt.title("Rating Distribution by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.show()

def analyze_theme_frequency(df, top_n=10):
    """Display top N most frequent themes"""
    plt.figure(figsize=(10, 6))
    theme_counts = df['themes'].value_counts().head(top_n)
    theme_counts.plot(kind='bar', color='orange')
    plt.title(f"Top {top_n} Review Themes")
    plt.xlabel("Theme")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analyze_sentiment_trend(df):
    """Display sentiment trend over time (requires date column)"""
    if 'date' not in df.columns:
        print("Warning: 'date' column not found for trend analysis")
        return
    
    df['review_date'] = pd.to_datetime(df['date'], errors='coerce')
    if df['review_date'].isna().all():
        print("Warning: Could not parse dates for trend analysis")
        return
        
    df['month'] = df['review_date'].dt.to_period("M")
    sent_trend = df.groupby(['month', 'bert_label']).size().unstack().fillna(0)
    sent_trend.plot(figsize=(10, 6), marker='o')
    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Reviews")
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()

def generate_keyword_wordcloud(df):
    """Generate word cloud from keywords"""
    if 'top_keywords_x' not in df.columns:
        print("Warning: 'top_keywords_x' column not found for word cloud")
        return
        
    text = ' '.join(df['top_keywords_x'].dropna().astype(str))
    text = text.replace('[', '').replace(']', '').replace("'", '')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Top Keywords Word Cloud")
    plt.show()

def run_all_analyses(df):
    """Run all available analyses"""
    analyze_sentiment_by_bank(df)
    analyze_rating_distribution(df)
    analyze_theme_frequency(df)
    analyze_sentiment_trend(df)
    generate_keyword_wordcloud(df)