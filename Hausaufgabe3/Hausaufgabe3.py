'''
Hausaufgabe 3
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: ...



Abgabe bis zum 23.05.17 - 13:00h

Unten finden Sie drei Texte, die aus der Wikipedia (Simple English, English und Deutsch)
kopiert wurden. Alle Satzzeichen sind entfernt (das ' in "sheep's" kann als Buchstabe gezaehlt werden).

Hinweise zur Aufgabenstellung und Loesung:

1) Bitte beachten Sie bei Ihrer Loesung: Fuers Testen Ihrer Programme werden andere, aehnliche Texte verwendet,
die in den Variablen text1, text2, text3 gespeichert werden. Ihre Programme sollen immer auch
mit anderen Eingaben funktionieren (z.B. "text1="Eins", text2="Zwei", text3="Drei drei")

2) Wenn Sie andere Loesungen finden, die ohne for-Schleifen oder Listen arbeiten, koennen Sie
sie am Ende des Programms auskommentiert einfuegen. Sie werden nicht bewertet.
Sie koennen aber als Uebung versuchen, eine zusaetzliche Loesung zu finden,
die in einer Zeile die durchschnittliche Wortlaenge in einem Text berechnet.



AUFGABE:

a) Berechnen Sie zunaechst die durchschnittliche Wortlaenge. Verwenden Sie für jeden Text eine andere der drei Varianten fuer for-Schleifen ueber Listen, die in der Vorlesung (Foliensatz 4, S. 29-34) vorgestellt wurden.

b) Geben Sie die Zahl der Bigramme je Text aus

c) Vergleichen Sie die durchschnittliche Wortlaenge der drei Texte.

d) Geben Sie aus, welcher Text die groesste, zweitgroesste und drittegroesste Wortlaenge hat (und
zwar welche) und lassen Sie auf der Konsole jeweils die ersten drei Worte der Texte ausgeben
(denken Sie daran, dass fürs Testen andere Inhalte in die Variablen text1-text3 gesetzt werden!)
und das längste Wort aus dem jeweiligen Text.


  Beispiel zum Ausgabeformat (nicht mit korrekten Werten!):
  
  Bigramme: 12    18    7

  Groesste Wortlaenge (5.66): "The sheep Ovis..." - laengstes Wort: Artiodactyla
  Zweitgroesste Wortlaenge (5.32): "A domestic sheep..." - laengstes Wort: for
  Drittgroesste Wortlaenge (5.02): "Das Hausschaf Ovis..." - laengstes Wort: Lammfleisch




'''

text1 = """The sheep Ovis aries is a quadrupedal ruminant mammal typically kept as livestock
Like all ruminants sheep are members of the order Artiodactyla the even toed ungulates
Although the name sheep applies to many species in the genus Ovis in everyday usage it almost
always refers to Ovis aries Numbering a little over one billion domestic sheep are also the
most numerous species of sheep An adult female sheep is referred to as a ewe  an intact male as
a ram or occasionally a tup a castrated male as a wether and a younger sheep as a lamb Sheep
are most likely descended from the wild mouflon of Europe and Asia One of the earliest animals
to be domesticated for agricultural purposes sheep are raised for fleece meat lamb hogget or
mutton and milk A sheep's wool is the most widely used animal fiber and is usually harvested by
shearing Ovine meat is called lamb when from younger animals and mutton when from older ones
Sheep continue to be important for wool and meat today and are also occasionally raised for
pelts as dairy animals or as model organisms for science Sheep husbandry is practised throughout
the majority of the inhabited world and has been fundamental to many civilizations In the modern
era Australia New Zealand the southern and central South American nations and the British Isles
are most closely associated with sheep production Sheepraising has a large lexicon of unique terms
which vary considerably by region and dialect Use of the word sheep began in Middle English as a
derivation of the Old English word scēap it is both the singular and plural name for the animal
A group of sheep is called a flock herd or mob Many other specific terms for the various life
stages of sheep exist generally related to lambing shearing and age Being a key animal in the
history of farming sheep have a deeply entrenched place in human culture and find representation
in much modern language and symbology As livestock sheep are most often associated with pastoral
Arcadian imagery Sheep figure in many mythologies such as the Golden Fleece and major religions
especially the Abrahamic traditions In both ancient and modern religious ritual sheep are used
as sacrificial animals"""

