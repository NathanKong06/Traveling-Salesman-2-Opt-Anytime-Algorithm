import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tsp.anytime_solver import anytime_tsp


def generate_random_points(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def main():
    points = generate_random_points(100, seed=42)
    solver = anytime_tsp(points)

    print("Running Anytime TSP with live visualization...")
    print("Close the plot window or press Ctrl+C to exit.\n")

    fig, ax = plt.subplots()
    tour_plot, = ax.plot([], [], marker="o", linestyle="-")
    ax.set_title("Anytime 2-opt TSP")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def update(_frame):
        try:
            tour, length = next(solver)
        except StopIteration:
            return

        x = [points[i][0] for i in tour] + [points[tour[0]][0]]
        y = [points[i][1] for i in tour] + [points[tour[0]][1]]
        tour_plot.set_data(x, y)

        ax.set_title(f"TSP Length: {length:.4f}")

        print(f"Tour length: {length:.4f}")

        return tour_plot,

    anim = FuncAnimation(fig, update, interval=300)

    try:
        plt.show()
    except KeyboardInterrupt:
        print("Visualization stopped.")

    print("\nDone.")


if __name__ == "__main__":
    main()