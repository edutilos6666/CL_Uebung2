import konverter


k = konverter.konverter()
input = 123 # 7B
print(k.int_zu_hex(input))
input = 123123 # 1E0F3
print(k.int_zu_hex(input))
input = 123123123 # 756B5B3
print(k.int_zu_hex(input))

input = -123 # -7B
print(k.int_zu_hex(input))
input = -123123 # -1E0F3
print(k.int_zu_hex(input))
input = -123123123 # -756B5B3
print(k.int_zu_hex(input))


input = "7B" # 123
print(k.hex_zu_int(input))
input = "1E0F3" # 123123
print(k.hex_zu_int(input))
input = "756B5B3" # 123123123
print(k.hex_zu_int(input))

input = "-7B" # -123
print(k.hex_zu_int(input))
input = "-1E0F3" # -123123
print(k.hex_zu_int(input))
input = "-756B5B3" # -123123123
print(k.hex_zu_int(input))


input = 123 # CXXIII
print(k.int_zu_rom(input))
input = 123123 # CXXIII.M CXXIII
print(k.int_zu_rom(input))
input = 123123123 # CXXIII.M.M CXXIII.M CXXIII
print(k.int_zu_rom(input))

input = -123 # -CXXIII
print(k.int_zu_rom(input))
input = -123123 # -CXXIII.M CXXIII
print(k.int_zu_rom(input))
input = -123123123 # -CXXIII.M.M CXXIII.M CXXIII
print(k.int_zu_rom(input))


input = "CXXIII" # 123
print(k.rom_zu_int(input))
input = "CXXIII.M CXXIII" # 123123
print(k.rom_zu_int(input))
input = "CXXIII.M.M CXXIII.M CXXIII" # 123123123
print(k.rom_zu_int(input))

input = "-CXXIII" # -123
print(k.rom_zu_int(input))
input = "-CXXIII.M CXXIII" # -123123
print(k.rom_zu_int(input))
input = "-CXXIII.M.M CXXIII.M CXXIII" # -123123123
print(k.rom_zu_int(input))

print(k.int_zu_hex(0))
print(k.hex_zu_int("0"))
print(k.int_zu_rom(0))
print(k.rom_zu_int("NULLUM"))
print("\n".join(konverter.geschichte))
print(len(konverter.geschichte))



res1 = "CXXIII.M.M CXXIII.M CXXIII"
res2 = k.int_zu_rom(123123123)
print(res1, res2)
print(len(res1), len(res2))

res1 = "756B5B3"
res2 = k.int_zu_hex(123123123)
print(res1, res2)
print(len(res1), len(res2))