text2= """
A domestic sheep Ovis aries is a domesticated mammal related to wild sheep and goats It is a
type of cattle and is owned and looked after by a sheep farmer Female sheep are called ewes
Male sheep are called rams Young sheep are called lambs
They are kept for their wool and their meat The wool of sheep after cleaning and treating
is used to make woollen clothes The meat of young sheep is called lamb and the meat from
adult sheep is called mutton Both are economically important products which have been used
since prehistoric times
Sheep are domesticated animals which have been bred by man There are breeds which
specialise in wool or meat The plural of sheep is just sheep
"""

text3= """
Das Hausschaf Ovis gmelini aries ist die domestizierte Form des Mufflons Es spielt in der
Geschichte der Menschheit eine bedeutende Rolle als Milch Lammfleisch beziehungsweise
Hammelfleisch Woll und Schaffelllieferant
"""

#########################
# Meine Loesungen       #
#########################
#a) durchschnittliche Wortlaenge
#text1
# Hier ich finde durchschnittliche Wortlaenge fuer den text1
# Zunaechst definiere ich sum_letters , und initiziere die mit 0 , diese Variable wird die gesamte Anzahl der Buchstaben enthalten
# Mit text1.split() , teile ich den text1 auf einzelne Woerte mit alle moeglichen Whitespaces als separator
# Mit for-Schleife iteriere ich die ganze Liste der Woerter und addiere die Laenge  des einzelnen Wortes auf sum_letters
# Und mit sum_letters/len(words) berechne ich die durchschnittliche Wortlaenge des text1
sum_letters = 0
words = text1.split()
for word in words:
    sum_letters += len(word)

average_word_length_1 = sum_letters/len(words)
#print("text1 = ", average_word_length_1)
############################################



#text2
# Hier ich finde durchschnittliche Wortlaenge fuer den text2
# Zunaechst definiere ich sum_letters , und initiziere die mit 0 , diese Variable wird die gesamte Anzahl der Buchstaben enthalten
# Mit text2.split() , teile ich den text2 auf einzelne Woerte mit alle moeglichen Whitespaces als separator
# Mit for-Schleife, zunaechst ich rufe range(len(words)) an , das wird eine Sequenz von 0 , 1 , ..., len(words)-1 erzeugen
# dann iteriere ich über diese Sequenz , in jedem Iterationschritt , wird i = 0 , ... , len(words)-1 sein , und dann mit words[i]
# greife ich die einzelnen Woerter zu und mit sum_letters += len(words[i]) addiere ich die Laenge des einzelnen Wortes auf sum_letters
# Und mit sum_letters/len(words) berechne ich die durchschnittliche Wortlaenge des text2
sum_letters = 0
words = text2.split()
for i in range(len(words)):
    sum_letters += len(words[i])
average_word_length_2 = sum_letters/len(words)
#print("text2 = ", average_word_length_2)
############################################################


#text3
# Hier ich finde durchschnittliche Wortlaenge fuer den text3
# Zunaechst definiere ich sum_letters , und initiziere die mit 0 , diese Variable wird die gesamte Anzahl der Buchstaben enthalten
# Mit text3.split() , teile ich den text1 auf einzelne Woerte mit alle moeglichen Whitespaces als separator
# Mit for-Schleife, zunaechst rufe ich enumerate(words) , damit ermoegliche ich Iteration mit Index und Element,
# dann mit sum_letters +=len(word) addiere ich die Laenge des einzelnen Wortes auf sum_letters
# Und mit sum_letters/len(words) berechne ich die durchschnittliche Wortlaenge des text3
sum_letters = 0
words = text3.split()
for i , word in enumerate(words):
    sum_letters += len(word)
average_word_length_3 = sum_letters/ len(words)
#print("text3 = ", average_word_length_3)
##############################################################

