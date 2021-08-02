class student:
    def __init__(self):
        self.usn=''
        self.name=''
        self.age=''
    def accept(self):
        self.usn=input("Enter usn")
        self.name=input("Input name")
        self.age=input("Input age")
class derived1(student):
    def __init__(self):
        self.s1=0
        self.s2=0
        self.s3=0
        self.s4=0
        self.s5=0
    def marks(self):
        super().accept()
        self.s1=int(input("Enter s1:"))
        self.s2=int(input("Enter s2:"))
        self.s3=int(input("Enter s3:"))
        self.s4=int(input("Enter s4:"))
        self.s5=int(input("Enter s5:"))
class derived2(derived1):
    def __init__(self):
        super().__init__()
    def display(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5
        self.per=self.total/5
        print(self.usn)
        print(self.name)
        print(self.age)
        print(self.total)
        print(self.per)

d={}
n=int(input("Enter the number of students:"))
for i in range(1,n+1):
    d2=derived2()
    d2.marks()
    d2.display()
    d[i]=d2.__dict__
for key in d.keys():
    print(key,d[key])
    print("\n")