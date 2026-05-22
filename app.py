import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load the data
books = pickle.load(open('books.pkl', 'rb'))
popular_books = pickle.load(open('popular_books1.pkl', 'rb'))
my_books = pickle.load(open('my_books.pkl', 'rb'))

# computing similarity
@st.cache_data
def get_similarity():
    tfidf = TfidfVectorizer(max_features=5000)
    vectors = tfidf.fit_transform(books['tags'])
    return cosine_similarity(vectors)

similarity = get_similarity()

# recommend function
def recommend(name):
    book_index = books[books["title"] == name].index[0]
    des = similarity[book_index]
    des = list(enumerate(des))
    des = sorted(des, key=lambda x: x[1], reverse=True)
    top5 = des[1:6]
    recommended_books = []
    for i in top5:
        recommended_books.append([
            books.iloc[i[0]].title,
            books.iloc[i[0]].thumbnail
        ])
    return recommended_books

# global styling
st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# sidebar
st.sidebar.markdown("## 🚩 Navigation")
page = st.sidebar.radio("Select Page", [
    "🏠 Home",
    "📖 Popular Books",
    "🔍 Find Similar Books",
    "✨ My Recommendations"
], label_visibility="collapsed",
   index=["🏠 Home", "📖 Popular Books", "🔍 Find Similar Books", "✨ My Recommendations"].index(
       st.session_state.get("page", "🏠 Home")
   ))

# home page

if page == "🏠 Home":
    st.markdown("""
        <h1 style='text-align:center; color:#00d4aa;'>
        📚 Your Next Great Read Awaits</h1>
        <p style='text-align:center; color:gray; font-size:16px;'>
        Discover books that speak to you. Our recommendation 
        system helps you uncover hidden literary gems.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📖 Trending Now")
        st.write("Browse the most loved and talked about books from our dataset.")
        if st.button("Browse Popular Books"):
            st.session_state["page"] = "📖 Popular Books"
            st.rerun()

    with col2:
        st.markdown("### 🔍 If You Liked That...")
        st.write("Enter a book you enjoyed and find similar books with same themes.")
        if st.button("Find Similar Books"):
            st.session_state["page"] = "🔍 Find Similar Books"
            st.rerun()

    with col3:
        st.markdown("### ✨ Tailored For You")
        st.write("Pick multiple books you love and get personalized recommendations.")
        if st.button("Personalized For You"):
            st.session_state["page"] = "✨ My Recommendations"
            st.rerun()

# popular page
elif page == "📖 Popular Books":
    st.markdown("<h1 style='text-align:center; color:#00d4aa;'>📖 Popular Books</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Top books from our dataset</p>",
                unsafe_allow_html=True)
    st.markdown("---")

    # show first 10 books
    popular = popular_books
    for i in range(0, 15, 5):
        cols = st.columns(5)
        for idx in range(5):
            book = popular.iloc[i + idx]
            with cols[idx]:
                st.markdown(f"""
                    <img src="{book['thumbnail']}" 
                    style="width:150px; height:220px; object-fit:cover; border-radius:8px;">
                    <p style='text-align:center; font-size:13px; 
                    font-weight:bold; margin-top:8px'>{book['title']}</p>
                """, unsafe_allow_html=True)

# find similar book page
elif page == "🔍 Find Similar Books":
    st.markdown("<h1 style='text-align:center; color:#00d4aa;'>🔍 Find Similar Books</h1>",
                unsafe_allow_html=True)
    st.markdown("---")

    selected_book = st.selectbox("Enter a book name", books['title'].values)

    if st.button("Recommend"):
        results = recommend(selected_book)
        cols = st.columns(5)
        for idx, result in enumerate(results):
            with cols[idx]:
                st.markdown(f"""
                    <img src="{result[1]}" 
                    style="width:150px; height:220px; object-fit:cover; border-radius:8px;">
                    <p style='text-align:center; font-size:13px; 
                    font-weight:bold; margin-top:8px'>{result[0]}</p>
                """, unsafe_allow_html=True)

# my recommendation page
elif page == "✨ My Recommendations":
    st.markdown("<h1 style='text-align:center; color:#00d4aa;'>✨ My Recommendations</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Books I personally love!</p>",
                unsafe_allow_html=True)
    st.markdown("---")

    for i in range(0, len(my_books), 5):
        cols = st.columns(5)
        for idx, (_, book) in enumerate(my_books.iloc[i:i+5].iterrows()):
            with cols[idx]:
                st.markdown(f"""
                    <img src="{book['thumbnail']}" 
                    style="width:150px; height:220px; object-fit:cover; border-radius:8px;">
                    <p style='text-align:center; font-size:13px; 
                    font-weight:bold; margin-top:8px'>{book['title']}</p>
                """, unsafe_allow_html=True)