#b) Anzahl der Bigramme
# Es gibt zwei verschiedene Implementation der Bigramme
# 1) ein ohne dummy
# 2) anderes mit dummy
# Hier ich ziehe Implementation ohne dummy vor (Aber Sie koennten Aufgabestellung präzis formulieren.)
# Anzahl der Bigramme (ohne dummy) = Anzahl der Woerter - 1
# Anzahl der Bigramme (mit dummy) = Anzahl der Woerter + 1
#text1
# Mit words = text1.split() , teile ich text1 auf einzelne Woerter mit alle moeglichen whitespaces als Separator auf
# und weise ich das Ergebnis der Variable words zu.
# Mit mit count_bigramms_1 = len(words) -1 , bestimme ich die Anzahl der bigramme (len(words) gibt die Anzahl der Woerter
# zurueck)
words = text1.split()
count_bigramms_1 = len(words)-1
#text2
# Mit words = text2.split() , teile ich text2 auf einzelne Woerter mit alle moeglichen whitespaces als Separator auf
# und weise ich das Ergebnis der Variable words zu.
# Mit mit count_bigramms_2 = len(words) -1 , bestimme ich die Anzahl der bigramme (len(words) gibt die Anzahl der Woerter
# zurueck)
words = text2.split()
count_bigramms_2 = len(words)-1
#text3
# Mit words = text3.split() , teile ich text3 auf einzelne Woerter mit alle moeglichen whitespaces als Separator auf
# und weise ich das Ergebnis der Variable words zu.
# Mit mit count_bigramms_1 = len(words) -1 , bestimme ich die Anzahl der bigramme (len(words) gibt die Anzahl der Woerter
# zurueck)
words = text3.split()
count_bigramms_3 = len(words)-1
# print("Anzahl der Bigramme in text1 = " , count_bigramms_1)
# print("Anzahl der Bigramme in text2 = ", count_bigramms_2)
# print("Anzahl der Bigramme in text3 = ", count_bigramms_3)
##############################################################




#c) und d) die Vergleiche der durchschnittlichen Wortlaenge der Texte, und Ausgabe in die Konsole
# Hier finde ich das laengste Wort in text1
# largest_word_1 = "" , damit definiere ich die Variable und inizialisire die mit leerem String. Diese Variable wird
# das laengste Wort enthalten
# words = text1.split() , teile ich text1 auf einzelne Woerte auf .
# in for-Schleife iteriere ich über die einzelnen Woerter der words, und vergleiche die Laenge des Wortes mit der Laenge
# der largest_word_1 , wenn Worr ist groesser als largest_word_1 , dann weise ich dieses Wort der largest_word_1 zu.
largest_word_1 = ""
words = text1.split()
for word in words:
    if len(word)> len(largest_word_1):
        largest_word_1 = word
##############################################################

# Hier finde ich das laengste Wort in text2
# largest_word_2 = "" , damit definiere ich die Variable und inizialisire die mit leerem String. Diese Variable wird
# das laengste Wort enthalten
# words = text2.split() , teile ich text2 auf einzelne Woerte auf .
# in for-Schleife iteriere ich über die einzelnen Woerter der words, und vergleiche die Laenge des Wortes mit der Laenge
# der largest_word_2 , wenn Worr ist groesser als largest_word_2 , dann weise ich dieses Wort der largest_word_2 zu.
largest_word_2 = ""
words = text2.split()
for word in words:
    if len(word)> len(largest_word_2):
        largest_word_2 = word
##############################################################

# Hier finde ich das laengste Wort in text3
# largest_word_3 = "" , damit definiere ich die Variable und inizialisire die mit leerem String. Diese Variable wird
# das laengste Wort enthalten
# words = text3.split() , teile ich text3 auf einzelne Woerte auf .
# in for-Schleife iteriere ich über die einzelnen Woerter der words, und vergleiche die Laenge des Wortes mit der Laenge
# der largest_word_3 , wenn Worr ist groesser als largest_word_3 , dann weise ich dieses Wort der largest_word_3 zu.
largest_word_3 = ""
words = text3.split()
for word in words:
    if len(word) > len(largest_word_3):
        largest_word_3 = word
##############################################################




# Von diesem Zeitpunkt an , werde ich das Code nur fuer text1 erklaeren , dasselbe gilt auch fuer text2 und text3
# words = text1.split() -> hier teile ich text1 auf einzelne Woerte auf
# first_three_words_1 = words[0] +" " + words[1] + " " + words[2] + " ..."  -> hier konkatiniere ich das erste , zweite
# und dritte Wort der Liste words und " ..." string
# Dasselbe gilt fuer text2 und text3
words = text1.split()
first_three_words_1 = words[0] +" " + words[1] + " " + words[2] + " ..."
words = text2.split()
first_three_words_2 = words[0] +" " + words[1] + " " + words[2] + " ..."
words = text3.split()
first_three_words_3 = words[0] +" " + words[1] + " " + words[2] + " ..."
##############################################################



