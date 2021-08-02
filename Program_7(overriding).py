class employee:
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self):
        self.p_raise = 1.04
        self.pay=self.pay*self.p_raise
        return self.pay
    def display(self):
        print(self.first)
        print(self.last)
        print(self.empid)
        print(self.pay)

class developer(employee):
    p_raise = 1.05
    def apply_raise(self):
        self.pay=self.pay*self.p_raise
        return self.pay
class manager(employee):
    p_raise = 1.06
    def apply_raise(self):
        self.pay=self.pay*self.p_raise
        return self.pay
d={}
while True:
    print("1:Print Developer employee details")
    print("1:Print Manager employee details")
    ch=int(input("Enter your choice"))
    if ch==1:
        first=input("Enter first name")
        last=input("Enter last name")
        empid=input("Enter empid")
        pay=int(input("Enter pay amount"))
        emp1=developer(first,last,empid,pay)
        print("Intial pay:",emp1.pay)
        print("Pay after raise:",emp1.apply_raise())
        d[emp1.empid]=emp1.__dict__
        print(d,"\n")
    elif ch==2:
        first=input("Enter first name")
        last=input("Enter last name")
        empid=input("Enter empid")
        pay=int(input("Enter pay amount"))
        emp2=manager(first,last,empid,pay)
        print("Intial pay:",emp2.pay)
        print("Pay after raise:",emp2.apply_raise())
        d[emp2.empid]=emp2.__dict__
        print(d,"\n")
    else:
        print("Invalid choice")