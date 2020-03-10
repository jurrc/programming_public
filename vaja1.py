

def func(d, m):
    if m in (1, 2, 3):
        if m == 3 and d >= 21:
            funcpom(d, m)
        else:
            print('zima')
    else:
        funcpom(d, m)

def funcpom(d, m):
    if m in (4, 5, 6):
        if m == 6 and d >= 21:
            funcpol(d, m)
        else:
            print('pomlad')
    else:
        funcpol(d, m)

def funcpol(d, m):
    if m in (7, 8, 9):
        if m == 9 and d >= 23:
            funcjes(d, m)
        else:
            print('poletje')
    else:
        funcjes(d, m)

def funcjes(d, m):
    print('jesen')

func(int(input('dan >> ')), int(input('mesec >> ')))

