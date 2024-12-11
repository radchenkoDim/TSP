import itertools
import matplotlib.pyplot as plt
import numpy as np

from city_coords import ukr_west

def traveling_salesman_brute_forse(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    best_route = None
    best_distance = float('inf')

    for perm in itertools.permutations(cities[1:]):
        route = [0] + list(perm) + [0]
        distance = sum(
            distance_matrix[route[i]][route[i + 1]] for i in range(num_cities)
        )
        if distance < best_distance:
            best_distance = distance
            best_route = route

    return best_route, round(best_distance, 2)

def calculate_distance_matrix(city_coords):
    """
    Обчислює матрицю відстаней між містами за їх координатами.
    
    Аргументи:
        city_coords: список координат міст [(x1, y1), (x2, y2), ...].
        
    Повертає:
        Матриця відстаней.
    """
    num_cities = len(city_coords)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                # Обчислюємо евклідову відстань
                # d = sqrt{(x1 - x2)^2 + (y1 - y2)^2}
                distance_matrix[i][j] = np.sqrt(
                    (city_coords[i][0] - city_coords[j][0]) ** 2 +
                    (city_coords[i][1] - city_coords[j][1]) ** 2
                )
    return distance_matrix

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

"""
Кількість можливих маршрутів C = (n - 1)!
    Де n - це кількість міст.

Задача для заходу України (8 міст) має:
    5040 можливих маршрутів.

Така ж задача для всіх обласних центрів (25 міст) має:
    620 448 401 733 239 439 360 000 можливих маршрутів.
"""

distance_matrix = calculate_distance_matrix(ukr_west)
best_route, best_distance = traveling_salesman_brute_forse(distance_matrix)
print(f"Найкращий маршрут: {best_route}")
print(f"Загальна відстань: {best_distance}")

plot_route(ukr_west, best_route)