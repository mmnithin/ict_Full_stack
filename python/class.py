class student:
    
    def __init__(self,n,r,a):
        self.name=n
        self.rollno=r
        self.age=a

    def printdata(self):
        print("Name is :",self.name)
        print("Roll number is",self.rollno)
        print("age number is",self.age)

       
s=student("nithin",1,20)



s.printdata()




