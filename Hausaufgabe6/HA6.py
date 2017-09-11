'''
Hausaufgabe 6
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: Mike Josaf 108014224341
'''


# 1. read_file
# Einlesen einer Datei
# Argument:Name der einzulesenden Datei
# Rueckgabewert: Inhalt der Datei in einem String
def read_file(filename):
    # Rueckgabewert der Funktion
    grammar = ""
    # Datei wird fuers Lesen geoffnet (und wird automatisch geschlossen, wenn with-Block verlassen wird)
    with open(filename, 'r') as f:
        # Alle Zeilen werden gelesen
        lines = f.readlines()
        # Das '\n' Zeichen wird aus jeder Zeile entfernt
        # Hier Listen-Abstraktion wird benutzt
        lines = [line.rstrip("\n") for line in lines]
        # Die Zeilen werden mit dem '\n' als delimiter zusammengefuegt
        # und der grammar zugewiesen
        grammar += "\n".join(lines)
    # grammar wird zurueckgegeben
    return grammar




# 2. read_grammar
# Einlesen einer Grammatik im obigen Format aus einem String
# Argument: String mit der Grammatik
# Rückgabewert: Grammatikregeln in einer geeigneten Datenstruktur (als list der dict-s)
def read_grammar(grammar):
    # string grammar wird mit dem '\n' als Separator in zeilen aufgeteilt
    lines = grammar.split("\n")
    # rules ist eine List , wer Elemente von Typ dict speichert
    rules = list()

    # Zeilen (lines) werden iteriert
    for line in lines:
        # Zeile wird mit dem " --> " als Separator aufgeteilt
        splitted = line.split(" --> ")
        # Das erste Element von splitted wird dem parent zugewiesen.
        parent = splitted[0]
        # Das zweite Element von splitted wird mit dem whitespace als Separator aufgeteilt
        # und das Ergebnis wird dem splitted2 zugewiesen.
        splitted2 = splitted[1].split()
        # Dem children werden all Elemente von splitted2 ausser das letzte  zugewiesen.
        children = splitted2[0:len(splitted2)-1]
        # Das letzte Element von splitted (Warhscheinlichkeit) wird dem probability
        # zugewiesen.
        probability = splitted2[len(splitted2)-1]
        # parent , children und probability werden als dict() zusammengefasst und der rules
        # hinzugefuegt.
        rules.append({
            "parent": parent,
            "children": children ,
            "probability": probability
        })

    # rules wird zurueckgegeben
    return rules






# 3. write_grammar
# Ausgabe einer Grammatik in eine Datei (gleiches Format wie oben;
# 2 Tabulatoren zwischen der Regel und ihrer Wahrscheinlichkeit)
# Argumente: 1. Dateiname der Ausgabedatei
# 2. Grammatikregeln in einer geeigneten Datenstruktur (als list der dict-s)
# Rückgabewert: keiner
def write_grammar(outfile, rules):
    # Datei wird fuers Schreiben mit with keyword geoeffnet.
    with open(outfile, "w") as out:
        # rules wird iteriert.
        for rule in rules:
            # rule ist ein dict , mit keys : "parent" , "children", "probability"
            # parent wird dem Wert fuers key "parent" von rule zugewiesen.
            parent = rule["parent"]
            # children wird dem Wert fuers key "children" von rule zugewiesen.
            children = rule["children"]
            # probability wird dem Wert fuers key "probability" von rule zugewiesen.
            probability = rule["probability"]
            # parent , children und probability werden im angeforderten Format
            # als string verknuepft und dem merged zugewiesen.
            merged = parent + " --> " + " ".join(children) + "\t\t" + probability +"\n"
            # merged wird der out geschrieben.
            out.write(merged)





