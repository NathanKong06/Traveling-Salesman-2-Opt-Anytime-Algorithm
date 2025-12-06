from tsp.geometry import tour_length
from tsp.tour import two_opt_swap

def try_two_opt(tour, points):
    best_len = tour_length(tour, points)
    best_tour = tour

    for i in range(len(tour) - 1):
        for j in range(i + 1, len(tour)):
            candidate = two_opt_swap(tour, i, j)
            candidate_len = tour_length(candidate, points)
            if candidate_len < best_len:
                best_len = candidate_len
                best_tour = candidate

    if best_tour is not tour:
        return best_tour, best_len
    return None