from tsp.tour import create_random_tour
from tsp.geometry import tour_length
from tsp.two_opt import try_two_opt

def anytime_tsp(points):
    tour = create_random_tour(len(points))
    length = tour_length(tour, points)

    best_tour = tour[:]
    best_length = length
    yield best_tour, best_length

    while True:
        result = try_two_opt(tour, points)

        if result is None:
            tour = create_random_tour(len(points))
            length = tour_length(tour, points)
            yield tour,length
        else:
            tour, length = result
            yield tour, length

        if length < best_length:
            best_tour = tour[:]
            best_length = length