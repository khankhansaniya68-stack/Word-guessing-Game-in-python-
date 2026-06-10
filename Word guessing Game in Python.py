import random 

name = input("What is your name? ")

print("Good Luck! ", name)

words = ['Saniya','Apple','Rainbow', 'Computer', 'Science', 'Proggramming', 'Python', 'Mathematics', 'Football', 'Player', 'Condition', 'Reverse', 'Water', 'Board', 'Geeks', 'Cat','Dog', 'Egg','Fish','Hen','Icecream']

word = random.choice(words)

print("Guess the Characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")

        else:
            print("_", end="a")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")

