def print_hi(name):

    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
from math import *

alpha = float(input("введите угол альфа: "))

chislitel_z1 = 1 - 2 * (sin(alpha)**2)

znamenatel_z1 = 1 + sin(2 * alpha)
z1 = chislitel_z1 / znamenatel_z1

chislitel_z2 = 1 - tan(alpha)
znamenatel_z2 = 1 + tan(alpha)
z2 = chislitel_z2 / znamenatel_z2

print(f"Результат z1 = {z1:.4f}")
print(f"Результат z2 = {z2:.4f}")