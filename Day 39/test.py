class A:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


class B(A):
    """docstring for B"""

    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    def display_surname(self):
        print(self.surname)


class C(A):
    """docstring for C"""

    def __init__(self, name, middlename):
        super().__init__(name)

        self.middlename = middlename

    def display_middlename(self):
        print(self.middlename)


class D(B,C):
    """docstring for D"""

    def __init__(self, name, surname, middlename, pid):
        self.middlename = middlename
        self.surname = surname
        C.__init__(self, name, self.middlename)
        B.__init__(self, name, self.surname)
        self.pid = pid

    def display_pid(self):
        print(self.pid)


a = A("orvil")
a.display_name()

b = B('orvil', 'dsilva')
b.display_surname()

c = C('orvil', 'ranjan')
c.display_middlename()

d = D('orvil', 'dsilva', 'ranjan', 190202)
#
#
d.display_name()
d.display_middlename()
d.display_surname()
d.display_pid()