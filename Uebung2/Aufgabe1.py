import random
lower_bound = 1
upper_bound = 20
random_number = random.randint(lower_bound, upper_bound)

guessed = False

guess = int(input("Gib deine Zahl [1, 20] ein: "))
if guess > random_number:
    print("Deine Zahl ist groesser.")
elif guess < random_number:
    print("Deine Zahl ist kleiner.")
else:
    print("Du hast richtig geraten.")
    guessed = True

if guessed == False:
    guess = int(input("Gib deine Zahl [1, 20] ein: "))
    if guess > random_number:
        print("Deine Zahl ist groesser.")
    elif guess < random_number:
        print("Deine Zahl ist kleiner.")
    else:
        print("Du hast richtig geraten.")
        guessed = True



if guessed == False:
    guess = int(input("Gib deine Zahl [1, 20] ein: "))
    if guess > random_number:
        print("Deine Zahl ist groesser.")
    elif guess < random_number:
        print("Deine Zahl ist kleiner.")
    else:
        print("Du hast richtig geraten.")
        guessed = True


if guessed == False:
    print("Du hast verloren.")
    print("Deine Zahl war ", guess,".", sep = "")