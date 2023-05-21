import random
while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input('rock, paper, scissors?:').lower()
    if player == computer:
        print('Computer: ', computer)
        print('Players: ', player)
        print('Tie')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ', computer)
            print('Players: ', player)
            print('you lose')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Players: ', player)
            print('You win')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer: ', computer)
            print('Players: ', player)
            print('you lose')
        if computer == 'paper':
            print('Computer: ', computer)
            print('Players: ', player)
            print('You win')
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Players: ', player)
            print('you lose')
        if computer == 'rock':
            print('Computer: ', computer)
            print('Players: ', player)
            print('You win')
    play_again = input("Play again? (Yes/no): ").lower()
    if play_again != 'yes':
        break
print('Bye')