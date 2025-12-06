import random 

def create_random_tour(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

def two_opt_swap(tour, i, j):
    if i > j:
        i, j = j, i
    
    prefix = tour[:i]
    segment_to_reverse = tour[i:j+1]
    reversed_segment = segment_to_reverse[::-1]
    suffix = tour[j+1:]
    return prefix + reversed_segment + suffix

def is_valid_tour(tour):
    return sorted(tour) == list(range(len(tour)))