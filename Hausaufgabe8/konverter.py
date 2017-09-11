'''
Hausaufgabe 8
NAME1 MATRIKELNUMMER: Nijat Aghayev 108015250476
NAME2 MATRIKELNUMMER: Mike Josaf 108014224341
'''

import re

# Top-Level-Statement
print('module konverter meldet sich an.')
# Module Attribute
geschichte = []


'''
Die Klasse konverter hat 4 wichtigste Methoden: 
int_zu_hex(self, int_num) -> konvertiert Integer Dezimalzahl nach Hexzahl
hex_zu_int(self, hex_string) -> konvertiert Hexzahl nach Integer Dezimalzahl
int_zu_rom(self, int_num) -> konvertiert Integer Dezimalzahl nach roemischer Zahl
rom_zu_int(self, rom_string) -> konvertiert roemische Zahl nach Integer Dezimalzahl
'''
class konverter:

    # Konstruktor
    def __init__(self):
        # Instanzvariablen: hex_map, reverse_hex_map und rom_map
        self.hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        self.reverse_hex_map = {'A':10,'B':11 , 'C':12, 'D':13, 'E':14, 'F':15}
        self.rom_map = {'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}



    # convert_hex_digit_to_str
    # Konvertierung der Hexziffer nach Hex-String, wichtig insbesondere fuer Ziffer 10-15
    # Argument: Integer Ziffer
    # Rueckgabewert: Hex-String
    def convert_hex_digit_to_str(self, digit):
        # Wenn digit >= 0 und <= 9, wird digit in string umgewandelt und zurueckgegeben
        if digit >= 0 and digit <= 9:
            return str(digit)
        # Sonst , der Wert der Instanzvariable hex_map fuer Schluessel digit wird zurueckgegeben
        elif digit >= 10 and digit <= 15:
            return self.hex_map[digit]


    # convert_hex_str_to_hex_digit
    # Konvertierung der Hex-String nach Hexziffer
    # Argument: Hex-String
    # Rueckgabewert: Hexziffer
    def convert_hex_str_to_hex_digit(self, input):
        # wenn input Ziffer von 0 bis 9 repraesentiert , wird str in integer umgewandelt
        # und zurueckgegeben.
        if input in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(input)
        # sonst  der Wert der Instanz-Variable reverse_hex_map fuer  Schluessel input.upper()
        # wird zurueckgegeben.
        elif input.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
            return self.reverse_hex_map[input.upper()]




    # int_zu_hex
    # Konvertierung der Integer Dezimalzahl nach Hex-String
    # Argument: Integer Dezimalzahl
    # Rueckgabewert: Hex-String
    def int_zu_hex(self, int_num):
        # is_negative wird auf False gesetzt
        is_negative = False
        # regex wird eingesetzt , um die Eingabe zu ueberpruefen.
        pattern = "^-?[0-9]+$"
        prog = re.compile(pattern)
        # wenn Eingabe ungueltig ist , Meldung wird in die Konsole ausgegeben und -1
        # wird zurueckgegeben.
        if not prog.match(str(int_num)):
            print("Ungueltige Eingabe , nur Integer-Zahlen(positive oder negative) sind erlaubt.")
            return -1

        # int_num wird in integer umgewandelt
        int_num = int(int_num)
        # wenn int_num == 0 , geeignete Berechnung wird in die geschichte hinzugefuegt und
        # 0 wird zurueckgegeben.
        if int_num == 0:
            geschichte.append("(0,0,I,H)")
            return 0

        # eine leere Liste namens digits wird belegt.
        digits = []

        # int_num wird der temp_num zugewiesen.
        temp_num = int_num

        # wenn int_num negative ist , wird Vorzeichen der temp_num veraendert und
        # is_negative auf True gesetzt.
        if int_num < 0:
            temp_num = -int_num
            is_negative = True

        # while-loop mit der Abbruchbedingung temp_num > 0 wird erstellt.
        while temp_num > 0 :
            # das Ergebnis des temp_num modulo 16 wird in rest gespeichert.
            rest = temp_num % 16
            # temp_num wird mit 16 ganzzahlig dividiert.
            temp_num = temp_num // 16
            # rest wird in die digits hinzugefuegt
            digits.append(rest)

        # digits wird umgedreht.
        digits = reversed(digits)
        # eine leere String namens ret wird erstellt.
        ret = ''
        # digits wird iteriert
        for digit in digits:
            # digit wird nach Hex-Ziffer umgewandelt und in die ret konkatiniert.
            ret += self.convert_hex_digit_to_str(digit)

        # wenn is_negative wahr ist , wird Minuszeichen in die ret vorangestellt.
        if is_negative:
            ret = '-'+ ret


        # tracker wird benutzt , um die Berechnung im geeigneten Format in geschichte hinzuzufuegen.
        tracker = [str(int_num), ret , "I", "H"]
        geschichte.append("(" + ",".join(tracker) + ")")
        # ret wird zurueckgegeben.
        return ret



    # hex_zu_int
    # Konvertierung Hex-String nach Integer Dezimalzahl
    # Argument: Hex-String
    # Rueckgabewert: Integer Dezimalzahl
    def hex_zu_int(self, hex_string):
        # hex_string wird nach String umgewandelt.
        hex_string = str(hex_string)
        # eine leere Liste namens tracker wird erstellt.
        tracker = []
        # hex_string wird in die tracker hinzugefuegt.
        tracker.append(hex_string)
        # is_negative wird auf False gesetzt,
        is_negative = False
        # regex wird eingesetzt , um die Gueltigkeit der Eingabe zu ueberpruefen.
        pattern = "^-?[0-9a-fA-F]+$"
        prog = re.compile(pattern)
        # Wenn die Eingabe nicht gueltig ist, wird eine Fehlermeldung ausgegeben und
        # -1 zurueckgegeben.
        if not prog.match(hex_string):
            print('hex_string darf Minuszeichen , Ziffer, Buchstaben von "a" bis "z" , von "A" bis "Z" enthalten')
            return -1

        # wenn das erste Zeichen der hex_string '-' ist,
        # wird das erste Zeichen aus hex_string geloescht und is_negative auf True gesetzt.
        if hex_string[0]  == '-':
            hex_string = hex_string[1:len(hex_string)]
            is_negative = True

        # wenn hex_string die Laenge 0 hat , wird eine Fehlermeldung ausgegeben und
        # -1 zurueckgegeben.
        if len(hex_string) == 0:
            print("falsche Eingabe fuer hex_string")
            return -1

        # prod wird mit 0 belegt.
        prod  = 0
        # ret wird mit 0 belegt.
        ret  = 0
        # while-loop mit der Abbruchbedingung len(hex_string) > 0 wird erstellt
        while(len(hex_string) > 0):
            # das letzte Zeichen der hex_string wird der digit_str zugewiesen.
            digit_str = hex_string[len(hex_string)-1]
            # digit_str wird nach Hex-Ziffer umgewandelt und in digit gespeichert.
            digit = self.convert_hex_str_to_hex_digit(digit_str)
            # das letzte Zeichen wird aus hex_string geloescht.
            hex_string = hex_string[0:len(hex_string)-1]
            # ret = ret + digit*(16^prod)
            ret += digit*pow(16, prod)
            # prod wird um 1 erhoeht.
            prod += 1

        # wenn is_negative wahr ist  , wird ret negiert.
        if is_negative:
            ret = -ret

        # ret wird in String umgewandelt und in die tracker hinzugefuegt.
        tracker.append(str(ret))
        # "H" und "I" werden in die tracker hinzugefuegt
        tracker.append("H")
        tracker.append("I")
        # tracker wird im geeigneten Format in die geschichte hinzugefuegt.
        geschichte.append("("+",".join(tracker)+")")
        # ret wird zurueckgegeben.
        return ret



    # convert_int_digit_to_rom_str
    # Konvertierung Integer Dezimalziffer nach roemischem Zeichen
    # Arguments: 1) Dezimalziffer
    # 2) Position der Dezimalziffer in der Zahl
    # Rueckgabewert: roemisches Zeichen
    def convert_int_digit_to_rom_str(self, digit, place):
        # wenn place == 1
        if place == 1:
            # I, II oder III
            if digit >= 1 and digit <= 3:
                return 'I'*digit
            # IV
            elif digit == 4:
                return 'IV'
            # V, VI, VII, oder VIII
            elif digit >= 5 and digit <= 8:
                return 'V' + 'I'*(digit-5)
            # IX
            elif digit == 9:
                return 'IX'

        # wenn place == 10
        if place == 10:
            # X, XX , oder XXX
            if digit >= 1 and digit <= 3:
                return 'X'*digit
            # XL
            elif digit == 4:
                return 'XL'
            # L, LX, LXX, oder LXXX
            elif digit >= 5 and digit <= 8:
                return 'L' + 'X'*(digit-5)
            # XC
            elif digit == 9:
                return 'XC'
        # wenn place == 100
        if place == 100:
            # C, CC , CCC
            if digit >= 1 and digit <= 3:
                return 'C'*digit
            # CD
            elif digit == 4:
                return 'CD'
            # D, DC, DCC, oder DCCC
            elif digit >= 5 and digit <= 8:
                return 'D' + 'C'*(digit-5)
            # CM
            elif digit == 9:
                return 'CM'




    # partial_int_zu_rom
    # Konvertierung der 3-stelligen Integer Dezimalzahl nach roemischer Zahl
    # Argument: 3-stellige Integer Dezimalzahl
    # Rueckgabewert: roemische Zahl
    def partial_int_zu_rom(self, int_num):
        # eine leere String namens ret wird erstellt.
        ret = ''
        # place wird mit 1 belegt.
        place = 1
        # while-loop mit Abbruchbedingung int_num > 0 erstellt
        while int_num > 0:
            # Das Ergebnis der Operation: int_num modulo 10 wird in der rest gespeichert
            rest = int_num % 10
            # wenn rest == 0 place wird mit 10 multipliziert , int_num wird mit 10 ganzzahlig
            # dividiert und Programm-Kontrolle wird an das erste Statement der while-Schleife
            # gesprungen
            if rest == 0:
                place *= 10
                int_num //= 10
                continue

            # rest wird nach rom-String umgewandelt , mit der ret zusammentadditiert und
            # der ret zugewiesen.
            ret = self.convert_int_digit_to_rom_str(rest, place) + ret
            # place wird mit 10 multipliziert
            place *= 10
            # int_num wird mit 10 ganzzahlig dividiert
            int_num //= 10

        # ret wird zurueckgegeben.
        return ret

    # int_zu_rom
    # Konvertierung der Integer Dezimalzahl nach roemischer Zahl
    # Argument: Integer Dezimalzahl
    # Rueckgabewert: roemische Zahl
    def int_zu_rom(self, int_num):
        # is_negative wird mit False belegt.
        is_negative = False
        # regex wird eingesetzt , um die Gueltigkeit der Eingabe zu ueberpruefen
        pattern = "^-?[0-9]+$"
        prog = re.compile(pattern)
        # wenn die Eingabe ungueltig ist , wird Fehlermeldung ausgegeben und -1 zurueckgegeben.
        if not prog.match(str(int_num)):
            print("Ungueltige Eingabe , nur Integer-Zahlen(positive oder negative) sind erlaubt.")
            return -1

        # int_num wird in Integer umgewandelt.
        int_num = int(int_num)
        # wenn int_num == 0 , wird geeignete Berechnung in geschichte hinzugefuegt und
        # NULLUM zurueckgegeben.
        if int_num == 0:
            geschichte.append("(0,NULLUM,I,R)")
            return "NULLUM"

        # int_num wird der temp_num zugewiesen.
        temp_num = int_num
        # wenn int_num negative ist , wird temp_num negiert und is_negative auf True gesetzt.
        if int_num < 0:
            temp_num = -int_num
            is_negative = True

        # eine leere String names ret wird belegt.
        ret = ''
        # factor wird auf 0 gesetzt.
        factor = 0
        # thousand_part wird mit '.M' belegt.
        thousand_part = '.M'
        # while-Schleife mit Abbruchbedingung temp_num > 0 erstellt.
        while(temp_num > 0 ):
            # Das Ergebnis der Operation temp_num modulo 1000 wird in der rest gespeichert.
            rest = temp_num % 1000
            # temp_num wird mit 1000 ganzzahlig dividiert.
            temp_num //= 1000
            # rest wird nach roemischer Zahl umgewandelt , 
            # thousand_part wird mit factor multipliziert (in String factor mal mit sich selbst 
            # konkateniert) 
            # diese Zwischenergebnisse und ret werden zusammenaddiert , und das Ergebnis wird 
            # in der ret gespeichert.
            ret = self.partial_int_zu_rom(rest) + thousand_part*factor +' ' + ret
            # factor wird um 1 erhoeht.
            factor += 1

        # wenn is_negative wahr ist , wird Minuszeichen in ret vorangestellt
        if is_negative:
            ret = '-' + ret

        # das letzte leere Zeichen wird aus ret entfernt
        ret = ret[0:len(ret)-1]

        # Berechnung wird im geeigneten Format in die geschichte hinzugefuegt.
        tracker = [str(int_num), ret, "I", "R"]
        geschichte.append("(" + ",".join(tracker) + ")")
        
        # ret wird zurueckgegeben.
        return ret




    # partial_rom_zu_int
    # Konvertierung roemischer Zahl bis dem Wert 999 im Dezimalsystem (einschliesslich) 
    # nach Integer Dezimalzahl
    # Argument: roemische Zahl bis dem Wert 999 im Dezimalsystem
    # Rueckgabewert: Integer Dezimalzahl
    def partial_rom_zu_int(self, rom_string):
        # prev wird mit 0 belegt.
        prev = 0
        # ret wird mit 0 belegt. 
        ret = 0
        # while-Schleife mit Abbruchbedingung rom_string > 0 wird erstellt.
        while len(rom_string) > 0:
            # Das erste Zeichen der rom_string wird in rom_digit_str gespeichert.
            rom_digit_str = rom_string[0]
            # Das erste Zeichen wird aus der rom_string geloescht.
            rom_string = rom_string[1:len(rom_string)]
            # der Wert der Instanz-Variable rom_map fuer den Schluesse rom_digit_str wird in der 
            # curr gespeichert.
            curr = self.rom_map[rom_digit_str]
            # ret wird um curr erhoeht.
            ret += curr
            # wenn prev kleiner als curr ist , wird ret um 2*prev erniedrigt.
            if prev < curr:
                ret -= 2 * prev

            # curr wird der prev zugewiesen.
            prev = curr
            
        # ret wird zurueckgegeben.
        return ret

   
    # rom_zu_int
    # Konvertierung der roemischen Zahl nach Integer Dezimalzahl
    # Argument: roemische Zahl
    # Rueckgabewert: Integer Dezimalzahl
    def rom_zu_int(self, rom_string):
        # is_negative wird auf False gesetzt.
        is_negative = False
        # wenn rom_string == "NULLUM" , wird geeignete Berechnung in die geschichte hinzugefuegt 
        # und 0 zurueckgegeben.
        if rom_string == "NULLUM":
            geschichte.append("("+rom_string+ ",0,R,I)")
            return 0

        # tracker Liste wird mit einzigem Element rom_string belegt.
        tracker = [rom_string]

        # regex wird eingetzt , um die Gueltigkeit der Eingabe zu ueberpruefen.
        pattern = "^-?[I|V|X|L|C|D|M|.|\s]+$"
        prog = re.compile(pattern)
        # wenn die Eingabe nicht gueltig ist , wird Fehlermeldung ausgegeben und -1 zurueckgegeben.
        if not prog.match(rom_string):
            print("rom_string darf nur 'I', 'V', 'X', 'L', 'C', 'D', 'M', '.', oder Leerzeichen enthalten.")
            return -1

        # wenn das erste Zeichen der rom_string Minuszeichen ist , 
        # wird is_negative auf True gesetzt und das erste Zeichen aus der rom_string entfernt.
        if rom_string[0] == '-':
            is_negative = True
            rom_string = rom_string[1:len(rom_string)]

        # wenn Laenge der rom_string == 0 , wird Fehlermeldung ausgegeben und -1 zurueckgegeben.
        if len(rom_string) == 0:
            print("ungueltige Eingabe fuer rom_string")
            return -1

        # ret wird mit 0 belegt.
        ret = 0
        # rom_string wird nach dem einzigen Leerzeichen aufgesplitted und das Ergebnis wird in 
        # thousand_places gespeichert.
        thousand_places = rom_string.split(" ")
        # thousand_places wird iteriert.
        for thousand_place in thousand_places:
            # thousand wird nach dem Zeichen "." aufgesplitted und das Ergebnis wird in splitted
            # gespeichert.
            splitted = thousand_place.split(".")
            # Bedeutet: factor = 1000^ (len(splitted) -1))
            factor = int(pow(1000, len(splitted)-1))
            # splitted[0] wird nach Integer Dezimalzahl umgewandelt ,mit factor multupliziert , 
            # und der ret addiert.
            ret += self.partial_rom_zu_int(splitted[0])*factor

        # wenn is_negative wahr ist , wird ret negiert.
        if is_negative:
            ret = -ret

        # ret wird nach String umgewandelt und in tracker hinzugefuegt.
        tracker.append(str(ret))
        # "R" und "I" werden in tracker hinzugefuegt.
        tracker.append("R")
        tracker.append("I")
        # tracker wird im geeigneten Format in geschichte hinzugefuegt.
        geschichte.append("(" + ",".join(tracker) + ")")
        # ret wird zurueckgegeben.
        return ret





