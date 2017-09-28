import numpy as np 

def generateMatrix(rank=4,seed=None,singular=False):
    np.random.seed(seed)
    while True:
        matrix = np.random.randint(-10,10, size=(rank, rank))
        if (np.linalg.matrix_rank(matrix) != rank) ^ (not singular):
            return matrix

def printInMatrixFormat(Ab):
    rank = len(Ab)
    rowFormat = ','.join(["{:>7.3f}"] * rank) + " || {:<7.3f}"     
    matrixFormat = '\n'.join([rowFormat] * rank)

    flattern = [e for row in Ab for e in row]

    print(matrixFormat.format(*flattern))


def generatePoints(seed=None,num=100):
    np.random.seed(seed)
    m = np.random.random() * 10 - 5 # -5 ~ 5
    b = np.random.random() * 10 + 5 # 5 ~ 15

    x = np.random.random(size=num) * 10 - 5
    y = x * m + b 
    y += np.random.normal(size=num)

    return x.tolist(),y.tolist()

