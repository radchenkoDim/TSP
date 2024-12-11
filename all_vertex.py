import matplotlib.pyplot as plt
import itertools
import math

from city_coords import city_coords

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

    plt.title(f"З'єднання всіх міст ({line})")
    plt.xlabel("X-координата")
    plt.ylabel("Y-координата")
    plt.grid(True)
    print(f"Кількість з'єднань: {line}")

    plt.show()

def combination_num(city_coords):
    n = len(city_coords)
    result = math.factorial(n - 1)
    result_str = "{:,}".format(result)
    result_str_replace = result_str.replace(',', ' ')
    return result_str_replace

print(f"Кількість міст: {len(city_coords)}")
print(f"Кільтість комбінацій: {combination_num(city_coords)}")
plot_all_connections(city_coords)