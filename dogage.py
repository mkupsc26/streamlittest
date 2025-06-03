import streamlit as st
def calc():
  age = age * 7
  st.write("The age of", dogname, "in human years is,", age)
dogname = st.text_input("Enter your dog's name :")
age = st.number_input("Enter your dog's age: ")
st.button("Calculate")
if st.button():
  calc()


  
