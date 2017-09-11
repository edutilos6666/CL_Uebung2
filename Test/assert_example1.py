class SimpleMath:
    def add(self, x, y):
        return x +y

    def subtract(self, x, y):
        return x -y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y




def main():
    sm = SimpleMath()
    x , y = 20 , 10
    assert 30 == sm.add(x,y) , "Addition error"
    assert 10 == sm.subtract(x,y)
    assert 200 == sm.multiply(x, y)
    assert 2.0 == sm.divide(x,y)


main()
