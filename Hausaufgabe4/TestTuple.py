t1 = ("foo", )
t2 = ("bar", 10, 100.0)

print(type(t1))
print(type(t2))

t3 = ("bim")
print(type(t3))
t4 = ()
print(type(t4))


name , age, wage= t2
print("name = ", name , "age = ", age , "wage = ", wage)


for el in t2:
    print(el)


print()
for i in range(len(t2)):
    print(t2[i])

print()
for i , el in enumerate(t2):
    print(i, "=> ", el)


print(t2)


print(t2[0:2])


t4 = t4 + t2 + ("pako", )
print(t4)

print(t4.index("pako"))

t5 = (("foo", 10 , 100.0), ("bar", 20 , 200.0))
print(t5[0])
print(t5[0][0], "; ", t5[0][1], "; ", t5[0][2])