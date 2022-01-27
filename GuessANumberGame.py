import random

def StartGame():
    low = 1
    high = 10000
    personalBest = 100000

    print('Welcome!')
    while True:
        PrintMenu() 
        selection = input()
        if selection == '2':
            break
        if selection == '1':
           personalBest = PlayGame(personalBest, low, high)
        if selection == '3':
            low = ChangeLow()
            high = ChangeHigh(low)
            print('Range changed to ' + str(low) + ' to ' + str(high))
            personalBest = 100000
    print('Bye')
    
def PlayGame(personalBest, low, high):
    print('Guess a number between ' + str(low) + ' and ' + str(high))    
    number = random.randint(low,high)
    tries = 0
    while True:
        guess = input()
        if not guess.isdigit():
            continue

        tries += 1
        if int(guess) > number:
            print(guess + ' was too high')
        if int(guess) < number:
            print(guess + ' was too low')
        if int(guess) == number:
            print('You are right!')
            print('The number was ' + str(number))
            print('Took you ' + str(tries) + ' tries to find it')
            if tries < personalBest:
                print('New Personal best ' + str(tries) +' tries, last best was ' + str(personalBest))
                return tries
            else:
                print('Your personal best is ' +str(personalBest) + ' tries')
            return personalBest


def ChangeLow():
    newLow=''
    while True:
        print('Input new low')
        newLow = input()
        if(newLow.isnumeric()):
            return int(newLow)

def ChangeHigh(low):
    newHigh = ''
    while True:
        print('Input new high')
        newHigh = input()
        if newHigh.isnumeric():
            if int(newHigh) > low:
                return int(newHigh)
            else:
                print('New high must be higher then ' + str(low))
       
def PrintMenu():
    print('Select option')
    print('1. Play')
    print('2. Quit')
    print('3. Change Low and High')

StartGame()
