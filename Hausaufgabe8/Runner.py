import konverter_v1


k1 = konverter_v1.konverter()
k1.int_zu_rom(123)
print(konverter_v1.geschichte)


int_num = 12345677
print(k1.int_zu_hex(int_num))

hex_string = '7B'  #123
hex_string = "BC614D" #12345677
print(k1.hex_zu_int(hex_string))



int_num = 2014 # MMXIV
print(k1.int_zu_rom(int_num))
int_num = 3999 # MMMCMXCIX
print(k1.int_zu_rom(int_num))
# int_num = 4000 # error
# print(k1.int_zu_rom(int_num))


hex_string = "123fe"
print(k1.hex_zu_int(hex_string))

rom_string = "MMXIV"
print(k1.rom_zu_int(rom_string))  # 2014
rom_string = "MMMCMXCIX"
print(k1.rom_zu_int(rom_string)) # 3999



rom_string = "MCCXXXIV" # 1234
print(k1.rom_zu_int(rom_string))
int_num = 1234 # MCCXXXIV
print(k1.int_zu_rom(int_num))

