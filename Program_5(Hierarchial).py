class student:
    def __init__(self,usn,name,age):
        self.usn=usn
        self.name=name
        self.age=age
    def accept(self):
        self.usn=input("Enter usn")
        self.name=input("Input name")
        self.age=input("Input age")
    def display(self):
        print(self.usn)
        print(self.name)
        print(self.age)
class ug(student):
    def __init__(self,sem,fees,stipend):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def ugaccept(self):
        super().accept()
        self.sem=input("Enter sem")
        self.fees=input("Input fees")
        self.stipend=input("Input stipend")
    def ugdisplay(self):
        super().display()
        print(self.sem)
        print(self.fees)
        print(self.stipend)
class pg(student):
    def __init__(self,sem,fees,stipend):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def pgaccept(self):
        super().accept()
        self.sem=input("Enter sem")
        self.fees=input("Input fees")
        self.stipend=input("Input stipend")
    def pgdisplay(self):
        super().display()
        print(self.sem)
        print(self.fees)
        print(self.stipend)
d={}
d1={}
while True:
    print("1:input UG student details")
    print("2:display ug")
    print("3.input pg details")
    print("4.display pg")
    ch=int(input("Enter your choice"))
    if ch==1:
        u=ug('','','')
        u.ugaccept()
        u.ugdisplay()
    elif ch==2:
        d[u.name]=u.__dict__
        print(d)
    elif ch==3:
        p=pg('','','')
        p.pgaccept()
        p.pgdisplay()
    elif ch==4:
        d1[p.name]=p.__dict__
        print(d1)
    else:
        print("Invalid choice")

