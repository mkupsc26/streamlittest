import streamlit as st
x1 = st.number_input("Enter the first X coordinate ")
y1 = st.number_input("Enter the first Y coordinate ")
x2 = st.number_input("Enter the second X coordinate ")
y2 = st.number_input("Enter the second Y coordinate ")
  
def calcMid(x1,x2,y1,y2):
  xMid = (x1+x2)/2
  yMid = (y1+y2)/2
  midpoint = ("(" + str(xMid) + ", " + str(yMid) + ")")
  return midpoint  
  
if st.button("Calculate midpoint: "):
  x1=int(x1)
  x2=int(x2)
  y1=int(y1)
  y2=int(y2)
  mid = calcMid(x1,x2,y1,y2)
  st.write("Midpoint:", mid)
  
  


