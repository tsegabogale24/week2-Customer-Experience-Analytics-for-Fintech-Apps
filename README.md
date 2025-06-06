# 📊 Customer Experience Analytics for Fintech Apps

This project analyzes user reviews from the Google Play Store for three major Ethiopian mobile banking applications. The goal is to extract insights about customer satisfaction using sentiment analysis, visualizations, and natural language processing (NLP) techniques.

---

## 🚀 Objective

To simulate the role of a Data Analyst at Omega Consultancy by:

- Scraping user reviews from Google Play.
- Preprocessing and cleaning the data.
- Analyzing review content for sentiment and themes.
- Visualizing customer experience insights.
- Recommending improvements based on findings.

---

## 🏦 Targeted Apps

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

Each app has **400+ English reviews** scraped for analysis.

---

## 📁 Project Structure

├── .vscode/
│ └── settings.json
├── .github/
│ └── workflows/
│ └── unittests.yml
├── data/
│ ├── fintech_reviews.csv
│ └── fintech_reviews_cleaned.csv
├── notebooks/
│ ├── 1_data_scraping.ipynb
│ └── 2_text_cleaning_and_eda.ipynb
├── scripts/
│ ├── scraps.py
│ └── preprocessing.py
├── tests/
│ └── init.py
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## 🧠 Key Features

- ✅ Scrape Google Play Store reviews using `google-play-scraper`.
- ✅ Preprocess data (remove duplicates, clean text, normalize date).
- ✅ Detect language using `langdetect`.
- ✅ Visualize trends in ratings, review volume, and top themes.
- ✅ Prepare for sentiment and topic modeling (next steps).

---

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/your-username/fintech-customer-analytics.git
cd fintech-customer-analytics