class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname


    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname


    def __repr__(self):
        return "Person ({0} {1})".format(self.fname, self.lname)


    def to_csv(self):
        return "{0},{1}\n".format(self.fname, self.lname)



    
    

class Student(Person):
    def __init__(self, fname, lname, mnumber):
        Person.__init__(self,fname, lname)
        self.mnumber = mnumber
        
    def set__mnumber(self, mnumber):
        self.mnumber = mnumber

    def get_mnumber(self):
        return self.mnumber

    def __repr__(self):
        return "Student ({0} {1} {2})".format(self.fname,self.lname, self.mnumber)

    def to_csv(self):
        return "{0},{1},{2}\n".format(self.fname, self.lname, self.mnumber)



class Professor(Person):
    def __init__(self, fname,lname , wage):
        Person.__init__(self,fname, lname)
        self.wage = wage

    def set_wage(self, wage):
        self.wage = wage

    def get_wage(self):
        return self.wage

    def __repr__(self):
        return "Professor ({0} {1} {2})".format(self.fname, self.lname, self.wage)

    def to_csv(self):
        return "{0},{1},{2}\n".format(self.fname, self.lname, self.wage)



class PersonManager:
    def printPeople(self, people):
        for person in people:
            print(person)


    def write_to_file(self, people, filename):
        with open(filename, "w") as f_out:
            for person in people:
                f_out.write(person.to_csv())

    def csv_to_person(self, str):
        splitted = str.split(",")
        assert len(splitted) == 2
        return Person(splitted[0], splitted[1])

    def read_person_from_file(self, filename):
        ret = []
        with open(filename) as f_in:
            for line in f_in:
                line = line.rstrip("\n")
                ret.append(self.csv_to_person(line))

        return ret


    def csv_to_student(self, str):
        splitted = str.split(",")
        student = ""
        assert len(splitted) == 3
        try:
            fname = (splitted[0])
            lname = (splitted[1])
            age = int(splitted[2])
            student = Student(fname, lname, age)
        except:
            print("Error occurred.")

        return student


    def read_student_from_file(self,filename):
        ret = []
        with open(filename) as f_in:
            for line in f_in:
                line = line.rstrip("\n")
                ret.append(self.csv_to_student(line))


        return ret



    def csv_to_professor(self, line):
        splitted = line.split(",")
        assert len(splitted) == 3
        professor = ""
        try:
            fname = (splitted[0])
            lname = (splitted[1])
            wage = float(splitted[2])
            professor = Professor(fname, lname, wage)

        except:
            print("Error occurred.")

        return professor


    def read_professor_from_file(self, filename):
        ret = []
        with open(filename) as f_in:
            for line in f_in:
                line = line.rstrip("\n")
                ret.append(self.csv_to_professor(line))

        return ret






def main():
    pm = PersonManager()
    p1 = Person("foo", "bar")
    p2 = Student("edu", "tilos", 1234)
    p3 = Professor("pako", "deko", 123.123)

    pm.printPeople([p1, p2, p3])

    p2 = Person("edu", "tilo")
    p3 = Person("pako", "deko")

    pm.write_to_file([p1, p2, p3], "people.csv")

    people = pm.read_person_from_file("people.csv")
    print("<<All People>>")
    for person in people:
        print(person)


    p1 = Student("foo", "bar", 10)
    p2 = Student("edu", "tilos", 20)
    p3 = Student("pako", "deko", 30)

    pm.write_to_file([p1, p2, p3], "students.csv")
    students = pm.read_student_from_file("students.csv")
    print("<<All Students>>")
    for student in students:
        print(student)


    p1 = Professor("foo", "bar", 100.0)
    p2 = Professor("edu", "tilos", 200.0)
    p3 = Professor("pako", "deko", 300.0)
    pm.write_to_file([p1, p2, p3], "professors.csv")
    professors = pm.read_professor_from_file("professors.csv")
    print("<<All Professors>>")
    for p in professors:
        print(p)


main()




