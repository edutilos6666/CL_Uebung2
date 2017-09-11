def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{0} likes this".format(names[0])
    elif len(names) == 2:
        return "{0} and {1} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{0}, {1} and {2} like this".format(names[0], names[1], names[2])
    else:
        part1 = names[0:2]
        rest_size = len(names[2:])
        return ", ".join(part1) + " and " + str(rest_size) + " others like this"


def find_outlier(integers):
    evens = [n for n in integers if n%2 == 0]
    odds = [n for n in integers if n%2 != 0]
    ret = None
    if len(evens) == 1 :
        ret = evens[0]
    elif len(odds) == 1:
        ret = odds[0]

    return ret

import re
def iq_test(numbers):
    numbers = re.split(r"\s+", numbers)
    #numbers = numbers.split(" ")
    numbers = [int(n) for n in numbers]
    evens = [n for n in numbers if n%2 == 0]
    odds = [n for n in numbers if n%2 != 0]
    ret = None
    if len(evens) == 1:
        ret = numbers.index(evens[0]) +1
    elif len(odds) == 1:
        ret = numbers.index(odds[0]) +1

    return ret



def alphabet_position(text):
    positions = []
    text = text.lower()
    text = [ch for ch in text if ch.isalpha()]
    alphas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
              "p","q","r","s","t","u","v","w","x","y","z"]
    for ch in text:
        positions.append(str(alphas.index(ch)+1))
    return " ".join(positions)



def spin_words(sentence):
    splitted =  sentence.split(" ")
    ret = []
    for w in splitted:
        if len(w) < 5:
            ret.append(w)
        else:
            ret.append(w[::-1])

    return " ".join(ret)


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    while len(array1) != 0 and len(array2) != 0:
        el1 = array1.pop()
        index = array2.index(el1**2)  if el1**2 in array2 else -1
        if index == -1:
            return False

        del array2[index]
    return True



def scramble(s1,s2):
    for ch in s2:
        index = s1.index(ch) if ch in s1 else None
        if index is None :
            return False
        if index != 0:
            s1 = s1[0:index] + s1[index+1:]
        else:
            s1 = s1[index:]
    return True