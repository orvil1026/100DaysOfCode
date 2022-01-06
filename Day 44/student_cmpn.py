class Student:
    total = 0

    def __init__(self, pid, name, contact):
        self.pid = pid
        self.name = name
        self.contact = contact
        Student.total = Student.total + 1

    def print_details(self):
        print(f"\n\nPID:{self.pid}\nName:{self.name}\nContact:{self.contact}")


    @classmethod
    def print_total(cls):
        print(f"\nTotal Students:{cls.total}")

    @staticmethod
    def greet():
        print("\nWelcome to SFIT")


class CMPN(Student):

    ctotal = 0

    def __init__(self, pid, name, contact, subject):
        self.subject = subject
        CMPN.ctotal += 1
        super().__init__(pid, name, contact)

    @classmethod
    def print_ctotal(cls):
        print(f"Total Students in CMPN branch:{CMPN.ctotal}")


class EXTC(Student):

    ctotal = 0

    def __init__(self, pid, name, contact, subject):
        self.subject = subject
        EXTC.ctotal += 1
        super().__init__(pid, name, contact)

    @classmethod
    def print_ctotal(cls):
        print(f"Total Students in EXTC branch:{CMPN.ctotal}")

ch=0

while ch != 4:

    print("\nMENU.\n1.New CMPN Student \n2.New EXTC Student ")
    print("3.Total Students \n4.Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        pid = input("Enter your PID:")
        name = input("Enter your name:")
        contact = input("Enter your contact number:")
        subject = input("Enter your special subject:")

        c1 = CMPN(pid, name, contact, subject)

        Student.greet()

        print("New student Details :")
        c1.print_details()

        CMPN.print_ctotal()

    elif ch == 2:
        pid = input("Enter your PID:")
        name = input("Enter your name:")
        contact = input("Enter your contact number:")
        subject = input("Enter your special subject:")

        c1 = EXTC(pid, name, contact, subject)

        Student.greet()

        print("New student Details :")
        c1.print_details()

        EXTC.print_ctotal()

    elif ch == 3:

        Student.print_total()

    else:

        print("Invalid Choice!")