import re

# Top-Level-Statement
print('module konverter meldet sich an.')
geschichte = []



class konverter:

    def __init__(self):
        geschichte.append("Konstruktor wurde aufgerufen.")
        self.hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        self.reverse_hex_map = {'A':10,'B':11 , 'C':12, 'D':13, 'E':14, 'F':15}
        self.rom_map = {'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def __del__(self):
        geschichte.append("Destruktor wurde aufgerufen.")



    def convert_hex_digit_to_str(self, digit):
        if digit >= 0 and digit <= 9:
            return str(digit)
        elif digit >= 10 and digit <= 15:
            return self.hex_map[digit]


    def convert_hex_str_to_hex_digit(self, str):
        if str in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(str)
        elif str.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
            return self.reverse_hex_map[str.upper()]




    def int_zu_hex(self, int_num):
        geschichte.append("int_zu_hex() wurde aufgerufen.")
        digits = []
        temp_num = int_num if int_num > 0 else -int_num
        while temp_num > 0 :
            rest = temp_num % 16
            temp_num = temp_num // 16
            digits.append(rest)

        digits = reversed(digits)
        ret = ''
        for digit in digits:
            ret += self.convert_hex_digit_to_str(digit)

        return ret



    def hex_zu_int(self, hex_string):
        geschichte.append("hex_zu_int() wurde aufgerufen.")
        pattern = "[^0-9a-fA-F]+"
        prog = re.compile(pattern)
        if prog.search(hex_string):
            print('hex_string darf Ziffer, "a" bis "z" , "A" bis "Z" enthalten')
            return -1

        ret = -1
        if len(hex_string) < 0:
            return ret

        prod  = 0
        ret  = 0
        while(len(hex_string) > 0):
            digit_str = hex_string[len(hex_string)-1]
            digit = self.convert_hex_str_to_hex_digit(digit_str)
            print(len(hex_string))
            hex_string = hex_string[0:len(hex_string)-1]
            ret += digit*pow(16, prod)
            prod += 1
        return ret




    def convert_int_digit_to_rom_str(self, digit, place):
        if place == 1:
            if digit >= 1 and digit <= 3:
                return 'I'*digit
            elif digit == 4:
                return 'IV'
            elif digit >= 5 and digit <= 8:
                return 'V' + 'I'*(digit-5)
            elif digit == 9:
                return 'IX'

        if place == 10:
            if digit >= 1 and digit <= 3:
                return 'X'*digit
            elif digit == 4:
                return 'XL'
            elif digit >= 5 and digit <= 8:
                return 'L' + 'X'*(digit-5)
            elif digit == 9:
                return 'XC'

        if place == 100:
            if digit >= 1 and digit <= 3:
                return 'C'*digit
            elif digit == 4:
                return 'CD'
            elif digit >= 5 and digit <= 8:
                return 'D' + 'C'*(digit-5)
            elif digit == 9:
                return 'CM'

        if place == 1000:
            if digit >= 1 and digit <= 3:
                return 'M'*digit




    def int_zu_rom(self, int_num):
        geschichte.append("int_zu_rom() wurde aufgerufen.")
        if int_num > 3999:
            print("int_num muss <= 3999 und > 0 sein.")
            return -1

        temp_num = int_num if int_num > 0 else -int_num
        if temp_num == 0 :
            print("int_num kann nicht 0 sein.")
            return -1

        ret = ''
        place = 1
        while temp_num > 0 :
            rest = temp_num % 10
            if rest == 0:
                place *= 10
                temp_num //= 10
                continue

            ret = self.convert_int_digit_to_rom_str(rest, place) + ret
            place *= 10
            temp_num //= 10

        return ret

    def rom_zu_int(self, rom_string):
        geschichte.append("rom_zu_int() wurde aufgerufen.")
        pattern = "[^I|V|X|L|C|D|M]+"
        prog = re.compile(pattern)
        if prog.search(rom_string):
            print("rom_string darf nur 'I', 'V', 'X', 'L', 'C', 'D', 'M' enthalten.")
            return -1

        prev = 0
        ret = 0
        while len(rom_string) > 0 :
            rom_digit_str = rom_string[0]
            rom_string = rom_string[1:len(rom_string)]
            curr = self.rom_map[rom_digit_str]
            ret += curr
            if prev < curr:
                ret -= 2*prev


            prev = curr

        return ret



