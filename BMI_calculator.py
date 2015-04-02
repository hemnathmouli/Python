print ("BMI calculator!!")
Name=input("Name: ")
x_str=input("Weight:(kg) ")
x=float(x_str)
y_str=input("Height:(m) ")
y=float(y_str)
BMI= x/y**2
if(BMI<18):
  print ('Hey', Name, 'you need to improve a lot because your BMI is ',BMI)
elif(18<BMI<25):
  print ('Hey', Name, 'you are perfect and your BMI is ',BMI) 
elif(BMI>30):
  print ('Hey', Name, 'you are obese(extra weight) try harder. Your BMI is',BMI) 
input("Press Enter")
