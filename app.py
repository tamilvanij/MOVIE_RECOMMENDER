import streamlit as st
from recommender import get_recommendations

st.title("🎬 Movie Recommender")

st.write("✅ App is running")

movie = st.text_input("Enter a movie:")

st.write("Typed movie:", movie)

if movie != "":
    st.write("Processing...")

    recs = get_recommendations(movie)

    st.write("Recommendations:", recs)

    if not recs:
        st.error("Movie not found. Try: Toy Story (1995)")