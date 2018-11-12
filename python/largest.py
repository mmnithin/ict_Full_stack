# num1=int(input("Enter the 1st number"))
# num2=int(input("Enter the 2nd number"))
# num3=int(input("Enter the 3rd number"))
# if(num1>num2):
#     if(num1>num3):
#         print(num1,"is largest number")
#     else:
#         print(num3,"is largest number")
# else:
#     if(num2>num3):

#         print(num2,"is largest number")
#     else:
#         print(num3,"is largest number")

def largest(x,y,z):
    if x>y:
        if x>z:
            return x;


            
        else:
           
            return z;
    else:
        if y>z:
            
            return y;
        else:
          
            return z;
    

num1=int(input("Enter the 1st number"))
num2=int(input("Enter the 2nd number"))
num3=int(input("Enter the 3rd number"))
result=largest(num1,num2,num3);
print(result,"is largest number")