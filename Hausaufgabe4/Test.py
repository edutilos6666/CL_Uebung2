filename = "foo.txt"
with open(filename , "w") as f :
    f.write("edu\n");
    f.write("tilos\n");
    f.write("pako\n");


with open(filename, "r") as f:
    print("<<content of " + filename + ">>")
    for line in f:
        line = line.strip()
        print(line)



with open(filename , "a") as f:
    f.write("new_edu\n")
    f.write("new_tilo\n")


with open(filename, "r") as f:
    print("<<content>>")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        print(line)


with open(filename, "r") as f:
    print("\n<<content>>")
    content = f.read()
    print(content)


filename = "person.txt"

class Person:
    def __init__(self, name, age , wage):
        self.name =  name
        self.age = age
        self.wage = wage

    def to_string(self):
        msg , nl2 = "", "\n"
        nl = ";"
        msg = msg + "name = "+ self.name + nl + "age = " + str(self.age) + nl+ "wage = " + str(self.wage) + nl2
        return msg


p1 = Person("foo", 10, 100.0)
p2 = Person("bar", 20 , 200.0)
print(p1.to_string())
print(p2.to_string())


import copy
with open(filename, "w") as f:
    people = [copy.deepcopy(p1), copy.deepcopy(p2), Person("bim", 30 , 300.0) ]
    for p in people:
        f.write(p.to_string())

with open(filename, "r") as f:
    print("<<content of " + filename + ">>")
    for line in f:
        line = line.strip()
        props = line.split(";")
        for prop in props:
            splitted = prop.split(" = ")
            k,v = splitted[0], splitted[1]
            print(k , "=> ", v)


