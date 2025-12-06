import random
from tsp.anytime_solver import anytime_tsp

def generate_random_points(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def main():
    points = generate_random_points(50, seed=42)
    solver = anytime_tsp(points)

    print("Running Anytime TSP Solver...")
    print("Press Ctrl+C to exit.\n")

    try:
        for tour, length in solver:
            print(f"Tour length: {length:.4f}")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()