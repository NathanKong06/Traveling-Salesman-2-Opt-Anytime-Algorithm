import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tsp.anytime_solver import anytime_tsp


def generate_random_points(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def main():
    num_cities = 100
    points = generate_random_points(num_cities, seed=random.seed())
    solver = anytime_tsp(points)

    print("Running Anytime TSP with live visualization...")
    print("Close the plot window or press Ctrl+C to exit.\n")

    fig, ax = plt.subplots()
    tour_plot, = ax.plot([], [], marker="o", linestyle="-", color="red")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    best_length = float("inf")
    best_tour = None

    def update(_frame):
        nonlocal best_length, best_tour
        try:
            tour, length = next(solver)
        except StopIteration:
            return

        if length < best_length:
            best_length = length
            best_tour = tour[:]

            plt.figure(fig.number) 
            plt.title(f"Best tour length: {best_length:.4f}")
            plt.savefig("best_tour.png")

        x = [points[i][0] for i in tour] + [points[tour[0]][0]]
        y = [points[i][1] for i in tour] + [points[tour[0]][1]]
        tour_plot.set_data(x, y)
        ax.set_title(f"Current: {length:.4f} | Best so far: {best_length:.4f} | Num Cities: {num_cities}")

        # print(f"Current length: {length:.4f} | Best length so far: {best_length:.4f}")

        return tour_plot,

    anim = FuncAnimation(fig, update, interval=300)

    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nVisualization stopped.")
        print("=" * 40)
        print("Best tour summary:")
        print(f"Best tour length : {best_length:.4f}")
        print(f"Best tour order  : {best_tour}")
        print("City coordinates :")
        for i, (x, y) in enumerate(points):
            print(f"  City {i}: ({x:.4f}, {y:.4f})")
        print(f"\nBest tour plot saved as 'best_tour.png'")
        print("=" * 40)

    print("\nDone.")


if __name__ == "__main__":
    main()