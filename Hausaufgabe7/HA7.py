'''
Hausaufgabe 7
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: Mike Josaf 108014224341
'''

'''
1

Schreiben Sie die Programm-Stücke aus den Teilaufgaben 2, 3 und 4
der 5. Hausaufgabe mit regulären Ausdrücken und ohne Listenabstraktionen.
(Sie können dafür bei Teilaufgabe 2 die Kommentarvorgabe ignorieren oder
nur an einigen Stellen ersetzen)
Achten Sie darauf, dass die Ein- und Ausgabe identisch zu der Lösung
von Hausaufgabe 5 (wie in der Übung besprochen und in der Korrektur
angegeben) sein soll.

'''


'''
5.2

Schreiben Sie ein Programm zu folgendem Kommentar. Nutzen Sie dabei an der mit * markierten Stelle Listen-Abstraktion
'''
import re
# Textdatei vorlage.txt oeffnen und verarbeiten
filename = 'vorlage.txt'
infile =  open(filename)

# Gib alle Woerter einer Zeile, deren dritter Buchstabe ein Vokal ist
# umgekehrt sortiert aus
# Fuer jede Zeile der Datei
# Die gefundene Woerter werden in words speichert
words = []
# pattern match-et alle Woerter, deren dritter Buchstabe ein Vokal ist.
pattern = "^\w{2}[aeiouyäöüAEIOUYÄÖÜY]\w*$"
prog = re.compile(pattern)
for line in infile:
    # Teile die Zeile in Worte
    splitted = line.split()
    for token in splitted:
        # * Fuer jedes Wort: Speichere das Wort in Reserveliste,
        # wenn der dritte Buchstabe ein Vokal ist
        if prog.search(token):
            words.append(token)
# Gib Reserveliste rueckwaerts alphabetisch sortiert aus
words.sort(reverse=True)
print("<<umgekehrt sortierte Liste>>")
for word in words:
    print(word)

# Datei wird geschlossen.
infile.close()

# Gib die Datei Zeilenweise unveraendert aus
print("\n<<Inhalt der Datei>>")
with open(filename) as infile:
    for line in infile:
        print(line, end='')









'''
5.3
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
with open('datei.txt') as infile:

    # pattern = ^(9|7|0|5|1|8|6|4|2|3)\s+  wird konstruiert.
    pattern = "^("
    for number in s_random_numbers:
        pattern += str(number) + "|"
    pattern = pattern[0:len(pattern)-1] + ")\s+"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern)

    # infile wird Zeile fuer Zeile gelesen
    for line in infile:
        # Wenn pattern zutrifft , wird das dritte Wort der Zeile in die third_words hinzugefuegt.
        if prog.search(line):
            third_words.append(line.split()[2])

# third_words wird ausgegeben.
print("third_words als Liste der Liste : ", third_words)
print()







'''
5.4
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

# Name der Eingabedatei
infile_name = '5_text.txt'
# Name der Ausgabedatei
outfile_name = '4_capitalized.txt'
# Die gefundene Woerter (die Woerter , die einen Grossbuchstaben haben) werden  in capitalized_words gespeichert.
capitalized_words = []
# Alle tokens werden in token_list gespeichert.
token_list = []
# Infile wird fuers Lesen geoeffnet.
with open(infile_name) as infile:
    # (\W+) bedeutet non-word Charakter , alle Zeichen ausser : [a-zA-Z0-9-] und () sichert , dass
    #  non-word Charakter auch als token betrachtet wird.
    pattern = "(\W+)"
    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern)
    # infile wird Zeile fuer Zeile gelesen.
    for line in infile:
        # line wird gesplitted und der splitted zugewiesen
        splitted = prog.split(line)
        # splitted wird iteriert
        for token in splitted:
            # fuehrende und schliessende whitespace-s werden aus token entfernt
            token = token.strip()
            # Wenn token ein empty string ist , wird es ignoriert.
            if token == '':continue
            # sonst token wird in die token_list hinzugefuegt.
            token_list.append(token)