# 4. extract_rules
# Extraktion aller Grammatikregeln mit einer bestimmten Mutterkategorie
# aus einer Grammatik
# Argumente: 1. Gewünschte Kategorie der Mutter
# 2. Grammatikregeln in einer geeigneten Datenstruktur
# Rückgabewert: Grammatik mit nur denjenigen Regeln,
# die die gewünschte Mutterkategorie
# enthalten, in einer geeigneten Datenstruktur (als list der dict-s)
def extract_rules(parent, rules):
    # subset ist der Rueckgabewert der Funktion
    subset = []
    # rules wird iteriert
    for rule in rules:
        # wenn der Wert fuers Key "parent" von rule dem parent Eingebeparameter gleich ist ,
        # wird rule der subset hinzugefuegt
        if rule["parent"] == parent:
            subset.append(rule)
    # subset wird zurueckgegeben.
    return subset



# partition
# Partionierung der Liste in Teilliste basierend auf oefnnenden und schliessenden
# Klammern.
# Argument: Liste im gewuenschten Format
# Rueckgabewert: Liste der Teilliste
# Bemerkung: diese Funktion wird in learn_rule() verwendet.
def partition(sublist):
    # ret ist der Rueckgabewert der Funktion, als Liste
    ret = []
    # counter wird mit 0 belegt
    counter = 0
    # init wird mit 0 belegt
    init = 0
    # Indizes der sublist wird iteriert
    for i in range(0,len(sublist)):
        # Element fuer den geeigneten Index von sublist zugegriffen und dem el
        # zugewiesen.
        el = sublist[i]
        # wenn el dem Wert '(' gleich ist , wird counter um 1 erhoeht.
        if el == '(': counter += 1
        # wenn el dem Wert ')' gleich ist , wird counter um 1 erniedrigt.
        if el == ')': counter -= 1
        # wenn counter dem Wert 0 gleich ist , Teilliste von sublist vom index init bis
        # (i+1) in die ret hinzugefuegt
        # und init wird mit (i+1) wiederbelegt.
        if counter == 0:
            ret.append(sublist[init:i+1])
            init = i + 1

    # ret wird zurueckgegeben.
    return ret





# learn_rule
# Extraktion der Regeln von einer Baumbank im Klammerformat
# Argumente: 1. Liste der Baumbank im Klammerformat
# 2. Leere liste , diese Liste wird im jedem Rekursionschritt modifiziert
# Rueckgabewert: keiner
# Bemerkung: Diese Funktion handelt keine Exception , es wurde davon ausgegangen , dass
# der Benutzer/in dieser Funktion weiss , was er/sie tut.
def learn_rule(grammar, learned):
    # das erste and letzte Element der grammar werden geloescht.
    grammar = grammar[1:len(grammar)-1]
    # das erste Element der grammar wird dem root zugewiesen.
    root = grammar[0]

    # das zweite Element der grammar wird dem el zugewiesen.
    el = grammar[1]
    # if el dem Wert '(' nicht gleich ist , root und el im gewuenschten Format
    # dem learned hinzugefuegt.
    if el != '(':
        learned.append(root+ " --> " + el)
    # Sonst
    else:
        # das erste Element der grammar geloescht.
        grammar = grammar[1:len(grammar)]
        # root + " --> " wird dem el zugewiesen.
        el = root + " --> "
        # Liste der Teillisten von grammar wird mit der Hilfe partition()  erstellt
        # und eventuell sie wird iteriert.

        for part in partition(grammar):
            # In jedem Iterationsschritt wird learn_rule rekursive aufgerufen und das Ergebnis wird
            # dem ret zugewiesen
            ret = learn_rule(part, learned)
            # (ret + " ") wird dem el hinzugefuegt.
            el += ret + " "

        # el wird der learned hinzugefuegt.
        learned.append(el)

    # root wird zurueckgegeben.
    return root