# Hier konstruiere ich str1, str2 ,und str3 um Ihre Ausgabeformat beizubehalten.
str1 = " durchschnittliche Wortlaenge ("+ str(average_word_length_1) + "): \"" + first_three_words_1 + "\" - laengstes Wort: "+ largest_word_1
str2 = " durchschnittliche Wortlaenge ("+ str(average_word_length_2) + "): \"" + first_three_words_2 + "\" - laengstes Wort: "+ largest_word_2
str3 = " durchschnittliche Wortlaenge ("+ str(average_word_length_3) + "): \"" + first_three_words_3 + "\" - laengstes Wort: "+ largest_word_3
##############################################################

# Hier konstruiere ich die Liste on-the-fly und sortiere ich die mit reverse=True
# Ich verwende diese umgekehrt-sortierte Liste um Vergleiche zwischen text1 , text2 und text3 einfach zu machen.
sorted_averages = sorted([average_word_length_1, average_word_length_2, average_word_length_3], reverse=True)


# Hier gebe ich Anzahl der Bigramme in bei Ihnen gewuenschten Format
print("Bigramme: ", count_bigramms_1, count_bigramms_2, count_bigramms_3)

# Hier vergleiche ich average_word_length der text1, text2 , text3
# da sorted_averages ist umgekehrt-sortierte Liste der 3 Elemente => das erste Element ist das groesste ,
# das zweite ELement ist das zweitegroesste , und das dritte Element ist das drittgroesste Element
# Und in jeder kompletten Verzweigung gebe ich str1 , str2 , str3 in der richtigen Reihenfolge aus.
if average_word_length_1 == sorted_averages[0]:
    str1 = "Groesste" + str1
    if average_word_length_2 == sorted_averages[1]:
        str2 = "Zweitgroesste" + str2
        str3 = "Drittgroesste" + str3
        print(str1,str2, str3, sep="\n")
    else:
        str3 = "Zweitgroesste" + str3
        str2 = "Drittgroesste" + str2
        print(str1, str3, str2, sep = "\n")
elif average_word_length_2 == sorted_averages[0]:
    str2 = "Groesste" + str2
    if average_word_length_1 == sorted_averages[1]:
        str1 = "Zweitgroesste" + str1
        str3 = "Drittgroesste" + str3
        print(str2, str1, str3, sep= "\n")
    else:
        str3 = "Zweitgroesste" + str3
        str1 = "Drittgroesste" + str1
        print(str2, str3, str1, sep="\n")
elif average_word_length_3 == sorted_averages[0]:
    str3 = "Groesste" + str3
    if average_word_length_2 == sorted_averages[1]:
        str2 = "Zweitgroesste" + str2
        str1 = "Drittgroesste" + str1
        print(str3, str2, str1, sep="\n")
    else:
        str1 = "Zweitgroesste" + str1
        str2 = "Drittgroesste" + str2
        print(str3, str1, str2, sep="\n")
##############################################################




#########################
# für Helena zum Testen #
#########################

# Ich schlage diese Probetexte für dich zum Testen vor:
text1= "dre dre dre dre schafe ei ei ei dre dre dre dre dre"
text2= "vier vier vier vie schafe vie vier vier vier vier"
text3 = "fuenf fuenf fuenf fuen schafe fuenf fuenf fuenf fuenf"


#Programm in haesslich zum Zahlentesten
texte = [text1.split(), text2.split(), text3.split()]
schnittlaenge = [0,0,0]
laengstes =["", "", ""]
erste_worte = ["", "", ""]

for i,text in enumerate(texte):
    print("Bigramme in Text "+str(i+1)+": "+str(len(text)-1))
    erste_worte[i] = " ".join(text[:3])
    schnittlaenge[i] = round(sum(map(len, text))/len(text),2)
    max_wort = ""
    for wort in text:
        if len(wort)>len(max_wort): max_wort=wort
    laengstes[i]=max_wort
print(schnittlaenge)
print(laengstes)
print(erste_worte)




