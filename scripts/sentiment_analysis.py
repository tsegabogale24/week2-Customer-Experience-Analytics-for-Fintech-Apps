from transformers import pipeline
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

def apply_sentiment_analysis(df, text_column="review_text"):
    # Load models
    sentiment_pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    sia = SentimentIntensityAnalyzer()
    
    # DistilBERT (Transformers)
    bert_results = sentiment_pipe(df[text_column].tolist(), truncation=True)
    df["bert_label"] = [res['label'].lower() for res in bert_results]  #
    df["bert_score"] = [res['score'] for res in bert_results]
    
    # VADER
    df["vader_score"] = df[text_column].apply(lambda x: sia.polarity_scores(x)["compound"])
    df["vader_label"] = df["vader_score"].apply(lambda x: "positive" if x > 0.05 else "negative" if x < -0.05 else "neutral")
    
    # TextBlob
    df["textblob_score"] = df[text_column].apply(lambda x: TextBlob(x).sentiment.polarity)
    df["textblob_label"] = df["textblob_score"].apply(lambda x: "positive" if x > 0.1 else "negative" if x < -0.1 else "neutral")

    return df
