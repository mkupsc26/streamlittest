import streamlit as st
x1 = st.number_input("Enter the first X coordinate ")
y1 = st.number_input("Enter the first Y coordinate ")
x2 = st.number_input("Enter the second X coordinate ")
y2 = st.number_input("Enter the second Y coordinate ")

def calculateDist(x1, y1, x2, y2):
  SubX = x1 - x2
  SubY = y1 - y2
  
  print("x sub:", SubX)
  print("y sub:", SubY)
  
  SquareX = SubX ** 2
  SquareY = SubY ** 2

  print("x square:", SquareX)
  print("y square:", SquareY)

  add = SquareX + SquareY
  
  print(add)
  
  ans = math.sqrt(add)

  return ans

def calcMid(x1,x2,y1,y2):
  xMid = (x1+x2)/2
  yMid = (y1+y2)/2
  midpoint = ("(" + str(xMid) + ", " + str(yMid) + ")")
  return midpoint  

if st.button("Calculate the distance: "):
  x1=int(x1)
  x2=int(x2)
  y1=int(y1)
  y2=int(y2)
    
  dist = calculateDist(x1, y1, x2, y2)
  dist_str = str(round(dist, 2))

  st.write("The distance is " + dist_str)
  
if st.button("Calculate midpoint:"):
  
  x1=int(x1)
  x2=int(x2)
  y1=int(y1)
  y2=int(y2)
  mid = calcMid(x1,x2,y1,y2)
  st.write("Midpoint:", mid)
  
  


