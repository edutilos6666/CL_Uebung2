# Programmieren Sie einen kleinen Taschenrechner. Der Nutzer wird
# aufgefordert, in der Shell einen zu berechnenden Ausdruck
# einzugeben, z.B. 2+4. Dabei koennen alle built-in Operatoren genutzt
# werden. Bieten Sie zudem an, das Ergebnis gemaess Nutzereingabe zu
# runden und geben Sie es anschliessend aus.


a = None
b = None
res = None
op = None

a = float(input("Gib die erste Zahl ein: "))
b = float(input("Gib die zweite Zahl ein: "))
op = input("Gib den Operator ein: ")

if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
elif op == "**":
    res = a ** b
elif op == "%":
    res = a % b



print(a, op , b , " = ", res)

