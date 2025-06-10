# scripts/keyword_extraction.py
import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

def extract_keywords(df, text_column="review_text", top_n=5):
    df["cleaned_text"] = df[text_column].apply(preprocess_text)
    vectorizer = TfidfVectorizer(max_df=0.9, min_df=2, ngram_range=(1, 2), stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["cleaned_text"])
    keywords = vectorizer.get_feature_names_out()
    
    top_keywords = []
    for row in tfidf_matrix:
        row_array = row.toarray().flatten()
        top_indices = row_array.argsort()[-top_n:][::-1]
        top_keywords.append([keywords[i] for i in top_indices])
    
    df["top_keywords"] = top_keywords
    print(vectorizer.get_feature_names_out()[:50])  # sample
    return df[["review_text", "cleaned_text", "top_keywords" , "app_name" , "rating"]]
def group_keywords_by_similarity(df, keyword_column="top_keywords"):
    theme_labels = [
        "Account Access Issues",
        "Transaction Performance",
        "User Interface & Experience",
        "Customer Support & Satisfaction",
        "Feature Requests & App Enhancements"
    ]
    
    theme_docs = {label: nlp(label.lower()) for label in theme_labels}
    df = df.copy()  # 🛡️ Prevents the SettingWithCopyWarning

    def assign_similar_theme(keywords):
        theme_scores = {label: 0.0 for label in theme_labels}
        for kw in keywords:
            kw_doc = nlp(kw)
            for label, theme_doc in theme_docs.items():
                sim = kw_doc.similarity(theme_doc)
                theme_scores[label] += sim
        sorted_themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)
        top_themes = [sorted_themes[0][0]]
        if sorted_themes[1][1] > 0.7:
            top_themes.append(sorted_themes[1][0])
        return top_themes

    df["themes"] = df[keyword_column].apply(assign_similar_theme)
    return df[["review_text", "top_keywords", "themes"]]
