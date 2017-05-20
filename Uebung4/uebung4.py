###############################
# Aufgabe 1
###############################

# Generieren Sie mithilfe der Methode random.randint() zunaechst 20 Zahlen zwischen 0 und 1.000.000 und
# speichern Sie diese in einer Liste ab. Berechnen Sie folgend die Quersummen all dieser Zahlen und speichern
# Sie diese ab. Geben Sie schließlich die größte und die kleinste Quersumme aus.
import random
list1 = []
list2 = []
lower = 20
upper = 1000000
for i in range(0, 20):
    list1.append(random.randint(lower , upper))

def calc_quersumme(number):
    ret = 0
    while number > 0:
        rest = number % 10
        number = number // 10
        ret += rest
    return ret

for el in list1:
    list2.append(calc_quersumme(el))


def print_list(list0):
    for el in list0:
        print(el , end= " ")
    print()
print_list(list1)
print_list(list2)


def find_min_max(list0):
    min_el = list0[0]
    max_el = list0[0]
    for i in range(1, len(list0)-1):
        if min_el > list0[i]:
            min_el = list0[i]
        if max_el < list0[i]:
            max_el = list0[i]

    return (min_el, max_el)


min_el, max_el = find_min_max(list2)
print("minimum quersumme = ", min_el)
print("maximum quersumme = ", max_el)


###############################
# Aufgabe 2
###############################

# Geben Sie mithilfe die durchschnittliche Satzlänge der drei Texte aus.
# Verwenden Sie dazu eine der drei vorgestellten Varianten für for-Schleifen

text1 = """Welch vortrefflicher Mensch hat mich aufgeschlagen?
Wenn es jemand ist, der mich lesen und verstehen kann, 
dann möge er mich – auch wenn es etwas an mir zu tadeln gibt – freundlich behandeln 
und mich mit übler Nachrede verschonen: dies wird ihn ehren."""

text2 = """Ich weiß sehr gut, daß ich gar nicht bereinigt und begradigt und auch nicht so gut
geschrieben bin, daß mich ein ruchloser Mensch mit Leichtigkeit verfälschte; 
denn niemand kann sich vor ihnen recht schützen, wie kunstgerecht auch immer er schreibt.
Keine Erzählung ist so vortrefflich, daß sie sie nicht verfälschen, ich weiß es genau.
Was ich auch Falsches von ihnen erdulde, weh, wem kann ich dies klagen?
Mir aber bedeutet es gar keine Last, wenn ich die Lobpreisung der Vortrefflichen erringen kann. """

text3 = """Daß ich es nicht lassen kann, bei offenem Fenster zu
schlafen. Elektrische Bahnen rasen läutend durch meine
Stube. Automobile gehen über mich hin. Eine Tür fällt zu. Irgendwo
klirrt eine Scheibe herunter, ich höre ihre großen Scherben lachen,
die kleinen Splitter kichern. Dann plötzlich dumpfer, eingeschlossener
Lärm von der anderen Seite, innen im Hause. Jemand steigt die
Treppe. Kommt, kommt unaufhörlich. Ist da, ist lange da, geht
vorbei. Und wieder die Straße. Ein Mädchen kreischt: Ah tais-toi, je
ne veux plus. Die Elektrische rennt ganz erregt heran, darüber fort,
fort über alles. Jemand ruft. Leute laufen, überholen sich. Ein Hund
bellt. Was für eine Erleichterung: ein Hund. Gegen Morgen kräht sogar
ein Hahn, und das ist Wohltun ohne Grenzen. Dann schlafe ich plötzlich
ein."""


def number_of_words(line):
    words = line.split(" ")
    return len(words)

def durch_satz_laenge(text):
    list0 = []
    att0 = text.split(". ")
    for line0 in att0:
        att1 = line0.split(".\n")
        for line in att1:
            att2 = line.split("?\n")
            for line2 in att2:
                if line2 == "": continue
                att3 = line2.split("? ")
                for line3 in att3:
                    if line3 != "":
                        list0.append(line3)

    # for line in list0:
    #     print("CARD " , line)
    # print(len(list0))
    sum = 0
    for line in list0:
        sum += number_of_words(line)

    return sum / len(list0)

