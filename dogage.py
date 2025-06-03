import streamlit as st
dogname = st.text_input("Enter your dog's name :")
age = st.number_input("Enter your dog's age: ")
def calc(age, dogname):
  age = age * 7
  st.write("The age of", dogname, "in human years is,", age)
if st.button("Calculate"):
  calc(age, dogname)


  
