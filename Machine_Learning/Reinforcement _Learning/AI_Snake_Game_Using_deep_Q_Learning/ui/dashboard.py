import streamlit as st

st.title("🐍 AI Snake Dashboard")

solver = st.selectbox("Choose AI", ["Greedy", "Hamilton", "DQN"])

st.write(f"Selected Solver: {solver}")

if st.button("Start Game"):
    st.success("Game Started 🚀")