# pattern matches die Woerter , die aus \w (alpha-numerischen) Zeichen bestehen , und deren nur einiziger Buchstabe gross ist.
# Bemerkung: pattern fuer die Woerter mit mehr als oder gleich 1 Grossbuchstaben:
# pattern = "^[a-z0-9-]*[A-Z]+[a-z0-9-]*$"
pattern = "^[a-z0-9-]*[A-Z][a-z0-9-]*$"
# pattern wird kompiliert und in prog gespeichert.
prog = re.compile(pattern)
# token_list wird iteriert.
for token in token_list:
    # wenn prog zutrifft , token wird in capitalized_words hinzugefuegt
    if prog.search(token):
        capitalized_words.append(token)


# capitalized_words wird aufsteigend sortiert
capitalized_words.sort()
# outfile wird fuers Schreiben geoffnet
with open(outfile_name, "w") as outfile:
    # capitalized_words wird iteriert
    for word in capitalized_words:
        # word wird in outfile geschrieben.
        outfile.write(word +"\n")



'''
2

a) Schreiben Sie ein kurzes Programm, das eine Datei mit einem deutschen
Beispieltext einliest und zwei Listen ausgibt:
Eine mit allen Nomen, eine mit allen Adjektiven aus dem Text.

Achtung: Sie werden kein 100 %iges Ergebnis für alle möglichen Eingaben
erhalten. Es geht bei dieser Aufgabe darum, durch linguistisch sinnvolle
Kriterien ein möglichst gutes Ergebnis zu erzielen.

b) Testen Sie Ihr Programm an folgendem Text:
"In den vergangenen Jahren haben wir uns mit vielen, schönen und bunten
Themen beschäftigen können. Wir haben unterschiedliche Kriterien anwenden
können und mit Begeisterung am 27.06.2017 den 364. König krönen können.
Begeistert waren auch die bunt gekleideten Besucher, die sich gerne zeigten.
Gewiss, ich schreibe diesen Bericht der Ordnung zuliebe nieder, aus einer
gewissen Pedanterie heraus, damit er zu den Akten komme. Ich will mich
zwingen, noch einmal die Ereignisse zu überprüfen, die zum Freispruch
eines Mörders und zum Tode eines Unschuldigen geführt haben. (Er meint
mehr als zwei Unschulde, aber hier zählen nur reiche, alte Herren.)
"

Vergleichen Sie die Zahl der richtig zugeordneten Nomen/Adjektive mit denen,
die Sie per Hand im Text finden können.
Kommentieren Sie beide Ergebnisse in jeweils 2-3 Sätzen.
'''

# clear_artikel
# Entfernen der Artikel aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_artikel(input_list):
    # Liste der Artikel
    artikel_list = ['ein', 'eines', 'einem', 'einen',
                    'eine', 'einer',
                    'der', 'des', 'dem', 'den',
                    'die', 'das']

    # pattern = ^(ein|eines|einem|einen|eine|einer|der|des|dem|den|die|das)$
    pattern = r"^("
    for artikel in artikel_list:
        pattern += artikel+ "|"
    pattern = pattern[0:len(pattern)-1] +")$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern, re.IGNORECASE)

    # Rueckgabewert : Liste
    res = []

    # input_list wird iteriert
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if prog.search(token):
            continue
        # sonst token wird in res hinzugefuegt
        else:
            res.append(token)

    # res wird zurueckgegeben.
    return res



# clear_pronomen
# Entfernen der Pronomen aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_pronomen(input_list):
    # Liste der Pronomen
    pronomen_list = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie",
                     "mein", "dein", "sein", "ihr", "unser", "euer",
                     "mich", "dich", "sich", "uns", "euch",
                     "jemand", "alle", "einer", "manche", "man", "wer", "etwas",
                     "einige", "andere",
                     "keiner", "nimeand", "nichts",
                     "der", "die", "das", "dieser", "diese", "dieses", "jener",
                     "jene", "jenes", "derjenige", "diejenige", "dasjenige",
                     "derselbe", "dieselbe", "dasselbe",
                     "wer", "was", "wessen", "welcher",
                     "deren", "einander",
                     "meine", "deine", "seine", "ihre", "unsere", "eure",
                     "jemandem", "jemander", "jemandes",
                     "desjenigen", "demjenigen", "denjenigen",
                     "derjenigen",
                     "desselben", "demselben",
                     "diese(?:r|n|m|s)?"]

    # pattern = ^(ich|du|er|sie|es|wir|ihr|sie|mein|dein|sein|ihr|unser|euer|mich|
    # dich|sich|uns|euch|jemand|alle|einer|manche|man|wer|etwas|einige|andere|keiner|
    # nimeand|nichts|der|die|das|dieser|diese|dieses|jener|jene|jenes|derjenige|diejenige|
    # dasjenige|derselbe|dieselbe|dasselbe|wer|was|wessen|welcher|deren|einander|meine|deine|
    # seine|ihre|unsere|eure|jemandem|jemander|jemandes|desjenigen|demjenigen|denjenigen|derjenigen|
    # desselben|demselben|diese(?:r|n|m|s)?)$
    pattern = r"^("
    for pronomen in pronomen_list:
        pattern += pronomen + "|"

    pattern = pattern[0:len(pattern)-1] +")$"


    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern,re.IGNORECASE)

    # Rueckgabewert: Liste
    ret = []


    # input_list wird iteriert
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if prog.search(token): continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)

    # ret wird zurueckgegeben.
    return ret



