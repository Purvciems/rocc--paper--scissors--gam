import random
turn = ['rock', 'paper', 'scissors']

while True:
    hooman_t = input('Input Hooman turn or exit: ')
    if hooman_t == 'exit':
        print('ok goodbye')
        break
    computer_t = random.choice(turn)
    print(f'Human: {hooman_t} vs Computer: {computer_t}')
    

    if hooman_t == computer_t:
        print('Draw?')
    elif hooman_t == 'rock' and computer_t == 'scissors':
        print('Human wins lol')

    elif hooman_t == 'paper' and computer_t == 'rock':
        print('Human wins lol')
    
    elif hooman_t == 'scissors' and computer_t == 'paper':
        print('Human wins lol')
    else:
        print('PC WINS HAHAHA')
