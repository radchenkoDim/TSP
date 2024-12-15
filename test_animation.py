import itertools
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from city_coords import ukr_west


def traveling_salesman_brute_forse_animated(distance_matrix, cities):
    """
    Виконує пошук найкращого маршруту комівояжера та відображає процес підбору.

    Аргументи:
        distance_matrix: матриця відстаней між містами.
        cities: список координат міст [(x1, y1, 'місто 1'), ...].

    Повертає:
        Найкращий маршрут і загальну відстань.
    """
    num_cities = len(distance_matrix)
    cities_indices = list(range(num_cities))
    best_route = None
    best_distance = float('inf')
    all_routes = []

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title("Оптимальний маршрут комівояжера (анімація)")
    ax.set_xlabel("X-координата")
    ax.set_ylabel("Y-координата")
    ax.grid()
    
    x_coords = [city[0] for city in cities]
    y_coords = [city[1] for city in cities]
    ax.scatter(x_coords, y_coords, c='blue', label='Міста', zorder=5)

    for i, (x, y, name) in enumerate(cities):
        ax.text(x, y, f"{i}. {name}", fontsize=10, ha='right')

    # Лінії для поточного та найкращого маршруту
    current_line, = ax.plot([], [], 'r-', label='Поточний маршрут', alpha=0.7)
    best_line, = ax.plot([], [], 'b-', label='Найкращий маршрут', linewidth=2)

    def update(frame):
        nonlocal best_route, best_distance
        perm = all_routes[frame]
        route = [0] + list(perm) + [0]
        distance = sum(
            distance_matrix[route[i]][route[i + 1]] for i in range(num_cities)
        )
        
        # Оновлення найкращого маршруту
        if distance < best_distance:
            best_distance = distance
            best_route = route

        # Оновлення червоної лінії (поточний маршрут)
        current_x = [x_coords[city] for city in route]
        current_y = [y_coords[city] for city in route]
        current_line.set_data(current_x, current_y)

        # Оновлення синьої лінії (найкращий маршрут)
        if best_route:
            best_x = [x_coords[city] for city in best_route]
            best_y = [y_coords[city] for city in best_route]
            best_line.set_data(best_x, best_y)

        return current_line, best_line

    # Генеруємо всі перестановки маршрутів
    all_routes = list(itertools.permutations(cities_indices[1:]))

    anim = FuncAnimation(fig, update, frames=len(all_routes), interval=10, blit=True)

    ax.legend()
    plt.show()

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
                distance_matrix[i][j] = np.sqrt(
                    (city_coords[i][0] - city_coords[j][0]) ** 2 +
                    (city_coords[i][1] - city_coords[j][1]) ** 2
                )
    return distance_matrix


# Тестовий виклик
distance_matrix = calculate_distance_matrix([(x, y) for x, y, _ in ukr_west])
best_route, best_distance = traveling_salesman_brute_forse_animated(distance_matrix, ukr_west)
print(f"Найкращий маршрут: {best_route}")
print(f"Загальна відстань: {best_distance}")
