# 💼 Customer Experience Analytics for Fintech Apps

This project analyzes user reviews from the Google Play Store for three major Ethiopian mobile banking applications. The goal is to extract insights about customer satisfaction using sentiment analysis, thematic clustering, and visualizations — simulating the role of a Data Analyst at Omega Consultancy.

---

## 🚀 Objective

- Scrape user reviews from Google Play.
- Preprocess and clean the data.
- Analyze review content for sentiment (BERT-based) and themes.
- Load structured data into an Oracle database.
- Visualize customer experience insights.
- Recommend improvements based on findings.

---

## 🏦 Targeted Apps

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

Each app has 400+ English-language reviews scraped and analyzed.

---

## 📁 Project Structure

fintech-customer-analytics/
├── .vscode/
│ └── settings.json
├── .github/
│ └── workflows/
│ └── unittests.yml
├── data/
│ ├── fintech_reviews.csv
│ ├── fintech_reviews_cleaned.csv
│ └── final_reviews_with_themes.csv
├── notebooks/
│ ├── 1_data_scraping.ipynb
│ ├── 2_text_cleaning_and_eda.ipynb
│ └── 3_sentiment_and_theming.ipynb
├── scripts/
│ ├── scraps.py
│ ├── preprocessing.py
│ └── insert_review.py # NEW: Loads reviews into Oracle DB
├── sql/
│ └── create_tables.sql # NEW: DB schema for banks and reviews
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

✅ Scrape Google Play Store reviews using `google-play-scraper`  
✅ Preprocess data (deduplication, cleaning, date normalization)  
✅ Language detection using `langdetect`  
✅ Keyword extraction using TF-IDF  
✅ Sentiment analysis using pretrained BERT (`nlptown/bert-base-multilingual-uncased-sentiment`)  
✅ Thematic classification using rule-based or manual tagging  
✅ Oracle database integration via `oracledb`  
✅ SQL schema to store banks and reviews  
✅ Visualization-ready CSV with labeled data  

---

## 🗃️ Database Integration (Oracle)

The script `insert_review.py` does the following:

- Connects to an Oracle DB using `oracledb`
- Creates or uses an existing user (`bank_reviews`)
- Inserts distinct bank names into `banks` table
- Inserts cleaned reviews with BERT scores and themes into `reviews` table

Make sure to:

- Set up your Oracle instance and user credentials
- Run `sql/create_tables.sql` to initialize the schema
- Edit DB credentials in `insert_review.py` accordingly

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/fintech-customer-analytics.git
cd fintech-customer-analytics

# Create virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
🧪 Testing
bash
Copy
Edit
# Run test files (if added under `tests/`)
pytest
📊 Sample Output
Bank	Sentiment	Theme	Keywords
CBE	Positive	Performance	good, responsive, stable
BOA	Negative	UX Issues	freeze, slow, uninstall
Dashen	Neutral	Transaction	send money, link, fail
