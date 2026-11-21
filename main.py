
import random

print("::::::: Welcome to Number guessing Game :::::::")
print("Rules: \n",
"Number range only from 1 - 100. \n",
"No letters are allowed. \n",
"Choose one number at a time.\n"
)
while True:
    try:
        difficulty = int(input("Choose difficulty: \n 1 : Easy \n 2 : Medium \n 3 : Hard \n => "))
        break
    except:
        print("Invalid input, Choose from 1 -3 ...")

if difficulty == 3:
    print("==== You have 3 atempts ====")
    chances = 3
elif difficulty == 2:
    print("==== You have 5 atempts ====")
    chances = 5
elif difficulty == 1:
    print("==== You have 10 atempts ====")
    chances = 10
else:
    print("Invalid Value.")
    exit()

option = "y"

while option == "y":
    number = random.randint(1, 100)

    count = 0
    while count < chances:
        print(f"\nAttempts remaining: {chances - count}")

        while True:
            try:
                guess = int(input("Choose your lucky number: "))
                break
            except:
                print("Choose number from 1- 100.")

        if number == guess:
            print(f"Wow, You got it right.! \n The number was {number}")
            break
        else:
            count = count + 1
            if number > guess:
                print("Number is less than your Guess !")
            else:
                print("number is Greater thn your Guess !")

    option = input(" \n Do you want to continue? y/n ")
