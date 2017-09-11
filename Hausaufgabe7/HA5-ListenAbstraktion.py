'''
1 

Schreiben Sie ein Programm, dass eine Textdatei oeffnet und - wenn vorhanden - die 42. Zeile ausgibt.
Implementieren Sie zwei Varianten:
a) Mit for-Schleife nach Wahl
b) mit einem eigenen Iterator
'''


'''
2

Schreiben Sie ein Programm zu folgendem Kommentar. Nutzen Sie dabei an der mit * markierten Stelle Listen-Abstraktion
'''

# Textdatei vorlage.txt oeffnen und verarbeiten

# Gib alle Woerter einer Zeile, deren dritter Buchstabe ein Vokal ist
# umgekehrt sortiert aus
# Fuer jede Zeile der Datei






# Teile die Zeile in Worte





# * Fuer jedes Wort: Speichere das Wort in Reserveliste,
# wenn der dritte Buchstabe ein Vokal ist




# Gib Reserveliste rueckwaerts alphabetisch sortiert aus




# Gib die Datei Zeilenweise unveraendert aus





'''
3
Kommentieren Sie folgendes Programm und aendern Sie die Variablennamen in
sprechende Namen:

'''
zlvf = {'0', '5'}
for z in range(0,10):
    zlvf.add(str(int(5*z/35*(4+3))))
krell = []
with open('datei.txt') as f:
    print(sorted(str(krell.append([x.split()[2] for x in f if x.split()[0]
in zlvf]))))
print("Krell:", krell)

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