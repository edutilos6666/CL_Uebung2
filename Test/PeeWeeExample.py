import peewee

pathname = "test.db"
db = peewee.SqliteDatabase(pathname)
class Person(peewee.Model):
    personId = peewee.IntegerField()
    fname = peewee.TextField()
    lname = peewee.TextField()

    class Meta:
        database = db




db.connect()
Person.create_table(True)
p1 = Person(personId = 1 , fname ="foo", lname = "bar")
p2 = Person(personId = 2 , fname = "edu",lname =  "tilos")
p3 = Person(personId = 3 , fname = "foo", lname = "pako")
p1.save()
p2.save()
p3.save()

#Person.get()
# for p in Person.filter(fname="foo"):
for p in Person.select():
    print(p.personId , " and ", p.fname , " and ", p.lname)

db.close()


db.connect()
for p in Person.select():
    p.delete_instance()
db.close()
