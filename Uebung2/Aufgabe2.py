# Aufgabe 2
###############################

# Entwickeln Sie ein Programm, welches vom Nutzer eingegebene Woerter
# alphabetisch sortiert ausgibt. Der Ntzer soll dazu bis zu 5 Woerter
# eingeben koennen.

# Hinweis: Da wir bisher noch keine Listen behandelt haben, speichern
# Sie die Woerter in verschiedenen Variablen.


str1 = None
str2 = None
str3 = None
str4 = None
str5 = None

str1 = input("Gib den ersten String ein: ")

str2 = input("Gib den zweiten String ein: ")
if str2 < str1:
    str1 , str2 = str2 , str1

str3 = input("Gib den dritten String ein: ")
if str3 < str1:
    str1 , str3 = str3 , str1
if str3 < str2:
    str2, str3 = str3 , str2


str4 = input("Gib den vierten String ein: ")
if str4 < str1:
    str1 , str4 = str4, str1
if str4 < str2:
    str2 , str4 = str4, str2
if str4 < str3:
    str3, str4 = str4, str3


str5 = input("Gib den fuenften String ein: ")
if str5 < str1:
    str1, str5 = str5, str1
if str5 < str2:
    str2, str5 = str5, str2
if str5 < str3:
    str3, str5 = str5, str3
if str5 < str4:
    str4, str5 = str5, str4




print("Sortierte Strings: ", str1, str2, str3, str4, str5, sep = " ")