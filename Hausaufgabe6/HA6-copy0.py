# 1. read_file
# Einlesen einer Datei
# Argument:Name der einzulesenden Datei
# Rueckgabewert: Inhalt der Datei in einem String
def read_file(filename):
    grammar = ""
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

        grammar += "\n".join(lines)

    return grammar


# grammar = read_file('grammatik.txt')
# print(grammar)


# 2. read_grammar
# Einlesen einer Grammatik im obigen Format aus einem String
# Argument: String mit der Grammatik
# Rückgabewert: Grammatikregeln in einer geeigneten Datenstruktur
import re
def read_grammar(grammar):
    lines = grammar.split("\n")
    rules = list()

    for line in lines:
        splitted = line.split(" --> ")
        parent = splitted[0]
        splitted2 = splitted[1].split()
        children = splitted2[0:len(splitted2)-1]
        probability = splitted2[len(splitted2)-1]
        rules.append({
            "parent": parent,
            "children": children ,
            "probability": probability
        })
    return rules



grammar = read_file('grammatik.txt')
# print(grammar)
rules = read_grammar(grammar)
# print(repr(grammar))
# for rule in rules:
#     for k, v in rule.items():
#         print(k, "=>", v, end= " ;; ")
#     print()




# 3. write_grammar
# Ausgabe einer Grammatik in eine Datei (gleiches Format wie oben;
# 2 Tabulatoren zwischen der Regel und ihrer Wahrscheinlichkeit)
# Argumente: 1. Dateiname der Ausgabedatei
# 2. Grammatikregeln in einer geeigneten Datenstruktur
# Rückgabewert: keiner
def write_grammar(outfile, rules):
    with open(outfile, "w") as out:
        for rule in rules:
            parent = rule["parent"]
            children = rule["children"]
            probability = rule["probability"]
            merged = parent + " --> " + " ".join(children) + "\t\t" + probability +"\n"
            out.write(merged)





# 4. extract_rules
# Extraktion aller Grammatikregeln mit einer bestimmten Mutterkategorie
# aus einer Grammatik
# Argumente: 1. Gewünschte Kategorie der Mutter
# 2. Grammatikregeln in einer geeigneten Datenstruktur
# Rückgabewert: Grammatik mit nur denjenigen Regeln,
# die die gewünschte Mutterkategorie
# enthalten, in einer geeigneten Datenstruktur
def extract_rules(parent, rules):
    subset = []
    for rule in rules:
        if rule["parent"] == parent:
            subset.append(rule)

    return subset



np_rules = extract_rules("NP", rules)




write_grammar("whole_rules.txt", rules)
write_grammar("np_rules.txt", np_rules)




def partition(sublist):
    ret = []
    counter = 0
    init = 0
    for i in range(0,len(sublist)):
        el = sublist[i]
        if el == '(': counter += 1
        if el == ')': counter -= 1
        if counter == 0:
            ret.append(sublist[init:i+1])
            init = i +1

    return ret


l = ['(', 'b', 'c', ')', '(', 'd', 'e', ')', '(', 'd', 'e', ')','(', 'd', 'e', ')',')']
for el in partition(l):
    print(el)



# def learn_rule(grammar):
#     grammar = grammar[1:len(grammar)-1]
#     root = grammar[0]
#
#     el = grammar[1]
#     if el != '(':
#         return [root].append([grammar[1]])
#     else:
#         grammar = grammar[1:len(grammar)]
#         for part in partition(grammar):
#             return [root].append(learn_rule(part))


import copy
# def learn_rule(grammar, parsed, learned):
#     grammar = grammar[1:len(grammar)-1]
#     root = grammar[0]
#
#     el = grammar[1]
#     if el != '(':
#         # parsed.append([root, [grammar[1]]])
#         parsed.append(el)
#         learned.append(root+ " --> " + el)
#     else:
#         grammar = grammar[1:len(grammar)]
#
#         # parsed = copy.deepcopy(temp)
#         # parsed.append(root)
#         el = root + " --> "
#         for part in partition(grammar):
#             ret = learn_rule(part, parsed, learned)
#             el += ret + " "
#             parsed.append(ret)
#
#         learned.append(el)
#
#     return root

def learn_rule(grammar, learned):
    grammar = grammar[1:len(grammar)-1]
    root = grammar[0]

    el = grammar[1]
    if el != '(':
        learned.append(root+ " --> " + el)
    else:
        grammar = grammar[1:len(grammar)]
        el = root + " --> "
        for part in partition(grammar):
            ret = learn_rule(part, learned)
            el += ret + " "
        learned.append(el)

    return root

l = ['(', 'a', '(', 'b', 'c', ')', '(', 'd', 'e', ')', ')']
parsed = []
learned = []
print(learn_rule(l, learned))
print(parsed)
print(learned)

l = ['(', 'a', '(', 'b', '(', 'f', 'c', ')',')', '(', 'd', 'e', ')', ')']
parsed = []
learned = []
print(learn_rule(l, learned))
print(parsed)
print(learned)


l = ['(', 'a', '(', 'b', '(', 'f', 'c', ')','(', 'g', 'h', ')',')', '(', 'd', 'e', ')', ')']
parsed = []
learned = []
print(learn_rule(l, learned))
print(parsed)
print(learned)

# children = []
# l = ['(', 'a', '(', 'b', 'c', ')', '(', 'd', 'e', ')', ')']
# learn_rule(l , children , True)

# import pprint
# pprint.pprint(children)


# 5. read_treebank
# Einlesen einer Baumbank im Klammerformat
# Argument: String mit der Baumbank
# Rückgabewert: Baumrepraesentationen mit Frequenzen
# in einer geeigneten Datenstruktur
from pprint import pprint
def read_treebank(treebank):
    lines = treebank.split("\n")
    tokens_with_freq = dict()
    for line in lines:
        tokens = line.split()
        learned = []
        learn_rule(tokens, learned)
        for token in learned:
            freq = tokens_with_freq.get(token, 0)
            freq += 1
            tokens_with_freq[token] = freq

    pprint(tokens_with_freq)
    return tokens_with_freq



# 6. write_grammar_in_file
# Ausgabe einer Grammatik in eine Datei (Format wie oben Z.17-19;
# 2 Tabulatoren zwischen Regel und ihre Wahrscheinlichkeit)
# Argumente: 1. Dateiname der Ausgabedatei
# 2. Grammatikregeln in einer geeigneten Datenstruktur
# Rückgabewert: keiner

# rules hier ist ein dict {XY --> I: 2, ...}
def calculate_whole_frequency (rules):
    ret = dict()
    for rule , freq in rules.items():
        splitted = rule.split(" --> ")
        value = ret.get(splitted[0], 0)
        value += freq
        ret[splitted[0]] = value

    return ret

def write_grammar_in_file(outfile, rules):
    whole_frequency = calculate_whole_frequency(rules)
    with open(outfile, "w") as f:
        for rule, freq in rules.items():
            splitted = rule.split(" --> ")
            probability = freq/ whole_frequency[splitted[0]]
            line = rule + "\t\t" + "{0:.10f}".format(probability) + "\n"
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
write_grammar_in_file("grammatik2.txt",rules)