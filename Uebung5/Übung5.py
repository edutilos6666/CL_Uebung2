"""
1) Geben Sie mit einem direktem Zuriff auf die Elemente und einem eigenen Iterator
 jeweils das zweite bis vierte Element von r=range(10,20) aus
"""
r = range(10, 20)
it = iter(r)
it.__next__()
elem_2 = it.__next__()
it.__next__()
elem_4 = it.__next__()

print("das zweite Element = ", elem_2)
print("das vierte Element = ", elem_4)

"""
2) Schreibe ein Programm zu folgendem Kommentar (und ergänze sinnvollen
    Kommentar wo nötig). Nutze dabei an der mit * markierten Stelle
    Listen-Abstraktion"""

print()
print("<<Teil 2>>")
# Menge aller Ziffern-Char
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

# Textdatei vorlage.txt oeffnen und verarbeiten
filename = "vorlage.txt"
f = open(filename)

# Gib alle Woerter einer Zeile, die mit einer Ziffer beginnen aus
   # Fuer jede Zeile der Datei
lines = []
for line in f:
   if line[0].isnumeric():
      lines.append(line.strip())

for line in lines:
   print(line)
print()
       # Teile die Zeile in Worte
words = []
for line in lines:
   words.extend(line.split())

       # * Für jedes Wort: Speichere das Wort in Reserveliste,
       #  wenn das Wort mit einer Ziffer beginnt
reserve_liste = [word for word in words if word[0].isnumeric()]
       # Gib Reserveliste numerisch sortiert aus
reserve_liste.sort()
for word in reserve_liste:
   print(word)


# Gib die Datei Zeilenweise unverändert aus
print()
f.close()
with open(filename) as f:
   for line in f:
      print(line.strip())

""" 3) Kommentiere folgendes Programm und ändere die Variablen in sprechende
Namen: """
print()
print("<<Teil 3>>")
vowels = {'a', 'e', 'i', 'o', 'u'}
result = []
with open('datei.txt') as f:
   result.append([line.split()[1] for line in f if line.split()[2][0]
in vowels])
   print(result.append(sorted(list(vowels))[0]))
print(result)
