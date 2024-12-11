import itertools
import matplotlib.pyplot as plt
import numpy as np
import module

def traveling_salesman_brute_forse(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    best_route = None
    best_distance = float('inf')

    i = 0
    for perm in itertools.permutations(cities[1:]):
        print(f"{i + 1}. {perm}")
        route = [0] + list(perm) + [0]
        distance = sum(
            distance_matrix[route[i]][route[i + 1]] for i in range(num_cities)
        )
        if distance < best_distance:
            best_distance = distance
            best_route = route
        i += 1

    return best_route, round(best_distance, 2)

def plot_route(cities, route):
    """
    Візуалізує маршрут комівояжера.

    Аргументи:
        cities: список координат міст та їх назви:
            [(x1, y1, 'місто 1'), (x2, y2, 'місто 2'), ...].
        route: список міст у порядку відвідування.
    """
    x = [cities[i][0] for i in route]
    y = [cities[i][1] for i in route]

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, '-o', label="Маршрут")
    # plt.scatter(x, y, c='red', label="Міста")
    
    for i, (xi, yi, name) in enumerate(cities):
        plt.text(xi, yi, f"{i}. {name}", fontsize=12, ha='right')

    plt.title("Оптимальний маршрут комівояджера")
    plt.xlabel("X-координата")
    plt.ylabel("Y-координата")
    plt.legend()
    plt.grid()
    plt.show()

city_coords = [
    (0, 0, 'Львів'),
    (3.1, 4.5, 'Луцьк'),
    (5.2, 4, 'Рівне'),
    (7.1, -1.5, 'Хмельницький'),
    (4.5, -5.7, 'Чернівці'),
    (3.8, -1, 'Тернопіль'),
    (1.5, -3.4, 'Франківськ'),
    (-4.2, -4.5, 'Ужгород')
]

"""
Кількість можливих маршрутів C = (n - 1)!
    Де n - це кількість міст.

Задача для заходу України (8 міст) має:
    5040 можливих маршрутів.

Така ж задача для 26 має:
    15 511 210 043 330 985 984 000 000 можливих маршрутів.
"""

distance_matrix = module.calculate_distance_matrix(city_coords)
best_route, best_distance = traveling_salesman_brute_forse(distance_matrix)
print(f"Найкращий маршрут: {best_route}")
print(f"Загальна відстань: {best_distance}")

plot_route(city_coords, best_distance)