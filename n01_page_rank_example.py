import numpy as np

M = [[0, 0, 0],
     [1, 0, 0],
     [0, 1, 1]]
U = [1 / 3, 1 / 3, 1 / 3]

# 初始矩阵
U0 = np.array(U)
# 转移概率矩阵
M = np.array(M)

print(M.T)
print('公式中没有加阻尼系数alpha...')
U_past_none_alpha = []
while True:
	U = np.dot(M, U)
	print('Un: ', U)
	if str(U) == str(U_past_none_alpha):
		break
	U_past_none_alpha = U
print('收敛: ', U)

print('公式中加阻尼系数alpha, 令alpha=0.85...')
U_past_has_alpha = []
while True:
	U = 0.85 * (np.dot(M, U)) + 0.15 * U0
	# print('Un: ', U)
	if str(U) == str(U_past_has_alpha):
		break
	U_past_has_alpha = U
print('收敛: ', U)
