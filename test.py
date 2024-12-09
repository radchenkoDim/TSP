import itertools
import matplotlib.pyplot as plt
import numpy as np

def traveling_salesman_greedy(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    route = [0]  # Починаємо з міста 0
    visited[0] = True
    total_distance = 0

    current_city = 0
    for _ in range(num_cities - 1):
        next_city = min(
            (i for i in range(num_cities) if not visited[i]),
            key=lambda x: distance_matrix[current_city][x]
        )
        total_distance += distance_matrix[current_city][next_city]
        route.append(next_city)
        visited[next_city] = True
        current_city = next_city

    # Повертаємося в початкове місто
    total_distance += distance_matrix[current_city][0]
    route.append(0)

    return route, total_distance

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
    
    for i in route:
        xi, yi, name = cities[i]
        

    plt.title("Оптимальний маршрут комівояджера")
    plt.xlabel("X-координата")
    plt.ylabel("Y-координата")
    plt.legend()
    plt.grid()
    plt.show()

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

distance_matrix = calculate_distance_matrix(city_coords)
route = traveling_salesman_greedy(distance_matrix)
print(route[0])

plot_route(city_coords, route[0])