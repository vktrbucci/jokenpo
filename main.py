import random

print('''Shall we play JoKenPo?

1. Rock
2. Paper
3. Scissors
''')

player = int(input('Make your move: '))


if player == 1:
    pc = random.choice(['Rock', 'Paper', 'Scissors'])
    print('My move is {}.'.format(pc))
    if pc == 'Rock':
        print('''
        You played Rock.
        Draw.''')
    elif pc == 'Paper':
        print('''
        It's so cute you played rock...
        I win bitch!
        Your ass is mine NOW!
        MWAHAHAHAHAHAHA''')
    else:
        print('''
        You played Rock.
        You win.''')
elif player == 2:
    pc = random.choice(['Rock', 'Paper', 'Scissors'])
    print('My move is {}.'.format(pc))
    if pc == 'Rock':
        print('''
        You played Paper.
        You win.''')
    elif pc == 'Paper':
        print('''
        You played Paper.
        Draw.''')
    else:
        print('''
        Trying your luck with Paper?
        So you think you can win?
        Mwahahahahaha
        Don't make me laugh, scrub...
        I OWN YOU!!!!''')
elif player == 3:
    pc = random.choice(['Rock', 'Paper', 'Scissors'])
    print('My move is {}.'.format(pc))
    if pc == 'Rock':
        print('''
        So you played Scissors?
        Hah! It must be frustrating for you not being able to beat me with your tiny little brain.
        Guess what, you monkey...
        I'll mind-rape you because you are nothing to me!
        MWAHAHAHAHAHAHAHAHAHA''')
    elif pc == 'Paper':
        print('''
        You played Scissors.
        You win.''')
    else:
        print('''
        You played Scissors.
        Draw.''')
else:
    print('''
    You can't even understand the rules.
    Come back here after you finish your morning milk.
    After all, babies in diapers shouldn't be playing games.''')
