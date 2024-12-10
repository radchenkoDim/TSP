import matplotlib.pyplot as plt
import math

def graphic(): 
    # Створюємо список кількості міст
    num_cities = list(range(2, 10))  # Для прикладу візьмемо від 2 до 10 міст

    # Обчислюємо кількість можливих комбінацій для кожної кількості міст
    combinations = [math.factorial(n - 1) for n in num_cities]

    # Створюємо графік
    plt.figure(figsize=(10, 6))
    plt.plot(num_cities, combinations, marker='o', color='b', linestyle='-', label="Кількість комбінацій")

    # Налаштовуємо графік
    plt.title("Зростання кількості можливих комбінацій для різної кількості міст")
    plt.xlabel("Кількість міст")
    plt.ylabel("Кількість комбінацій (факторіал (n-1)!)")
    plt.grid(True)
    plt.legend()

    # Форматуємо числа на осі Y, щоб вони відображалися без скорочень
    plt.ticklabel_format(style='plain', axis='y')  # Вимикає наукову нотацію

    # Показуємо графік
    plt.show()
