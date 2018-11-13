class employee:
    def __init__(self,name,age,salary,code):
        self.name=name
        self.age=age
        self.salary=salary
        self.code=code
    def printdata(self):
        print ("     ")
        print("Employee name is ",self.name)
        print("Employee age is ",self.age)
        print("Employee salary is ",self.salary)
        print("Employee code is ",self.code)
n=input("Enter the name :")
a=int(input("Enter the age :"))
s=int(input("Enter the salary :"))
c=int(input("Enter the code :"))


e=employee(n,a,s,c)
e.printdata()
