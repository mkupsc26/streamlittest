def main():
  inputs()

def inputs(): 
  global dogname
  global age
  dogname = st.text_input("Enter your dog's name :")
  age = st.number_input("Enter your dog's age: ")
  return dogname
  return age
def calculations():
  age = age * 7
  st.write(
  