# clear_numerale
# Entfernen der Numeralen aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_numerale(input_list):
    # Liste der Numeralen
    numeral_list = ["[0-9]+", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
                    "elf", "zwölf",
                    "erste[smn]?", "zweite[smn]?", "dritte[smn]?", "vierte[smn]?", "fünfte[smn]?",
                    "sechste[smn]?", "siebte[smn]?", "achte[smn]?", "neunte[smn]?", "zehnte[smn]?",
                    "(drei|vier|fünf|sech|sieb|acht|neun)[zehn|zig]", "zwanzig", "hundert", "tausend",
                    "(ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun)und[a-z]+",
                    "(ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun)(mal|fach)",
                    "viel(?:en|e)?"]


    # pattern =  ^([0-9]+|eins|zwei|drei|vier|fünf|sechs|sieben|acht|neun|
    # zehn|elf|zwölf|erste[smn]?|zweite[smn]?|dritte[smn]?|vierte[smn]?|fünfte[smn]?|
    # sechste[smn]?|siebte[smn]?|achte[smn]?|neunte[smn]?|zehnte[smn]?|(drei|vier|fünf|
    # sech|sieb|acht|neun)[zehn|zig]|zwanzig|hundert|tausend|(ein|zwei|drei|vier|fünf|sechs|
    # sieben|acht|neun)und[a-z]+|(ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun)(mal|fach)|
    # viel(?:en|e)?)$
    pattern = "^("
    for numeral in numeral_list:
        pattern += numeral + "|"

    pattern = pattern[0:len(pattern)-1] +")$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern, re.IGNORECASE)

    # Rueckgabewert: Liste
    ret = []

    # input_list wird iteriert.
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert.
        if prog.search(token):continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)

    # ret wird zurueckgegeben.
    return ret



# clear_konjunktion
# Entfernen der Konjunktionen aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_konjunktion(input_list):
    # Liste der Konjunktionen
    konjuktion_list = ["während", "indem", "indes", "indessen",
                       "solange", "sowie", "sooft", "als", "wie",
                       "nachdem", "wenn", "sobald", "sowie", "seit",
                       "seitdem", "bis", "bevor", "ehe", "selten",
                       "indem", "soweit", "insoweit", "sofern", "insofern",
                       "soviel", "während", "wohingegen", "als", "ob",
                       "weil", "da", "zumal", "nun", "dass",
                       "sodass", "falls", "sofern", "soweit",
                       "obgleich", "obwohl", "obschon", "obzwar", "wenngleich",
                       "wennschon", "wiewohl", "ungeachtet", "gleichwohl",
                       "damit", "und"]

    # pattern =  ^(während|indem|indes|indessen|solange|sowie|sooft|als|wie|nachdem|wenn|
    # sobald|sowie|seit|seitdem|bis|bevor|ehe|selten|indem|soweit|insoweit|sofern|insofern|
    # soviel|während|wohingegen|als|ob|weil|da|zumal|nun|dass|sodass|falls|sofern|soweit|
    # obgleich|obwohl|obschon|obzwar|wenngleich|wennschon|wiewohl|ungeachtet|gleichwohl|
    # damit|und)$
    pattern = r"^("
    for konkuktion in konjuktion_list:
        pattern += konkuktion + "|"
    pattern = pattern[0:len(pattern)-1] +")$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern,re.IGNORECASE)
    # Rueckgabewert: Liste
    ret = []
    # input_list wird iteriert
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if prog.search(token): continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)
    # ret wird zurueckgegeben.
    return ret



