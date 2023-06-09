import numpy as np
from math import inf

# matrice de poids non orienté
MV = np.array([[inf, 2, 4, 3, 6],
               [2, inf, 7, inf, inf],
               [4, 7, inf, 2, 8],
               [3, inf, 2, inf, 1],
               [6, inf, 8, 1, inf]], dtype="object")




def prim(MV):
    arbre = np.full((len(MV), len(MV)), inf)
    marque = [0]
    while(len(marque) < len(MV)):
        list_x_m = []
        for m in marque:
            x = min(MV[m])
            list_x_m.append((x, m))

        x_temp = []
        for e in list_x_m:
            x_temp.append(e[0])

        x = min(x_temp)
        for e in list_x_m:
            if e[0] == x:
                m = e[1]
                break

        y = np.where(MV[m] == x)[0][0]

        if y not in marque:
            marque.append(y)

        arbre[m][y] = x
        arbre[y][m] = x

        MV[m][y] = inf
        MV[y][m] = inf

    return arbre

#print(prim(MV))
