# Format = “Vorname Nachname: TT/MM/JJJJ: Geburtsort“
# Satz = „Der Proband wurde am TT/MM/JJJJ geboren.“
# Satz_neu = „Der.DET Proband.N wurde.VAFIN am.APPART TT/MM/JJJJ.CARD
# geboren.VVPP“

import re
user_input = input("Gib deinen Vornamen, Nachnamen , Geburtsdatum , und Geburtsort ein:\n").rstrip()
pattern = r"^[A-Z][a-z]+\s[A-Z][a-z]+:\s\d{2}\/\d{2}\/\d{4}:\s[A-Z][a-z]+$"
prog = re.compile(pattern)
if prog.match(user_input):
    splitted = user_input.split(" ")
    vorname = splitted[0]
    nachname = splitted[1]
    nachname = nachname[0:len(nachname)-1]
    gdatum = splitted[2]
    gdatum = gdatum[0:len(gdatum)-1]
    gort = splitted[3]
    print("Der Proband wurde am {0} geboren.".format(gdatum))
    print("Der.DET Proband.N wurde.VAFIN am.APPART {0}.CARD geboren.VVPP".format(gdatum))
else:
    print("Eingabe ist nicht korrekt.")

