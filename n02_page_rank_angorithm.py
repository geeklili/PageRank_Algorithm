import numpy as np

# Building matrix M, M is a square matrix（方阵）
# The first row of M is the probability of A, B, C ，...linked to A
# and the second row is the probability that A, B, C will be linked to B
M = [[0, 0, 0],
     [1, 0, 0],
     [0, 1, 1]]
M = np.array(M)

a, b = M.shape
print(a, b)
U = [1 / 3, 1 / 3, 1 / 3]

U0 = np.array(U)

U_past = []
while True:
    U = 0.85 * (np.dot(M, U)) + 0.15 * U0
    # print('Un: ', U)
    if str(U) == str(U_past):
        break
    U_past = U
print('Un converge to: ', U)
