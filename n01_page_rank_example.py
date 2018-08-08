import numpy as np

M = [[0, 0, 0],
     [1, 0, 0],
     [0, 1, 1]]
U = [1 / 3, 1 / 3, 1 / 3]

U0 = np.array(U)

print('The alpha parameter is not used in the formula...')
U_past_none_alpha = []
while True:
    U = np.dot(M, U)
    # print('Un: ', U)
    if str(U) == str(U_past_none_alpha):
        break
    U_past_none_alpha = U
print('Un converge to: ', U)

print('The alpha parameter is not used in the formula, and the value of alpha is 0.85...')
U_past_has_alpha = []
while True:
    U = 0.85 * (np.dot(M, U)) + 0.15 * U0
    # print('Un: ', U)
    if str(U) == str(U_past_has_alpha):
        break
    U_past_has_alpha = U
print('Un converge to: ', U)
