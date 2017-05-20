###############################
# Aufgabe 1
###############################

# Entwickeln Sie ein Programm, welches vom Nutzer eingegebene Woerter
# alphabetisch sortiert ausgibt. Der Nutzer soll dazu bis zu 5 Woerter
# eingeben koennen. Verwenden Sie keine builtin-Sortierfunktionen.


# list.sort()
names = ["e", "d" , "c", "b", "a"]
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names);


def insertion_sort(names):
    i , j = 0, 0
    while (i < len(names)-1):
        j = i +1
        while(j < len(names)):
            if(names[j] < names[i]):
                names[j], names[i] = names[i], names[j]
            j = j +1

        i = i +1

names = ["e", "d" , "c", "b", "a"]
insertion_sort(names)
print(names)



def selection_sort(names):
    i = 0
    while(i < len(names)-1 ):
        min_el = names[i]
        min_index = i
        j = i +1
        while(j < len(names)):
            if(names[j] < names[i]):
                min_el = names[j]
                min_index = j
            j = j +1

        if(min_index != i):
            names[i], names[min_index] = names[min_index], names[i]

        i = i +1


names = ["e", "d" , "c", "b", "a"]
selection_sort(names)
print(names)



def bubble_sort(names):
    pass

# words = []
# while len(words) < 5:
#     words.append(input("Insert word: "))
#
#
# insertion_sort(words)
# print(words)
    






###################################################
# Aufgabe 2
###################################################

# Aufgabe 2.1
# Berechnen Sie die durchschnittliche Wortlaenge des folgenden Texts
# auf 2 Nachkommastellen genau. Geben Sie ausserdem die Anzahl der
# Satzzeichen im Text aus.
# Benutzen Sie fuer Ihre Loesung eine Liste.

text = """Daß ich es nicht lassen kann, bei offenem Fenster zu
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


splitted = text.split(" ")
# for str in splitted:
#     print(str)

anzahl_woerter  = len(splitted)
print("anzahl_woerter = ", anzahl_woerter)

anzahl_puenkt = text.count(".")
anzahl_komma = text.count(",")
anzahl_doppelpuenkt = text.count(":")
anzahl_fragezeichen = text.count("?")
anzahl_ausrufezeichen = text.count("!")
anzahl_semikolon = text.count(";")
anzahl_anfuehrungszeichen = text.count("\"")
anzahl_leerzeichen = text.count(" ")
anzahl_bindestrich = text.count("-")
anzahl_apostroph = text.count("'")

anzahl_satzzeichen = anzahl_puenkt + anzahl_komma + anzahl_doppelpuenkt + anzahl_fragezeichen + anzahl_ausrufezeichen +\
                    anzahl_semikolon + anzahl_anfuehrungszeichen + anzahl_leerzeichen + anzahl_bindestrich + anzahl_apostroph


print("Anzahl der Satzzeichen = ", anzahl_satzzeichen)



# Aufgabe 2.2
# Geben Sie alle grossgeschriebenen Woerter aus (1 Wort pro Zeile)

# print(text)
splitted = text.split("\n")

# for line in splitted:
#     print(line)


capitalized_words = []
for line in splitted:
    semiwords = line.split(" ")
    found = False
    for word in semiwords:
        if(found == True): break
        if word[0].isupper():
            found = True
            word = word.strip()
            word = word.strip(",")
            word = word.strip(".")
            word = word.strip(":")
            word = word.strip("\"")
            word = word.strip("'")
            word = word.strip(";")
            word = word.strip("?")
            word = word.strip("!")
            capitalized_words.append(word)


print("capitalized words for each line = ", capitalized_words, sep="\n")

###################################################
# Aufgabe 3
###################################################

# Schreiben Sie ein Programm, welches die Frequenzen zweier vom Nutzer
# bestimmten Woerter in einem Korpus miteinander vergleicht Geben Sie
# an, welches Wort haeufiger vorkommt.  Geben Sie auch die
# Einzelfrequenzen aus.


korpus = """Daß ich es nicht lassen kann, bei offenem Fenster zu
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

# str1 = input("das erste  Wort: ")
# str2 = input("das zewite Wort: ")
# count_str1 = korpus.count(str1)
# count_str2 = korpus.count(str2)
# print("count str1 = ", count_str1)
# print("count str2 = ", count_str2)
# if count_str1 > count_str2:
#     print(str1 , "kommt hauefiger vor.")
# elif count_str1 < count_str2:
#     print(str2 , "kommt haeufiger vor.")
# else:
#     print(str1 , " und ", str2 , "kommen gleich haeufig vor.")



###################################################
# Aufgabe 4
###################################################

# Generieren Sie mithilfe der Methode random.randint() zunaechst
# eine Zahl zwischen 0 und 1.000.000.
# Berechnen Sie dann
# (i) die (einfache) Quersumme
# (ii) die interierte, einstellige Quersumme (d.h. Sie berechnen
# so lange die Quersumme der Quersumme, bis sie einstellig ist).
import random 
lower_bound = 0 
upper_bound = 1000000

random_number = random.randint(lower_bound, upper_bound)
temp_number = random_number
quersumme = 0 
while temp_number > 0 : 
    digit = temp_number % 10 
    temp_number = temp_number // 10
    quersumme = quersumme + digit
    
print("Quersummer der ", random_number , "ist ", quersumme)


temp_number = random_number
quersumme_temp = 0
while quersumme >= 10 :
    temp = quersumme
    quersumme_temp = 0
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        quersumme_temp = quersumme_temp + digit
    quersumme = quersumme_temp
print("interierte Quersumme = ", quersumme)




