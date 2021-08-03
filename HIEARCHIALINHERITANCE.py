class Student:
    def __init__(self,usn=0,name=0,age=0):
        pass
    def getData(self):
        self.name = input("Enter Name:")
        self.usn = input("Enter USN:")
        self.age = int(input("Enter age:"))
    def display(self):
        print("USN:",self.usn)
        print("Name:",self.name)
        print("Age:",self.age)
class PgStudent(Student):
    def __init__(self, sem=0, fees=0, stipend=0):
        pass
    def PgGetData(self):
        super().getData()
        self.sem = int(input("Enter Semester:"))
        self.fees = int(input("Enter Fee:"))
        self.stipend = int(input("Enter Stipend:"))
    def display(self):
            super().display()
            print("Semester:", self.sem)
            print("Fee:", self.fees)
            print("Stipend:", self.stipend)
class UgStudent(Student):
    def __init__(self, sem=0, fees=0, stipend=0):
        pass
    def UgGetData(self):
        super().getData()
        self.sem = int(input("Enter Semester:"))
        self.fees = int(input("Enter Fee:"))
        self.stipend = int(input("Enter Stipend:"))
    def display(self):
            super().display()
            print("Semester:", self.sem)
            print("Fee:", self.fees)
            print("Stipend:", self.stipend)
pgStudent=PgStudent()
ugStudent=UgStudent()
while True:
    print("1.Enter PG Student Details:")
    print("2.Enter UG Student Details:")
    print("3.Display PG Student Data:")
    print("4.Display UG Student Data:")
    print("5.exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        pgStudent.PgGetData()
    elif ch==2:
        ugStudent.UgGetData()
    elif ch==3:
        pgStudent.display()
    elif ch==4:
        ugStudent.display()
    elif ch==5:
        break
    else:
        print("Invalid input please try again!")