# clear_praeposition
# Entfernen der Praepositionen aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_praeposition(input_list):
    # Liste der Praepositionen
    praeposition_list = ["ab", "aus", "von",
                         "an", "am" , "auf", "außer", "bei", "gegenüber", "hinter", "in",
                         "neben", "über", "unter", "vor", "zwischen",
                         "abseits", "außerhalb", "diesseits", "entlang", "inmitten",
                         "innerhalb", "jenseits", "längs", "oberhalb", "unterhalb", "unweit",
                         "an", "auf", "bis", "durch", "gegen", "hinter", "neben", "vor",
                         "nach", "ab", "bei", "mit", "von", "zu(?:r|m)?", "bis", "gegen",
                         "binnen", "in", "seit", "außerhalb", "innerhalb", "während",
                         "angesichts", "anlässlich", "auf", "aufgrund", "aus", "behufs",
                         "bei", "betreffs", "bezüglich", "dank", "durch", "für", "gemäß", "halber",
                         "infolge", "laut", "mangels", "mit", "mittels", "seitens", "trotz", "um",
                         "unbeschadet", "ungeachtet", "vermittels", "vermöge", "wegen", "zufolge",
                         "zwecks",
                         "abzüglich", "auf", "aus", "ausschließlich", "außer", "bei", "bis",
                         "an", "einscgließlich", "mitsamt", "nebt", "ohne", "samt", "statt",
                         "anstatt", "wider", "zuwider", "zuzüglich"]

    # pattern =  ^(ab|aus|von|an|am|auf|außer|bei|gegenüber|hinter|in|neben|über|unter|vor|zwischen|abseits|
    # außerhalb|diesseits|entlang|inmitten|innerhalb|jenseits|längs|oberhalb|unterhalb|unweit|an|auf|
    # bis|durch|gegen|hinter|neben|vor|nach|ab|bei|mit|von|zu(?:r|m)?|bis|gegen|binnen|in|seit|
    # außerhalb|innerhalb|während|angesichts|anlässlich|auf|aufgrund|aus|behufs|bei|betreffs|
    # bezüglich|dank|durch|für|gemäß|halber|infolge|laut|mangels|mit|mittels|seitens|trotz|um|
    # unbeschadet|ungeachtet|vermittels|vermöge|wegen|zufolge|zwecks|abzüglich|auf|aus|ausschließlich|
    # außer|bei|bis|an|einscgließlich|mitsamt|nebt|ohne|samt|statt|anstatt|wider|zuwider|zuzüglich)$
    pattern = r"^("
    for praeposition in praeposition_list:
        pattern += praeposition + "|"

    pattern = pattern[0:len(pattern)-1] +")$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern, re.IGNORECASE)
    # Rueckgabewert: Liste
    ret = []

    # input_list wird iteriert.
    for token in input_list:
        # if prog zutrifft , token wird ignoriert.
        if prog.search(token):continue
        # sonst token wird in ret hinzugefuegt
        else: ret.append(token)
    # ret wird zurueckgegeben.
    return ret



# clear_interjektion
# Entfernen der Interjektionen aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_interjektion(input_list):
    # Liste der Interjektionen
    interjektion_list = ["ach", "au", "pfui", "hä\?", "haha", "hey", "brr", "igit"]

    # pattern =  ^(ach|au|pfui|hä\?|haha|hey|brr|igit)$
    pattern = r"^("
    for interjektion in interjektion_list:
        pattern += interjektion + "|"

    pattern = pattern[0:len(pattern)-1]+")$"

    # pattern wird kompiliert und in prog gespeichert
    prog = re.compile(pattern, re.IGNORECASE)

    # Rueckgabewert : Liste
    ret = []

    # input_list wird iteriert
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if  prog.search(token) : continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)

    # ret wird zurueckgegeben.
    return ret




