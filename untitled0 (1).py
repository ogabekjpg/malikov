# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sP3VZexkARf5Oo8kp6Sx_heZ3J5U4cOg
"""



import numpy as np

# 1. Massiv yaratish
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Matematik operatsiyalar
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

print("1D Massiv: ", array_1d)
print("2D Massiv:\n", array_2d)
print("Massivlar yig'indisi: ", sum_array)
print("O'rtacha: ", mean_array)
print("Ko'paytma: ", product_array)