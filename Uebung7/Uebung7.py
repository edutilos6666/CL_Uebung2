#Schreiben Sie ein Programm, das aus folgendem Text alle Adverbien
#herausfiltert und sie in einer Liste abspeichert.
text = """He quickly reads a book.
Mandy is a pretty girl.
The class is terribly loud today.
Max is a good singer.
You can easily open this tin.
It's a terrible day today.
She sings the song well.
He is a careful driver.
He drives the car carefully.
The dog barks loudly.
The bus driver was seriously injured.
Kevin is extremely clever.
This hamburger tastes awful.
Be careful with this glass of milk. It's hot.
Robin looks sad. What's the matter with him?
Jack is terribly upset about losing his keys.
This steak smells good.
Our basketball team played badly last Friday.
Don't speak so fast. I can't understand you.
Maria slowly opened her present."""
import re
adverbs = []
pattern = r"\w*ly"
prog = re.compile(pattern)
l = prog.findall(text)
# i only miss fast
print(l)


#Schreiben Sie ein Programm, das folgendem String alle Geburtstage entnimmt
#und Sie in einer Datenstruktur kombiniert mit dem jeweiligen Geburtstagskind abspeichert.
#Wählen Sie dazu eine geeignete Datenstruktur.


birthday = """Peter --> 01/02/03
Sebastian --> 02/04/90
Sarah --> 11.06.91
Petra --> 07/08/11
Tomas --> 01.08.1994
Markus --> 09.03.80
Silke --> 21/12/1970"""

pattern = "\n"
prog = re.compile(pattern)
lines = prog.split(birthday)
children = {}
prog = re.compile(" --> ")
for line in lines:
    splitted = prog.split(line)
    children[splitted[0]] = splitted[1]


print("<<birthdays>>")
for name, age in children.items():
    print(name , ": ", age)


#Dem Verfasser des folgenden Textes ist ein Fehler unterlaufen.
#Ersetzen Sie alle Vorkommen von „Back“ durch “Bach“. Verwenden Sie dazu einen regulären Ausdruck.


bach = """Johann Sebastian Back war Musiker und Komponist. Auch heute noch ist er einer der wichtigsten Komponisten in der Geschichte der Musik.
Seine Stücke für das Klavier, die Orgel, die Flöte, Gesang und das Orchester werden oft gespielt.
Er wurde im Jahr 1685 in Eisenach in Thüringen geboren und steht für den Stil des Barock.
Back kam aus einer musikalischen Familie und lernte die Musik vom Vater und einem älteren Bruder.
Das Komponieren, also Schreiben von Musikstücken, brachte er sich selbst bei. Mit 17 Jahren arbeitete er schon als Orgel-Spieler.
Als er fast 40 war, wurde er Thomaskantor. Das heißt, er leitete den Chor der Thomaskirche in Leipzig in Sachsen.
Die Kirche und ihre Thomasschule gibt es auch heute noch. Hier arbeitete Bach bis zu seinem Lebensende.
Im Gegensatz zu seinen Söhnen Wilhelm Friedemann und Carl Philipp Emmanuel war Johann Sebastian Back eher etwas für Musik-Kenner.
Nach seinem Tod im Jahre 1750 wurde er bald vergessen. Es dauerte fast 100 Jahre, bis man Backs Werke wiederentdeckte.
Was für Musik machte Back?
Johann Sebastian Back interessierte sich für allerlei Arten von Musik und hatte Respekt für andere Musiker.
Mit Instrumenten kannte er sich gut aus. Er wusste auch von den Ideen, die hinter der Musik stecken.
Besonders gut konnte Bach Orgel spielen. Wenn man ihm eine Melodie vorgesungen hat, konnte er sie sofort mit bis zu acht Stimmen auf der Orgel nachspielen.
Ein berühmtes Stück Bachs ist „Das Wohltemperierte Klavier“, das zeigen soll, was man alles aus den Tasten herausholen kann.
Noch berühmter sind die großen Werke für Orchester und Chöre: Das „Weihnachtsoratorium“ wird zu Weihnachten gespielt und erzählt von der Geburt von Jesus Christus."""


pattern = "Back"
prog = re.compile(pattern)
res = prog.sub("Bach", bach)
print(res)
