import matplotlib.pyplot as plt
import seaborn as sns

size = 3

dx = 0.05
dy = 0.05
dt = 0.001

nx = int(size // dx)  # размер по ох
ny = int(size // dy)  # размер по oy
nt = int(size // dt)  # кол-во циклов

value = [[0 for i in range(nx + 1)] for j in range(ny + 1)]  # заполянем массив 0

# граничные условия
for j in range(ny + 1):
    value[0][j] = 100
    value[nx][j] = 100

# создаем такой же массив
value_null = [[value[i][j] for i in range(nx + 1)] for j in range(ny + 1)]

# схема
for t in range(nt + 1):
    for i in range(1, nx):
        for j in range(1, ny):
            if ((i >= nx // 3) & (i <= 2 * nx // 3) & (j >= ny // 3) & (j <= 2 * ny //3)):  # ЫЫЫ
                value[i][j] = 0
                value_null[i][j] = 0
            else:
                value[i][j] = (((value_null[i + 1][j] - 2 * value_null[i][j] + value_null[i - 1][j]) / dx ** 2) + ((value_null[i][j + 1] - 2 * value_null[i][j] + value_null[i][j - 1]) / dy ** 2)) * dt + value_null[i][j]
                value_null[i][j] = (((value_null[i + 1][j] - 2 * value_null[i][j] + value_null[i - 1][j]) / dx ** 2) + ((value_null[i][j + 1] - 2 * value_null[i][j] + value_null[i][j - 1]) / dy ** 2)) * dt + value_null[i][j]

sns.heatmap(value)
plt.show()