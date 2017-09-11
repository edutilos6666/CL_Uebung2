from dictionary import *
d = dictionary()
d.set_def("foo", ["bar", "bim"])
print(d.get_def("foo"))

d.del_def("foo", ["bar"])
print(d.get_def("foo"))