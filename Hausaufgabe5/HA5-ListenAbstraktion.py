'''
Hausaufgabe 5
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: Mike Josaf 108014224341
'''

'''
1 

Schreiben Sie ein Programm, dass eine Textdatei oeffnet und - wenn vorhanden - die 42. Zeile ausgibt.
Implementieren Sie zwei Varianten:
a) Mit for-Schleife nach Wahl
b) mit einem eigenen Iterator
'''
print("<<Teil 1>>")
# a)
# i wird als Inkrement benutzt , um die Anzahl der gelesenen Zeilen zu verfolgen.
i = 1

# Die Datei namens "part1.txt" wird fuers Lesen geoeffnet.
# Der Ausdruck - with behandelt das Schliessen der geoeffneten Datei automatisch.
filename = "part1.txt"
f = open(filename)
with open(filename) as f:
    # Die geoffnete Datei wird Zeile fuer Zeile gelesen.
    # Wenn Zeile 42 gelesen wird (i == 42) , wird diese Zeiel ausgegeben.
    # Und i wird in jedem Iterationsschritt um eins erhoeht.
    for line in f:
        if i == 42:
            print(line)
        i += 1


# b)
# i wird als Inkrement benutzt , um die Anzahl der gelesenen Zeilen zu verfolgen.
i = 1
# Die Datei namens "part1.txt" wird fuers Lesen geoeffnet.
with open(filename) as f:
    # Iterator namens file_it wird aus Datei Deskriptor - f erstellt.
    file_it = iter(f)
    # In dieser while-Schleife wird next(iterator) aufgerufen und wenn das Iterator 42 mal aufgerufen
    # wird , wird diese Zeile ausgegeben.
    # In jedem Iterationsschritt wird i um eins erhoeht.
    # Bemerkung: Als Exception Handling noch nicht in der Vorlesung behandelt worden ist , wird das
    # hier verzichtet. Aber wenn die Datei weniger als 42 Zeile enthaelt wird StopIteration Exception
    # geworfen.
    while True:
        line = next(file_it)
        if i == 42:
            print(line)
            break
        i += 1



'''
2

Schreiben Sie ein Programm zu folgendem Kommentar. Nutzen Sie dabei an der mit * markierten Stelle Listen-Abstraktion
'''
print("<<Teil 2>>")
# Textdatei vorlage.txt oeffnen und verarbeiten
filename = "vorlage.txt"
f = open(filename)

# Gib alle Woerter einer Zeile, deren dritter Buchstabe ein Vokal ist
# umgekehrt sortiert aus
# Fuer jede Zeile der Datei
lines = []
vowels = ["a", "e", "i", "o", "u", "ä", "ö", "ü"]
for line in f:
    third_letter = line[2]
    if third_letter in vowels:
        lines.append(line.strip())

f.close()

lines.sort(reverse=True)
for line in lines:
    print(line)






# Teile die Zeile in Worte
words = []
for line in lines:
    words.extend(line.split())


# * Fuer jedes Wort: Speichere das Wort in Reserveliste,
# wenn der dritte Buchstabe ein Vokal ist
reserve_liste = []
for word in words:
    if(len(word) < 3): continue
    third_letter = word[2]
    if third_letter in vowels:
        reserve_liste.append(word)



# Gib Reserveliste rueckwaerts alphabetisch sortiert aus
reserve_liste = sorted(reserve_liste, reverse=True)
for word in reserve_liste:
    print(word)


print()
# Gib die Datei Zeilenweise unveraendert aus
f = open(filename)
for line in f:
    print(line)




'''
3
Kommentieren Sie folgendes Programm und aendern Sie die Variablennamen in
sprechende Namen:

'''
print()
print("<<Teil 3>>")
# 0 and 5 werden als string in s_random_numbers set gespeichert.
s_random_numbers = {'0', '5'}

# Sequenz von 0 bis 10(ausschliesslich) werden iteriert und mit jedem Element dieser Sequenz
# wird neue Zahl erstellt.
# Diese Zahl wird als string in s_random_numbers gespeichert.
for z in range(0,10):
    s_random_numbers.add(str(int(5*z/35*(4+3))))

# third_words wird eine Liste als einziges Element enthalten. Dieses eniziges Element wird
# das dritte Wort  aller Zeilen von datei.txt enthalten ,
# dessen erste Wort in s_random_numbers vorhanden ist.
third_words = []

# Die Datei "datei.txt" wird fuers Lesen geoeffnet und mit "with" wird die geoffnete Datei
# automatisch geschlossen.
# Innerhalb print() wird list-comprehension benutzt . f wird Zeile fuer Zeile ueberprueft ,
# und wenn das erste Wort der Zeile in s_random_numbers vorhanden ist ,
# wird das dritte Wort der Zeile via list-comprehension
# zwischengespeichert und die Ergebnisliste wird in third_words hinzugefuegt.

with open('datei.txt') as f:
    # Bemerkung: Es waere besser , .extend() , statt .append() zu benutzen. Das macht keinen Sinn ,
    # Liste der Liste fuer ein einziges Element zu erstellen.
    print(sorted(str(third_words.append([x.split()[2] for x in f if x.split()[0]
in s_random_numbers]))))
print("third_words als Liste der Liste : ", third_words)



'''
4
# Nutzen Sie eine Datei '5_text.txt'
# Lesen Sie die Datei ein und tokenisieren Sie den Text
# unter der vereinfachenden Annahme, dass alle Wort-initialen
# und -finalen Sonderzeichen ein eigenes Token darstellen.

# Speichern Sie die Tokens in einer geeigneten Datenstruktur ab.

# Schreiben Sie schliesslich alle Woerter, die einen
# Grossbuchstaben enthalten, alphabetisch sortiert
# in eine Datei namens '4_capitalized.txt' im gleichen
# Verzeichnis,
# im Format 1 Wort pro Zeile.
'''
print()
print("<<Teil 4>>")
# capitalized_words Liste wird alle Woerter enthalten , das zumindestens einen großen Buchstaben hat.
capitalized_words = []

# Datei namens "5_text.txt" fuers Lesen wird geoeffnet
filename="5_text.txt"
with open(filename) as f:
    # Die Datei wird Zeile fuer Zeile gelesen.
    for line in f:
        # Jede Zeile wird mit split() auf einzelne Woerter aufgesplittet.
        words = line.split()
        # words Liste wird iteriert
        for word in words:
            # Jedes Wort (als String) wird iteriert.
            # Wenn der Buchstabe Grossbuchstabe ist , dann wird das Wort - word in capitalized_words
            # hinzugefuegt, und innere Schleife wird abgebrochen.
            for letter in word:
                if letter.isupper():
                    capitalized_words.append(word)
                    break


# capitalized_words wird sortiert.
capitalized_words.sort()

# Die Datei namens "4_capitalized.txt" wird fuers  Schreiben geoeffnet und alle Woerter aus
# capitalized_words werden in diese Datei geschrieben.
# 1 Wort pro Zeile.
filename = "4_capitalized.txt"
with open(filename, mode="w") as f:
    for word in capitalized_words:
        f.write(word+"\n")

