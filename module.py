import itertools
import numpy as np
import math

# Функції для розв'язання задачі комівояжера
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

def combination_num(city_coords):
    n = len(city_coords)
    result = math.factorial(n - 1) # Обчислюємо (n - 1)!
    result_str = "{:,}".format(result)
    formatted_result = result_str.replace(',', ' ')
    return formatted_result