durchsatz = durch_satz_laenge(text1)
print("durchschnittliche Satzlaenge des text1 = ", durchsatz)
durchsatz = durch_satz_laenge(text2)
print("durchschnittliche Satzlaenge des text2 = ", durchsatz)
durchsatz = durch_satz_laenge(text3)
print("durchschnittliche Satzlaenge des text3 = ", durchsatz)



def durch_satz_laenge_2(text):
    import re
    pattern = "\.\s+|\.\n+|\?\s+|\?\n+"
    lines = re.split(pattern , text)
    list0 = []
    for line in lines:
        if line == "": continue
        list0.append(line)

    lines = list0
    sum = 0
    for line in lines:
        sum += number_of_words(line)

    return sum / len(lines)

print("mit regex")
durchsatz = durch_satz_laenge_2(text1)
print("durchschnittliche Satzlaenge des text1 = ", durchsatz)
durchsatz = durch_satz_laenge_2(text2)
print("durchschnittliche Satzlaenge des text2 = ", durchsatz)
durchsatz = durch_satz_laenge_2(text3)
print("durchschnittliche Satzlaenge des text3 = ", durchsatz)

###############################
# Aufgabe 3
###############################

# Sortieren die in Aufgabe 1 entstandene Liste der Quersummen absteigend. Verwenden Sie dazu sorted und sort().

###############################
# Aufgabe 3
###############################
list2_sorted = sorted(list2, reverse=True)
print(list2_sorted)
print(list2)
list2.sort(reverse=True)
print(list2)
# Zeigen Sie anhand von selbst erstellten Listen und Variablen die Unterschiede zwischen einer Kopie und einer Referenz.
# Was passiert, wenn man Listen verändert? Wie vermeide ich ungewollte Änderungen?
class Person:
    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage

    def to_string(self):
        return ", ".join([self.name, str(self.age), str(self.wage)])


p1 = Person("foo", 10, 100.0)
p2 = Person("bar", 20 , 200.0)
p3 = Person("bim", 30 , 300.0)
list0 = [p1, p2, p3]

def print_list_people(list0):
    for p in list0:
        print(p.to_string())


print_list_people(list0)

list2 = list0
list2[0].name = "new_foo"
print_list_people(list0)

import copy
list2 = copy.copy(list0)
list2[0].name = "old_foo"
print_list_people(list0)

list2 = copy.deepcopy(list0)
list2[0].name = "new_foo"
print_list_people(list0)


#shallow copy
list2 = list(list0)
list2[0].name = "new_new_foo"
print_list_people(list0)



list0 = [1, 2, 3, 4, 5]
list2 = list(list0)
list2.reverse()
print(list2)
list2 = list(list0)

for el in list2:
    print(el, end = " ")

print()

for i in range(len(list2)):
    print(list2[i], end = " ")

print()

for i , el in enumerate(list2):
    print(i, el, end = " ; ")

print()


list2 = ["foo", "pako", "edutilos"]
laenge = map(len, list2)
for el in laenge:
    print(el, end = " ")

print()


s = sum(range(0, 101))
print(s)

import re
def calculate_ttr(text_temp):
    # text_temp = "foo bar bim foo"
    pattern = "\.\s+|\.\n+|\,\s+|\;\s+|\?\s+|\?\n+|\:\s+|\:\n+|\s+"

    words = re.split(pattern, text_temp)
    types = []
    for word in words:
        if word not in types:
            types.append(word)
    ttr = len(types) / len(words)
    print("ttr = ", ttr)
    print(" ".join(sorted(types, key=str.lower)))


calculate_ttr(text1)
calculate_ttr(text2)
calculate_ttr(text3)



def calculate_ngramm(text , n):
    #sum = 0
    ngramms = []
    pattern = "\.\s+|\.\n+|\,\s+|\;\s+|\?\s+|\?\n+|\:\s+|\:\n+|\s+"
    words = re.split(pattern, text)
    for i in range(0, len(words)-n+1):
        l = []
        for j in range(0, n):
            l.append(words[j+i])
        ngramms.append(l)

    return ngramms

text_temp = "foo bar bim pako"
ngramms = calculate_ngramm(text_temp, 2)
print(ngramms)
ngramms = calculate_ngramm(text_temp, 3)
print(ngramms)
ngramms = calculate_ngramm(text_temp, 4)
print(ngramms)


ngramms = calculate_ngramm(text1, 2)
print(ngramms)
