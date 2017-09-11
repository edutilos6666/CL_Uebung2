# -*- coding: utf-8 -*-

'''Hausaufgabe 2
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: ...
NAME3 MATRIKELNUMMER: ...

Zwei allgemeine Hinweise, die fuer alle HAs gelten:
(Diese Hinweise werden zukuenftig nicht mehr extra aufgefuehrt,
gelten aber natuerlich fuer saemtliche HAs dieses Kurses.)

Hinweis: Sie sollen grundsaetzlich (d.h. bei allen HAs) fuer Ihre
Loesung ausschliesslich Datenstrukturen und Operatoren verwenden, die
wir schon im Kurs besprochen haben. Sie koennen _zusaetzlich_ am Ende Ihres
Programmes eine Loesung anfuegen, in denen Sie auch fortgeschrittene
Python-Konstrukte verwenden.

Hinweis: Die Aufgaben sind oft bewusst so gestellt, dass man sich
Gedanken dazu machen soll, wie man sie _sinnvoll_ loest. D.h. es gibt
meist etwas Spielraum, wie die Aufgaben zu interpretieren sind. Es
gibt aber (fast) immer nur eine sinnvolle Interpretation, wie die
Aufgabe zu loesen ist. Gegebenenfalls kommentieren Sie Ihre Loesung
entsprechend, wenn Sie z.B. verschiedene (sinnvolle)
Interpretationsmoeglichkeiten sehen, und entscheiden Sie sich fuer
Ihre Implementation fuer eine davon.
'''

"""
Haeufig muss man in der Computerlinguistik ein Korpus fuer die 
Weiterverarbeitung in ein anderes Format bringen.

Gegeben sei ein solches Korpus in folgendem Format:
Token1\tPOS1.Morphologie1\tLemma1\n
Token2\tPOS2.Morphologie2\tLemma2\n
mit einem Token pro Zeile und Leerzeilen als Satzgrenzenmarkierung.

Dieses Format soll in folgendes Format umgewandelt werden:
Token1/POS1/Lemma1/Morphologie1 Token2/POS2/Lemma2/Morphologie2 ...

D.h. die Annotationen (POS etc.) sind jetzt mit Schraegstrichen an 
das jeweilige Token angefuegt, zudem sind die POS- und 
Morphologie-Informationen getrennt.

Pro Zeile soll ein kompletter Satz stehen.
Hinweis: manche Lemmas heissen <unknown>, diese so uebernehmen.
"""

korpus = """Rund\tADJD.Pos\tRund
40\tCARD\t40
Prozent\tN.Reg.*2.*3.Neut\tProzent
aller\tPRO.Indef.Attr.-3.Gen.Pl.Neut\talle
staatlichen\tADJA.Pos.Gen.Pl.Neut\tstaatlich
Gelder\tN.Reg.Gen.Pl.Neut\tGeld
für\tAPPR.Acc\tfür
Verkehr\tN.Reg.Acc.Sg.Masc\tVerkehr
,\tSYM.Pun.Comma\t,
Gesundheit\tN.Reg.Acc.Sg.Fem\tGesundheit
und\tCONJ.Coord.-2\tund
Soziales\tN.Reg.Acc.Sg.Neut\tSoziale
würden\tVFIN.Aux.3.Pl.Past.Subj\twerden
unterschlagen\tVPP.Full.Psp\tunterschlagen
.\tSYM.Pun.Sent\t.

Die\tART.Def.Nom.Pl.Masc\tdie
dadurch\tPROADV.Dem\tdadurch
verursachten\tADJA.Pos.Nom.Pl.Masc\tverursacht
Schäden\tN.Reg.Nom.Pl.Masc\tSchaden
beliefen\tVFIN.Full.3.Pl.Past.Ind\tbelaufen
sich\tPRO.Refl.Subst.3.Acc.Pl.*6\tsie
auf\tAPPR.Auf\tauf
rund\tADJD.Pos\trund
20\tCARD\t20
Milliarden\tN.Reg.Acc.Pl.Fem\tMilliarde
Dollar\tN.Reg.*2.*3.Masc\tDollar
im\tAPPRART.Dat.Sg.Neut\tin
Jahr\tN.Reg.Dat.Sg.Neut\tJahr
.\tSYM.Pun.Sent\t.

Ein\tART.Indef.Nom.Sg.Masc\teine
Teil\tN.Reg.Nom.Sg.Masc\tTeil
der\tART.Def.Gen.Pl.Neut\tdie
unterschlagenen\tADJA.Pos.Gen.Pl.Neut\tunterschlagen
Gelder\tN.Reg.Gen.Pl.Neut\tGeld
werde\tVFIN.Aux.3.Sg.Pres.Subj\twerden
von\tAPPR.Dat\tvon
der\tART.Def.Dat.Sg.Fem\tdie
Verwaltungsmafia\tN.Reg.Dat.Sg.Fem\t<unknown>
ins\tAPPRART.Acc.Sg.Neut\tin
Ausland\tN.Reg.Acc.Sg.Neut\tAusland
weitergeleitet\tVPP.Full.Psp\tweitergeleiten|weiterleiten
.\tSYM.Pun.Sent\t."""


#split korpus into lines
splitted = korpus.split("\n\n")
#result will contain modified line-s from splitted list
result = []
#iterate over each line
for line in splitted:
    #split each line into its members
    members  = line.split("\n")
    #new_members will contain modified member-s from members list
    new_members = [];
    #iterate over each member
    for member in members:
        #split each member into its parts , by using '\t' as delimiter , my purpose is to replace all '.' with '/' betweeen '\t'
        parts = member.split("\t")
        #in part2 all '.' will be replaced with '/'
        part2 = parts[1] 
        part2 = part2.replace(".", "/")
        #parts have 3 elements , combine them by using '/' as delimiter
        new_member = parts[0] + "/" + part2 + "/" + parts[2]
        #append new_member into new_members
        new_members.append(new_member);
    #join new_members list by using ' ' as delimiter and append the joined string into result list
    result.append(" ".join(new_members));

#join result list by using '\n' as delimiter and print the joined string into console
print("\n".join(result))
