import random, sys

print('ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.

choices = {'r': 'rock', 's':'scissors', 'p': 'paper'}
user_choices = ('r', 'p', 's', 'q')
computer_choices = ('r', 'p', 's')
win_lose = {
    'rr': 'tie', 'rs': 'win', 'rp': 'lose',
    'ss': 'tie', 'sp': 'win', 'sr': 'lose',
    'pp': 'tie', 'pr': 'win', 'ps': 'lose'
}
result = {'win': 0, 'lose': 0, 'tie': 0}

while True:
    print('%s Wins, %s Losses, %s Ties' % (result['win'], result['lose'], result['tie']))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove in user_choices:
            break
    if playerMove == 'q':
        exit()
    computerMove = computer_choices[random.randint(0, 2)]
    print('%s versus %s ....'% (choices[playerMove], choices[computerMove]))
    print('You %s'% win_lose[playerMove+computerMove])
    match win_lose[playerMove+computerMove]:
        case 'win':
            result['win'] += 1
        case 'lose':
            result['lose'] += 1
        case 'tie':
            result['tie'] += 1
    print("===================================")