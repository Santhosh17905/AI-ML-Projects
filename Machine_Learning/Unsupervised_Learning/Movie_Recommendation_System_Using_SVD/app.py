import streamlit as st
from model import recommend
from poster_fetcher import get_poster
import json

st.set_page_config(layout="wide")

# ---------------- CSS ----------------

st.markdown("""
<style>

body{
background-color:#141414;
color:white;
}

.movie-card{
transition: transform .3s;
}

.movie-card:hover{
transform: scale(1.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------

with open("user.json") as f:
    users = json.load(f)

st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

logged_in = False

if username in users and users[username] == password:
    st.sidebar.success("Logged in")
    logged_in = True

# ---------------- WATCHLIST ----------------

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

# ---------------- HEADER ----------------

st.title("🎬 Movie Recommendation System")

# ---------------- SEARCH ----------------

if st.button("Recommend"):
    movie_title = st.text_input("Enter a movie you like:")
    results = recommend(movie_title=movie_title, top_n=5)

    st.subheader("⭐ Recommended Movies")
    cols = st.columns(5)

    for i, r in enumerate(results):
        with cols[i]:
            st.image(get_poster(r["title"]), width="stretch")  # now flexible
            st.write(r["title"])
            st.write(f"⭐ Predicted Rating: {r['rating']}")
            
            trailer_query = r["title"].replace(" ", "+")
            st.markdown(
                f"[🎬 Trailer](https://www.youtube.com/results?search_query={trailer_query}+trailer)"
            )

            if logged_in:
                if st.button(f"❤️ Add {i}"):
                    st.session_state.watchlist.append(r["title"])

# ---------------- TRENDING SECTION ----------------

st.subheader("🔥 Trending Movies")

trending = [
    "Avengers",
    "Batman",
    "Spider-Man",
    "Iron Man",
    "Thor"
]

cols = st.columns(5)

for i, movie in enumerate(trending):
    with cols[i]:
        st.image(get_poster(movie), width="stretch")
        st.write(movie)

# ---------------- WATCHLIST ----------------

st.sidebar.title("❤️ My Watchlist")

for m in st.session_state.watchlist:

    st.sidebar.write(m)