# 5. read_treebank
# Einlesen einer Baumbank im Klammerformat
# Argument: String mit der Baumbank
# Rückgabewert: Baumrepraesentationen mit Frequenzen
# in einer geeigneten Datenstruktur (als dict() mit dem Name der Regel als Key , und Frequenz
# dieser Regel als Value)
def read_treebank(treebank):
    # treebank wird mit dem '\n' als Separator auf Zeilen aufgeteilt
    lines = treebank.split("\n")
    # Dieser ist der Rueckgabewert der Funktion
    tokens_with_freq = dict()
    # lines werden iteriert
    for line in lines:
        # line wird mit dem whitespace als Separator auf tokens aufgeteilt
        tokens = line.split()
        # learned wird mit der leeren Liste belegt.
        learned = []
        # learn_rules wird aufgerufen.
        learn_rule(tokens, learned)
        # learned wird iteriert.
        for token in learned:
            # Frequenz von token wird von tokens_with_freq dict abgefragt
            # Wenn dict  das abgefragte Token nicht enthaelt, 0 wird zurueckgegeben.
            freq = tokens_with_freq.get(token, 0)
            # freq wird um 1 erhoeht.
            freq += 1
            # freq wird dem Key token in dict zugewiesen.
            tokens_with_freq[token] = freq

    # dict wird zurueckgegen.
    return tokens_with_freq


# calculate_whole_frequency
# Berechnung der gesamten Haeufigkeit der einzelnen Regeln
# Argument: Regeln im Format (dict , mit Regel als Key , und Frequenz dieser Regel als Value)
# Rueckgabewert: gesamte Frequenz der einzelnen Regeln als dict mit Regel als Key , die gesamte
# Frequenz als Value
# Bemerkung: diese Funktion wird in write_grammar_in_file() benutzt.
def calculate_whole_frequency (rules):
    # ret ist der Rueckgawert der Funktion
    ret = dict()
    # rules dict wird iteriert
    for rule , freq in rules.items():
        # rule (key) wird mit dem " --> " als Separator aufgeteilt und
        # dem splitted zugewiesen.
        splitted = rule.split(" --> ")
        # splitted[0] wird dem parent_rule zugewiesen.
        parent_rule = splitted[0]
        # Wert mit dem key parent_rule von ret abgefragt , unnd dict den abgefragten key
        # nicht enthaelt 0 wird zurueckgegeben.
        whole_freq = ret.get(parent_rule, 0)
        # whole_freq wird um freq erhoeht
        whole_freq += freq
        # Dem Entry mit key parent_rule in ret wird whole_freq zugewiesen.
        ret[parent_rule] = whole_freq

    # ret wird zurueckgegeben.
    return ret


# 6. write_grammar_in_file
# Ausgabe einer Grammatik in eine Datei (Format wie oben Z.17-19;
# 2 Tabulatoren zwischen Regel und ihre Wahrscheinlichkeit)
# Argumente: 1. Dateiname der Ausgabedatei
# 2. Grammatikregeln in einer geeigneten Datenstruktur (als dict mit Regel als Key , die gesamte
# Frequenz als Value )
# Rückgabewert: keiner
def write_grammar_in_file(outfile, rules):
    # calculate_whole_frequency() wird aufgerufen und das Ergebnis wird
    # dem whole_frequency zugewiesen.
    whole_frequency = calculate_whole_frequency(rules)
    # Datei fuers Schreiben wird geoffent.
    with open(outfile, "w") as f:
        # rules dict wird iteriert.
        for rule, freq in rules.items():
            # rule wird mit dem " --> " als Separator aufgeteilt und dem splitted
            # zugewiesen.
            splitted = rule.split(" --> ")
            # Wahrscheinlichkeit der freq wird berechnet und dem probability zugewiesen.
            probability = freq/ whole_frequency[splitted[0]]
            # rule und probability wird im angeforderten Format als String verknuepft.
            line = rule + "\t\t" + "{0:.10f}".format(probability) + "\n"
            # line wird dem f geschrieben.
            f.write(line)



# Grammatik einlesen
grammar = read_file("grammatik.txt")
# Regeln parsen
rules = read_grammar(grammar)
# NP-Regeln extrahieren (beispielhafte Anfrage
# -- andere Kategorien sollten natuerlich ebenfalls moeglich sein)
subset = extract_rules("NP",rules)
# Subset ausgeben
outfile = "subset_out.txt"
write_grammar(outfile,subset)
# Baumbank einlesen
treebank = read_file("tueba5000.penn")
# Baeume parsen
rules = read_treebank(treebank)
# Grammatik ausgeben
write_grammar_in_file("grammatik.txt",rules)