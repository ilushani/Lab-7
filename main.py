import random
import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation
from matplotlib.ticker import FormatStrFormatter
import csv


def animate_func(num):
    ax_anm.clear()
    ax_anm.plot(dataSet[0, :num + 1], dataSet[1, :num + 1], c='blue')
    ax_anm.scatter(dataSet[0, num], dataSet[1, num], c='blue', marker='o')
    ax_anm.plot(dataSet[0, 0], dataSet[1, 0], c='black', marker='o')
    ax_anm.set_xlim([0, np.pi*5])
    ax_anm.set_ylim([-1, 1])


print("Задание 1")

default_list_a = [random.randint(1, 99) for i in range(10 ^ 6)]
default_list_b = [random.randint(1, 99) for i in range(10 ^ 6)]

t1_start = time.perf_counter()
for i in range(len(default_list_a)):
    default_list_a[i] *= default_list_b[i]
all_time1 = time.perf_counter() - t1_start

numpy_list_a = np.random.randint(1, 100, 10 ^ 6)
numpy_list_b = np.random.randint(1, 100, 10 ^ 6)

t2_start = time.perf_counter()
numpy_list_a = np.multiply(numpy_list_a, numpy_list_b)
all_time2 = time.perf_counter() - t2_start

print("Время, затраченное на умножение стандартных списков: %s" % (all_time1))
print("Время, затраченное на умножение массивов NumPy: %s" % (all_time2))

print("Задание 2")
data_raw = []
data_normalized = []
column_number = 4
with open("data2.csv", 'r') as csvfile:
    csvfile.readline()
    lines = csv.reader(csvfile, delimiter=';')
    for line in lines:
        if line[column_number] != '':
            data_normalized.append(float(line[column_number]))
            data_raw.append(float(line[column_number]))
        else:
            data_raw.append(0)
bins = 20

fig1, ax1 = plt.subplots()
ax1.set_xlabel('значения')
ax1.set_ylabel('частотность')
ax1.set_title('Гистограмма')
ax1.hist(data_raw, bins, density=True, color='blue', edgecolor='black')

fig2, ax2 = plt.subplots()
ax2.set_xlabel('значения')
ax2.set_ylabel('частотность')
ax2.set_title('Нормализованная гистограмма')
ax2.hist(data_normalized, bins, density=True, color='blue', edgecolor='black')
plt.show()

deviation = np.std(data_normalized)
print('Среднеквадратичное отклонение нормализированных ванных: %.3f' % (deviation))

x = np.linspace(-np.pi * 3, np.pi * 3, 100)
y = x * np.cos(x)
z = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()

t = np.linspace(0, 20, 100)
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

dataSet = np.array([x, y])
numDataPoints = len(t)

fig = plt.figure()
ax_anm = plt.axes()
line_anm = animation.FuncAnimation(fig, animate_func, interval=100,
                                   frames=numDataPoints)
plt.show()
writergif = animation.PillowWriter(fps=numDataPoints / 6)
line_anm.save("animation.gif", writer=writergif)