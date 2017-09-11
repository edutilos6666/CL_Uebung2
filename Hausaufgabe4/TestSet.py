set1 = {"der" , "das" , "die", "der"}
print(set1)
set2 = set(["der", "das", "die", "der"])
print(set2)
set3 = set("foobar")
print(set3)

set4 = frozenset("foobar")
print(set4)


print("der" in set1)
print("dier" not in set1)

print(sorted(set3))
print(len(set3))

print(sorted(set4))
print(len(set4))


set1.add("the")
set1.discard("der")
print(set1)


set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
set_or = set1 | set2
set_and = set1 & set2
set_diff1 = set1 - set2
set_diff2 = set2 - set1

print("set1 = " , set1)
print("set2 = ", set2)
print("set_or = ", set_or)
print("set_and = ", set_and)
print("set_diff1 = ", set_diff1)
print("set_diff2 = ", set_diff2)