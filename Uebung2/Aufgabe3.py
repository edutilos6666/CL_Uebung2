###############################
# Aufgabe 3
###############################


# Aufgabe 3.1
# Formatieren Sie den gegebenen Text so um, dass jeder Satz auf einer
# eigenen Zeile steht. Nehmen Sie dabei an, dass Saetze durch einen
# abschliessenden Punkt markiert sind. Ein Satz sollte dabei auch nicht
# auf mehrere Zeilen aufgeteilt werden.

# Aufgabe 3.2
# Wandeln Sie den Text in Kleinbuchstaben um, zaehlen Sie, wie haeufig
# die verschiedenen Vokale (a,e,i,o,u) vorkommen und geben Sie das
# Ergebnis aus.

# Aufgabe 3.3
# Geben Sie aus, ob der Buchstabe 'a' haeufiger vorkommt als 'o' oder
# umgekehrt oder ob beide Vokale gleich haeufig sind.

text1 = """Wegen des Ukraine-Konflikts genehmigt die Bundesregierung derzeit
keine Ausfuhr von Rüstungsgütern nach Russland. Betroffen sind
Handfeuerwaffen, Munition oder Torpedos."""


# Teil 1
text1 = text1.replace("\n", " ")
text1 = text1.replace(". ", ".\n")
print(text1)


# Teil 2
text1 = text1.lower()
#(a,e,i,o,u)
count_a = text1.count("a")
count_e = text1.count("e")
count_i = text1.count("i")
count_o = text1.count("o")
count_u = text1.count("u")

print("# [a e i o u] = ", count_a, count_e, count_i, count_o, count_u)



# Teil 3
if count_a  > count_o:
    print("a kommt haeufiger als o vor.")
elif count_a < count_o:
    print("o kommt haeufiger als a vor.")
else:
    print("a und o kommon gleich haeufig vor.")
    