def  test1():
    assert 1== 1



class ComplexNumber:
    def __init__(self, real= 0, imag= 0):
        self.real = real
        self.imag = imag

    def add(self, other):
        ret = ComplexNumber()
        ret.real = self.real + other.real
        ret.imag = self.imag + other.imag
        return ret

    def subtract(self, other):
        ret = ComplexNumber
        ret.real = self.real - other.real
        ret.imag = self.imag - other.imag
        return ret

    def to_string(self):
        ret = str(self.real) + " + i*" + str(self.imag)
        if self.imag == 0:
            ret = self.real
        elif self.real == 0:
            ret = "i*" + str(self.imag)
        elif self.imag < 0:
            ret = str(self.real) + " + (i*" + str(self.imag) + ")"

        return ret



def test_complex_number():
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(2, 2)
    assert n1.real == 1
    assert n1.imag == 1
    assert n2.real == 2
    assert n2.imag == 2
    _sum = n1.add(n2)
    _subtract = n1.subtract(n2)
    assert _sum.real == 3
    assert _sum.imag == 3
    assert _subtract.real == -1
    assert _subtract.imag == -1




class Worker:
    def __init__(self, id , name, age, wage):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage


def test_worker():
    w1, w2 = Worker(1, "foo", 10, 100.0), Worker(2, "bar", 20, 200.0)
    assert w1.id == 1
    assert w1.name == "foo"
    assert w1.age == 10
    assert w1.wage == 100.0

    assert w2.id == 2
    assert w2.name == "bar"
    assert w2.age == 20
    assert w2.wage == 200.0

