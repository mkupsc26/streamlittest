import streamlit as st

st.write("You have entered a dark forest, would you like to take the left path or the right?")\

if st.button("Turn Left"):
  st.write("You turned left")
if st.button("Turn Right"):
  st.write("You turned right")
