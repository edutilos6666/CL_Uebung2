from prettytable import PrettyTable

headers = ['id', 'name' , 'age', 'wage']

table = PrettyTable(headers)

class Worker:
    def __init__(self, id, name, age, wage):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage


workers = [
    Worker(1, "foo", 10, 100.0),
    Worker(2, "bar", 20, 200.0),
    Worker(3, "bim", 30, 300.0)
]

for worker in workers:
    row = [worker.id, worker.name, worker.age, worker.wage]
    table.add_row(row)



table.reversesort = True
table.sortby = 'age'
print(table)