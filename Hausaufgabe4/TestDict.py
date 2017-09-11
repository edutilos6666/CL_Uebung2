d1 = {}
d1["fname"] = "foo"
d1["lname"] = "bar"
d1["age"] = 10
print(d1["fname"], d1["lname"], d1["age"])

d2 = dict()
d2["fname"] = "pako"
print(d2["fname"], d2.get("lname"))


d3 = {"name": "foo", "age": 10 , "wage": 100.0}
print(d3["name"], d3["age"], d3["wage"])



d4 = {
    ("fname", "lname"): ["foo", "bar"],
    "age": 10,
    "Points": {"Richtig": 90, "Falsch": 10}
}

print(d4[("fname", "lname")][0])
print(d4[("fname", "lname")][1])
print(d4["age"])
print(d4["Points"]["Richtig"])
print(d4["Points"]["Falsch"])


print(len(d4))
print("fname" in d4)
print("Points" in d4)



keys = d1.keys()
values = d1.values()

for key in keys:
    print(key)

print()
for value in values:
    print(value)

print()

items = d1.items()
for item in items:
    print(item[0], item[1])



korpus = "foo bar bim foo pako bar deko edutilos"
words = korpus.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) +1

print(frequency)


frequency = {}

for word in words:
    if word in frequency: frequency[word] += 1
    else: frequency[word] = 1

print(frequency)

print()
for key in d1:
    print(key , "=> ", d1[key])

print()


for k, v in d1.items():
    print(k , "=> ", v)

print()