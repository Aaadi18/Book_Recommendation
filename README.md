# 📚 Book Recommendation System

A content-based book recommendation system that suggests 
5 similar books based on your input using NLP and Machine Learning.

## 🔗 Live Demo
https://bookrecommendation-b6faq8qq4rzsfxgxawuvyo.streamlit.app/

## 🛠️ Tech Stack
- Python
- Scikit-learn
- NLTK 
- Streamlit
- Pandas

## 📊 Dataset
- 6000+ books from Kaggle
- Features: Title, Authors, Categories, Description, Thumbnail

## ⚙️ How It Works
1. Title, Authors, Categories and Description are combined into tags
2. Stopwords removed using NLTK
3. TF-IDF Vectorizer converts tags into numerical vectors
4. Cosine Similarity finds most similar books
5. Top 5 recommendations displayed with book covers

## 🚀 Run Locally
1. Clone the repo
   git clone https://github.com/Aaadi18/Book_Recommendation.git

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

├── data.csv                  → Raw dataset
└── requirements.txt          → Dependencies
