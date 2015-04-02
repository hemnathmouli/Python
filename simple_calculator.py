print ('1.Addition')
print ('2.Subraction')
print ('3.Multiplication')
print ('4.Division')
print ('5.Exponentional')
oper=input("Enter the Operation number: ")
if (oper=='1'):
    print ("You selected Addition: ")
    n1_str=input("Enter first number: ")
    n1=int(n1_str)
    n2_str=input("Enter second number: ")
    n2=int(n2_str)
    add=n1+n2
    print ('On Adding',n1,'and ',n2,'the answer is',add)
elif (oper=='2'):
    print ("You selected Subract: ")
    n1_str=input("Enter first number: ")
    n1=int(n1_str)
    n2_str=input("Enter second number: ")
    n2=int(n2_str)
    sub=n1+n2
    print ('On Subracting',n1,'and ',n2,'the answer is',sub)
elif (oper=='3'):
    print ("You selected Multiplication: ")
    n1_str=input("Enter first number: ")
    n1=int(n1_str)
    n2_str=input("Enter second number: ")
    n2=int(n2_str)
    mul=n1*n2
    print ('On Multiplying',n1,'and ',n2,'the answer is',mul)
elif (oper=='4'):
    print ("You selected Division: ")
    n1_str=input("Enter first number: ")
    n1=float(n1_str)
    n2_str=input("Enter second number: ")
    n2=float(n2_str)
    div=n1/n2
    print ('On Adding',n1,'and ',n2,'the answer is',div)
elif (oper=='5'):
    print ("You selected Exponentional: ")
    n1_str=input("Enter first number: ")
    n1=int(n1_str)
    n2_str=input("Enter second number: ")
    n2=int(n2_str)
    sub=n1**n2
    print ('On Exponating',n1,'and ',n2,'the answer is',sub)
input('pressEnter')
    
    
    