# clear_modal_und_hilfs_verben
# Entfernen der Modal- und Hilfsverben aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_modal_und_hilfs_verben(input_list):
    # Liste der Modal- und Hilfsverben
    modal_und_hilfs_verbe_list = ["dürfen", "können", "mögen", "müssen", "sollen", "wollen",
                  "darf(?:st)?", "durfte(?:st)?", "dürfte(?:st)?", "gedurft",
                  "kann(?:st)?", "konnte(?:st)?", "könnte(?:st)?", "gekonnt",
                  "mag(?:st)?", "mochte(?:st)?", "möchte(?:st)?", "gemocht",
                  "musst?", "musste(?:st)?", "müsste(?:st)?", "gemusst",
                  "soll(?:st)?", "sollte(?:st)?", "gesollt",
                  "will(?:st)?", "wollte(?:st)?", "gewollt",
                  "haben", "sein", "werden",
                  "habe", "hast", "hat", "hatte(?:st|n)?", "hätte(?:st|n)?", "hab", "habt", "gehabt",
                  "bin", "bist", "ist", "sind", "war(?:st|en)?", "wäre(?:st|n)?", "sei", "seid", "gewesen",
                  "werde", "wirst", "wird", "wurde(?:st|n)?", "würde(?:st|n)?", "ward",
                  "(?:ge)?worden", "aber"
                  ]


    # pattern =  ^(dürfen|können|mögen|müssen|sollen|wollen|darf(?:st)?|durfte(?:st)?|dürfte(?:st)?|
    # gedurft|kann(?:st)?|konnte(?:st)?|könnte(?:st)?|gekonnt|mag(?:st)?|mochte(?:st)?|möchte(?:st)?|
    # gemocht|musst?|musste(?:st)?|müsste(?:st)?|gemusst|soll(?:st)?|sollte(?:st)?|gesollt|will(?:st)?|
    # wollte(?:st)?|gewollt|haben|sein|werden|habe|hast|hat|hatte(?:st|n)?|hätte(?:st|n)?|hab|habt|
    # gehabt|bin|bist|ist|sind|war(?:st|en)?|wäre(?:st|n)?|sei|seid|gewesen|werde|wirst|wird|
    # wurde(?:st|n)?|würde(?:st|n)?|ward|(?:ge)?worden|aber)[.,]?$
    pattern = "^("
    for verb in modal_und_hilfs_verbe_list:
        pattern += verb + "|"

    pattern = pattern[0:len(pattern)-1] + ")[.,]?$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern, re.IGNORECASE)
    # Rueckgabewert: Liste
    ret = []

    # input_list wird iteriert
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if prog.search(token): continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)

    # ret wird zurueckgegeben.
    return ret




# clear_adverb
# Entfernen der Adverbien aus der Eingabeliste
# Argument: Eingabeliste
# Rueckgabewert: "bereinigte" Liste
def clear_adverb(input_list):
    # Liste der Adverbien
    adverb_list = ["hier", "da", "links", "vorne", "hinten", "überall",
                   "hoch", "vorwärts", "abwärts", "dorthin", "umher", "herum",
                   "herunter", "dorther", "herab", "herunter", "hindurch",
                   "nachdem", "sobald", "während", "solange", "bevor", "bis",
                   "deshalb", "also", "folglich", "dann", "andernfalls", "dennoch",
                   "trotzdem", "so", "dazu", "wozu",
                   "überaus", "äußerst", "einigermaßen", "halbwegs", "sehr", "größtenteils",
                   "kaum", "haufenweise", "umsonst", "ebenfalls", "sonst", "auch",
                   "ferner", "außerdem", "zudem", "erstens", "zweitens", "drittens",
                   "hingegen", "allerdings", "immerhin", "wenigstens", "doch", "noch", "auch", "jedoch", "nur",
                   "zumindest", "kurzerhand", "wahrscheinlich", "(?:un)?glücklicherweise",
                   "mehr", "gerne"]
    # pattern =  ^(hier|da|links|vorne|hinten|überall|hoch|vorwärts|abwärts|dorthin|umher|herum|herunter|dorther|herab|
    # herunter|hindurch|nachdem|sobald|während|solange|bevor|bis|deshalb|also|folglich|dann|andernfalls|dennoch|
    # trotzdem|so|dazu|wozu|überaus|äußerst|einigermaßen|halbwegs|sehr|größtenteils|kaum|haufenweise|umsonst|
    # ebenfalls|sonst|auch|ferner|außerdem|zudem|erstens|zweitens|drittens|hingegen|allerdings|immerhin|wenigstens|
    # doch|noch|auch|jedoch|nur|zumindest|kurzerhand|wahrscheinlich|(?:un)?glücklicherweise|mehr|gerne)$
    pattern = "^("
    for adverb in adverb_list:
        pattern += adverb + "|"
    pattern = pattern[0:len(pattern)-1] +")$"

    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern, re.IGNORECASE)

    # Rueckgabewert : Liste
    ret = []

    # input_list wird iteriert.
    for token in input_list:
        # wenn prog zutrifft , token wird ignoriert
        if prog.search(token): continue
        # sonst token wird in ret hinzugefuegt.
        else: ret.append(token)

    # ret wird zurueckgegeben.
    return ret



