import konverter


rom_string = "CMXCIX*M*M CMXCIX*M CMXCIX"

k = konverter.konverter()
res = k.rom_zu_int(rom_string)
print(res)


int_num = 999999999999
print(k.int_zu_rom(int_num))
int_num = 666
print(k.int_zu_rom(int_num))
int_num = 666666
print(k.int_zu_rom(int_num))
int_num = -666666666
print(k.int_zu_rom(int_num))


int_num = 123
print(k.int_zu_hex(int_num))
hex_string = "-ABCDEF"
print(k.hex_zu_int(hex_string))
print(k.hex_zu_int("0"))
print(k.int_zu_hex(0))
print(k.int_zu_rom(0))
print(k.rom_zu_int("NULLUM"))
print("\n".join(konverter.geschichte))


