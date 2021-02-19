def add(*args):
    return sum(args)


print(add(1,23,4,5,6,3,23,4,53,234))


def calculate(a,**kw):
    a += kw['add']
    a *= kw['multipy']
    print(a)


calculate(2,add=3,multipy=3)


class Car:

    def __init__(self, **kw):
        self.color = kw.get('color')
        self.model = kw.get('model')
        self.speed = kw.get('speed')


my_car = Car(color='red')
print(my_car.color, my_car.model)

