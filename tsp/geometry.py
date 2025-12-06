import math 

def distance(p1, p2):
    return math.dist(p1, p2)

def tour_length(tour, points):
    if len(tour) == 0:
        return 0.0
    length = 0.0
    for i in range(len(tour)):
        length += distance(points[tour[i]], points[tour[(i + 1) % len(tour)]])
    return length