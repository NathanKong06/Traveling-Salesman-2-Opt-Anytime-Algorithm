from tsp.tour import create_random_tour
from tsp.geometry import tour_length
from tsp.two_opt import try_two_opt
import time

def anytime_tsp(points):
    tour = create_random_tour(len(points))
    length = tour_length(tour, points)
    yield tour, length

    while True:
        result = try_two_opt(tour, points)

        if result is None:
            yield tour, length
            time.sleep(0.1)
            continue

        tour, length = result
        yield tour, length