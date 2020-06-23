#Greetings
print("Hi there! Welcome to Monica's first coding project, 'The Python Number Guessing Game'!")
print("Let's see if you can guess the number in fewer steps than the computer openent. Let's begin!")

#Computer Function
def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # If guess is in the middle, it is found
        if guess == randnum:
            return count
        #If 'guess' is greater than the number it must be
        #found in the lower half of the set of numbers
        #between the lower value and the guess.
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)

        #The number must be in the upper set of numbers
        #between the guess and the upper value
        else:
            count + 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        #Number not found
        return -1
#End of function        

#Generate a random number between 1 and 100
import random
randnum = random.randint(1,101)


count = 0
guess = -99

while (guess != randnum):
    #Get the user's guess
    guess = (int) (input("Enter your guess between 1 and 100:"))
    if guess < randnum:
        print("You need to guess higher")
    elif guess > randnum:
        print("Not quite! Try guessing lower")
    else:
        print("Congratulations! You guessed right!")
        break
    count = count + 1
#End of while loop

print("You took " + str(count) + " steps to guess the number")
print("The computer guessed it in " + str(computerGuess(0,100, randnum)) + " steps")
input("Press Enter to close program")