text = """In den vergangenen Jahren haben wir uns mit vielen, schönen und bunten
Themen beschäftigen können. Wir haben unterschiedliche Kriterien anwenden
können und mit Begeisterung am 27.06.2017 den 364. König krönen können.
Begeistert waren auch die bunt gekleideten Besucher, die sich gerne zeigten.
Gewiss, ich schreibe diesen Bericht der Ordnung zuliebe nieder, aus einer
gewissen Pedanterie heraus, damit er zu den Akten komme. Ich will mich
zwingen, noch einmal die Ereignisse zu überprüfen, die zum Freispruch
eines Mörders und zum Tode eines Unschuldigen geführt haben. (Er meint
mehr als zwei Unschulde, aber hier zählen nur reiche, alte Herren.)
"""

# find_nomen
# Finden der Nomen aus dem Eingabestring
# Argument: Eingabestring
# Rueckgabewert: Gefundene Nomen als eine Liste
def find_nomen(input):
    # input wird nach "\n+" gesplitted und in lines gespeichert.
    lines = input.split("\n+")
    # alle non-empty tokens werden in input_list gespeichert
    input_list = []
    # Rueckgabewert: Liste
    nomen = []
    # \W+ => non-word Zeichen, >= 1 mals
    pattern = "\W+"
    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern)
    # lines werden iteriert
    for line in lines:
        # line wird gesplitted und in splitted gespeichert.
        splitted = prog.split(line)
        # splitted wird aus leeren Strings bereinigt
        splitted = [word for word in splitted if word != ""]
        # Elemente der splitted werden in input_list hinzugefuegt.
        input_list.extend(splitted)


    # clear_* Funktionen werden auf input_list aufgerufen , um input_list zu bereinigen.
    input_list = clear_modal_und_hilfs_verben(input_list)
    input_list = clear_numerale(input_list)
    input_list = clear_interjektion(input_list)
    input_list = clear_praeposition(input_list)
    input_list = clear_konjunktion(input_list)
    input_list = clear_pronomen(input_list)
    input_list = clear_artikel(input_list)
    input_list = clear_adverb(input_list)

    # input_list wird iteriert
    for word in input_list:
        # wenn der erste Buchstabe des word ein Grossbuchstabe ist , wird word in nomen hinzugefuegt.
        if word[0].isupper():
            nomen.append(word)


    # nomen wird zurueckgegeben.
    return nomen




