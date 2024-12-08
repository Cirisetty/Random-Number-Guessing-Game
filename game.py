import random

attempts_list = []

def start_game():
    attempts = 0
    num = random.randint(1, 15)
    print('Welcome to the game of guesses!')
    player = input('PLEASE ENTER YOUR NAME: ')
    toplay = input(f'Hi {player}, would you like to play the guessing game? (Enter Yes/No): ')
    
    if toplay.lower() != 'yes':
        print('Thanks for visiting!')
        exit()
    
    while toplay.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 15: '))
            if guess < 1 or guess > 15:
                raise ValueError('Please guess a number within the given range.')
            attempts += 1
            if guess == num:
                print('You got it!')
                print(f'It took you {attempts} attempts.')
                attempts_list.append(attempts)
                toplay = input('Would you like to play again? (Enter Yes/No): ')
                if toplay.lower() != 'yes':
                    print('Thanks for playing!')
                    break
                else:
                    attempts = 0
                    num = random.randint(1, 15)
            else:
                if guess > num:
                    print('Your guess is too high!')
                elif guess < num:
                    print('Your guess is too low!')
        except ValueError as err:
            print('It is not a valid value.')
            print(err)

if __name__ == '__main__':
    start_game()
