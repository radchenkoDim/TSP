import matplotlib.pyplot as plt
import itertools
import math

def plot_all_connections(cities):
    """
    Візуалізує всі можливі з'єднання між містами.
    
    Аргументи:
        cities: список координат міст та їх назви:
            [(x1, y1, 'місто 1'), (x2, y2, 'місто 2'), ...].
    """
    # Створюємо графік
    plt.figure(figsize=(8, 8))
    
    # Розділяємо координати X та Y
    x = [city[0] for city in cities]
    y = [city[1] for city in cities]
    
    # Додаємо червоні точки для кожного міста
    plt.scatter(x, y, color='red', zorder=5)

    # З'єднуємо всі пари міст
    line = 0
    for (i, j) in itertools.combinations(range(len(cities)), 2):
        xi, yi, _ = cities[i]
        xj, yj, _ = cities[j]
        plt.plot([xi, xj], [yi, yj], alpha=0.5)  # лінія з прозорістю
        line += 1
    
    # Додавання підписів до міст
    for i, (xi, yi, name) in enumerate(cities):
        plt.text(xi, yi, f"{name} ({i})", fontsize=8, ha='right')

    # Заголовок та підписи осей
    plt.title(f"З'єднання всіх міст ({line})")
    plt.xlabel("X-координата")
    plt.ylabel("Y-координата")
    plt.grid(True)
    print(f"Кількість з'єднань: {line}")

    # Показуємо графік
    plt.show()

city_coords = [
    (0, 0, 'Київ'),
    (55, 125, 'Чернігів'),
    (310, 60, 'Суми'),
    (410, -45, 'Харків'),
    (110, -110, 'Черкаси'),
    (295, -85, 'Полтава'),
    (120, -215, 'Кропивницький'),
    (205, -280, 'Кривий Ріг'),
    (330, -220, 'Дніпро'),
    (340, -290, 'Запоріжжя'),
    (535, -270, 'Донецьк'),
    (645, -210, 'Луганськ'),
    (205, -390, 'Миколаїв'),
    (150, -420, 'Херсон'),
    (10, -440, 'Одеса'),
    (215, -635, 'Севастопіль'),
    (-140, -15, 'Житомир'),
    (-155, -140, 'Вінниця'),
    (-265, -110, 'Хмельницький'),
    (-340, -240, 'Чернівці'),
    (-365, -100, 'Тернопіль'),
    (-430, -170, 'Івано-Франківськ'),
    (-480, -60, 'Львів'),
    (-605, -200, 'Ужгород'),
    (-320, 20, 'Рівне'),
    (-385, 40, 'Луцьк')
]

def combination_num(city_coords):
    n = len(city_coords)
    result = math.factorial(n - 1) # Обчислюємо (n - 1)!
    result_str = "{:,}".format(result)
    formatted_result = result_str.replace(',', ' ')
    return formatted_result


print(f"Кількість міст: {len(city_coords)}")
print(f"Кільтість комбінацій: {combination_num(city_coords)}")
plot_all_connections(city_coords)