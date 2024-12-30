import random
secret_number = random.randint(1, 10)

#prompting the user for a guess

guess = int(input("I'm thinking of a number between 1 to 10. Can you guess it? "))

#using the match case conditionals

match guess:
    case 5:
        print("Nop,your guess is a bit low.Give it another short.")
    case 7:
        print("Congradulation you guessed it correct!")

# prompting the user if they'll want to contunue with the game or not

new_game = input(" new game? ")
message = "yes"
if new_game == message:
    print("new game starts")
else:
    print("thanks for giving it a try.")

         