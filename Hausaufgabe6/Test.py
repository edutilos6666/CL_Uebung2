def subtrahiere(x, y):
    return x -y


print(subtrahiere(3 , y = 10))


for i in range(0, 5):
    print(i)

print("now i = %d" %(i))



test = "foo"
def change_global1():
    test = "bar"

change_global1()
print("test = ", test)

def change_global2():
    global test
    test = "bar"

change_global2()
print("test = ", test)


name = "edutilos"
def print_name():
    name = "foobar"
    return name 

name = print_name()

print("Name = ", name)