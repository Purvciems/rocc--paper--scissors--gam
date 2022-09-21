hooman_t = input('Input Hooman turn: ')
computer_t = 'scissors'

if hooman_t == computer_t:
    print('Draw?')
elif hooman_t == 'rock' and computer_t == 'scissors':
    print('Human wins lol')

elif hooman_t == 'paper' and computer_t == 'rock':
    print('Human wins lol')
    
elif hooman_t == 'scissors' and computer_t == 'paper':
    print('Human wins lol')
else:
    ('PC WINS HAHAHA')
