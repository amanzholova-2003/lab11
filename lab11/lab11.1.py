import random
import matplotlib.pyplot as plt

# Создание списка случайных чисел
random_numbers = [random.randint(1, 100) for _ in range(10)]

   # Вывод списка случайных чисел в консоль
print("Список случайных чисел:", random_numbers)

   # Создание диаграммы, отображающей распределение случайных чисел
plt.hist(random_numbers, bins=10)
plt.title("Распределение случайных чисел")
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.show()