def main():
  inputs()
  calculations()

def inputs(): 
  dogname = st.text_input("Enter your dog's name :")
  age = st.number_input("Enter your dog's age: ")
  return dogname
  return age
def calculations(age, dogname):
  age = age * 7
  st.write("The age of", dogname, "in human years is,", age)
main()
  
