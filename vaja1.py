


def func(d, m):
    if m in (1, 2, 3):
        print('zima')
    elif m in (4, 5, 6):
        print('pomlad')
    elif m in (7, 8, 9):
        print('poletje')
    else:
        print('jesen')

func(int(input('dan >> ')), int(input('mesec >> ')))