# find_adjektive
# Finden der Adjektiven aus dem Eingabestring
# Argument: Eingabestring
# Rueckgabewert: Gefundene Adjektiven als eine Liste
def find_adjektive(input):
    # input wird nach "\n+" gesplitted und in lines gespeichert.
    lines = input.split("\n+")
    # alle non-empty tokens werden in input_list gespeichert
    input_list = []
    # Rueckgabewert: Liste
    adjektive = []
    # \W+ => non-word Zeichen, >= 1 mals
    pattern = "\s+"
    # pattern wird kompiliert und in prog gespeichert.
    prog = re.compile(pattern)
    # lines werden iteriert
    for line in lines:
        # line wird gesplitted und in splitted gespeichert.
        splitted = prog.split(line)
        # splitted wird aus leeren Strings bereinigt
        splitted = [word for word in splitted if word != ""]
        # Elemente der splitted werden in input_list hinzugefuegt.
        input_list.extend(splitted)


    # Woerter die vor dem '.' vorkommen , werden entfernt
    input_list = [word for word in input_list if word[len(word)-1] != '.']


    temp = []
    # input_list wird iteriert
    for word in input_list:
        # ',' wird aus dem Wort entfernt
        if word[len(word)-1] == ",": temp.append(word[0:len(word)-1])
        else: temp.append(word)

    # Elemente der temp werden in input_liste kopiert.
    input_list = temp[0:len(temp)]

    # clear_* Funktionen werden auf input_list aufgerufen , um input_list zu bereinigen.
    input_list = clear_modal_und_hilfs_verben(input_list)
    input_list = clear_numerale(input_list)
    input_list = clear_interjektion(input_list)
    input_list = clear_praeposition(input_list)
    input_list = clear_konjunktion(input_list)
    input_list = clear_pronomen(input_list)
    input_list = clear_artikel(input_list)
    input_list = clear_adverb(input_list)

    # input_list wird iteriert
    for word in input_list:
        # wenn der erste Buchstabe des word ein Kleinbuchstabe ist , wird word in adjektive hinzugefuegt.
        if word[0].islower():
            adjektive.append(word)

    # adjektive wird zurueckgegeben.
    return adjektive


# find_nomen_und_adjektive
# Finden Nomen and Adjektiven aus dem Eingabestring
# Argument: Eingabestring
# Rueckgabewert: Tupel der Nomenliste und Adjektivenliste
def find_nomen_und_adjektive(text):
    # find_nomen() wird aufgerufen und das Ergebnis wird in nomen_list gespeichert.
    nomen_list = find_nomen(text)
    # find_adjektive() wird aufgerufen und das Ergebnis wird in adjektive_list gespeichert.
    adjektive_list = find_adjektive(text)
    # nomen_list and adjektive_list wird as Tupel zurueckgegeben.
    return (nomen_list, adjektive_list)


# find_nomen_und_adjektive() wird aufgerufen und das Ergebnis wird dekomposiert
# das erste Element des Tupels wird in nomen_list , das zweite Element wird in adjektive_list gespeichert.
(nomen_list, adjektive_list) = find_nomen_und_adjektive(text)
# nomen_list wird ausgegeben
print("<<find_nomen>>")
print(nomen_list)
# adjektive_list wird ausgegeben
print("<<find_adjektive>>")
print(adjektive_list)


# Das Ergebnis des Programs
"""
<<find_nomen>>
['Jahren', 'Themen', 'Kriterien', 'Begeisterung', 'König', 'Begeistert', 'Besucher', 'Gewiss', 
'Bericht', 'Ordnung', 'Pedanterie', 'Akten', 'Ereignisse', 'Freispruch', 'Mörders', 'Tode', 'Unschuldigen',
 'Unschulde', 'Herren']
<<find_adjektive>>
['vergangenen', 'schönen', 'bunten', 'beschäftigen', 'unterschiedliche', 'anwenden', 'krönen', 'bunt', 
'gekleideten', 'schreibe', 'zuliebe', 'nieder', 'gewissen', 'heraus', 'zwingen', 'überprüfen', 'geführt',
 'meint', 'zählen', 'reiche', 'alte']

 
Finden Nomen liefert besseres Ergebnis , der Trick hier ist , nach der Bereinigung der input_liste , haben wir meistens Nomen, 
 Adjektiven , ein paar Adverbien, und Vollverben. Und ausser der Nomen , anderen muessen klein geschrieben werden ,
  wenn sie nicht  am Anfang des Satzes verwendet werden. 
 
Finden Adjektiven liefert nicht so gutes Ergebnis , es war schwierig zwischen Adjektive/Adverb und Adjektive/Vollverb 
zu unterscheiden.
"""

# Das manuell-berechnete Ergebnis
"""
Nomen: 
Jahren, Themen, Kriterien, Begeisterung, König, Besucher, Bericht , Ordnung , Pedanterie, Akten, Ereignisse , 
Freispruch, Mörders, Tode, Unschuldigen , Unschulde , Herren

Adjektiven: 
vergangenen, schönen, bunten , unterschiedliche , Begeistert, gekleideten, gewissen, reiche , alte
"""
