import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from city_coords import city_coords

coords = np.array([(x, y) for x, y, _ in city_coords])
name = [name for _, _, name in city_coords]

distances = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(axis=2))
np.fill_diagonal(distances, np.inf)

N_CITIES = len(coords)
N_ANTS = 20
ALPHA = 1
BETA = 2
RHO = 0.5
Q = 100
N_ITERATIONS = 300

awards = np.ones((N_CITIES, N_CITIES))
best_path = None
best_distance = np.inf
iteration_results = []

for iteration in range(N_ITERATIONS):
    paths = []
    path_distances = []

    for ant in range(N_ANTS):
        path = [np.random.randint(N_CITIES)]
        for _ in range(N_CITIES - 1):
            currrent_city =  path[-1]
            probabilities = (
                (awards[currrent_city] ** ALPHA) *
                ((1 / distances[currrent_city]) ** BETA)
            )
            probabilities[path] = 0
            probabilities /= probabilities.sum()
            next_city = np.random.choice(range(N_CITIES), p=probabilities)
            path.append(next_city)
        path.append(path[0])
        paths.append(path)
        path_distance = sum(distances[path[i], path[i + 1]] for i in range(len(path) - 1))
        path_distances.append(path_distance)
        if path_distance < best_distance:
            best_distance = path_distance
            best_path = path

    awards *= (1 - RHO)
    for path, path_distance in zip(paths, path_distances):
        for i in range(len(path) - 1):
            awards[path[i], path[i + 1]] += Q / path_distance

    iteration_results.append((best_path[:], best_distance))

fig, ax = plt.subplots(figsize=(6, 4))

def update(frame):
    ax.clear()
    path, distance = iteration_results[frame]
    for i in range(len(path) - 1):
        city_a = coords[path[i]]
        city_b = coords[path[i + 1]]
        ax.plot([city_a[0], city_b[0]], [city_a[1], city_b[1]], 'b-', alpha=0.6)
    ax.scatter(coords[:, 0], coords[:, 1], color='red', label='Cities')
    for idx, (x, y, name) in enumerate(city_coords):
        ax.text(x, y, name, fontsize=10, ha='right')
    ax.set_title(f"Iteration {frame + 1}, Distance: {distance:.2f}")
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")
    ax.grid()
    ax.legend()

ani = FuncAnimation(fig, update, frames=len(iteration_results), interval=100, repeat=False)
plt.show()