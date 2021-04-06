def readmatrix(file):
    f = open(file, "r")
    mat = []
    matint = []
    for i in f:
        mat.append(i.split(' '))

    for i in mat:
        for n in i:
            if '\n' in n:
                i[i.index(n)] = n[:-1]
                matint.append(list(map(int, i)))

    print(*matint, sep='\n')
    print('\n')
    return matint


def lab1(file):
    matint = readmatrix(file)
    points = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    first = 'a'
    uses = []

    uses.append(first)
    while len(uses) != len(points):
        maxi = []
        for i in uses:
            if points[matint[points.index(i)].index(max(matint[points.index(i)]))] not in uses:
                maxi.append(max(matint[points.index(i)]))
            else:
                maxi.append(0)
        k = max(maxi)
        a = points[matint[points.index(uses[maxi.index(k)])].index(k)]
        line = points.index(uses[maxi.index(k)])
        elem = matint[points.index(uses[maxi.index(k)])].index(k)
        matint[line][elem] = 0
        matint[elem][line] = 0
        print(uses[maxi.index(k)] + ' --> ' + a, k)
        if a not in uses:
            uses.append(a)
