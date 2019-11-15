import matplotlib.pyplot as plt
import math


# tanh函数改装成[0，1]之间的衰减函数
# 调整这个参数可以在横向上获取到更多的tanh函数的信息
BIG_ARG = 10
# 调整这个参数可以拉开y的差距
SMALL_ARG = 2


def tanh_change(i):
    return (0.5 * (math.tanh(((1 - i) * BIG_ARG - 2.2)) + 1)) ** SMALL_ARG


def tanh_derivative(i):
    return (((0.5 * (math.tanh(((1 - i - 1 / 1000) * BIG_ARG - 2.2)) + 1)) ** SMALL_ARG) - (
            (0.5 * (math.tanh(((1 - i) * BIG_ARG - 2.2)) + 1)) ** SMALL_ARG)) * 100


X = [i / 1000 for i in range(1000)]
Tanh_Y = [tanh_change(i) for i in X]
Tanh_Der_Y = [tanh_derivative(i) for i in X]

line = 0
for ind, i in enumerate(Tanh_Der_Y):
    if Tanh_Der_Y[ind - 1] > Tanh_Der_Y[ind] < Tanh_Der_Y[ind + 1]:
        line = ind / 1000
        print('最大斜率点：', line)

plt.title('Tanh Function')
plt.plot(X, Tanh_Y, color='green', label='tanh')
plt.plot(X, Tanh_Der_Y, color='blue', label='der')
plt.plot(X, [0 for i in X], color='black')
plt.plot([line for i in X], Tanh_Der_Y, color='red')
plt.plot([line for i in X], Tanh_Y, color='red')
plt.legend()  # 显示图例

plt.xlabel(line)
plt.ylabel('value')
plt.show()
