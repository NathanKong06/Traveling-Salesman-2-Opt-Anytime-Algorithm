import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tsp.anytime_solver import anytime_tsp


def generate_random_points(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def main():
    num_cities = 150
    points = generate_random_points(num_cities, seed=random.seed())
    solver = anytime_tsp(points)
    fast_mode = input("Enable fast mode? (y/n): ").strip().lower() == 'y'

    fig, ax = plt.subplots()
    tour_plot, = ax.plot([], [], marker="o", linestyle="-", color="red")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    best_length = float("inf")
    best_tour = None
    
    if not fast_mode:
        print("Running Anytime TSP with live visualization...")
        print("Close the plot window or press Ctrl+C to exit.\n")

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

            print(f"Current length: {length:.4f} | Best length so far: {best_length:.4f} | Num Cities: {num_cities}")

            return tour_plot,

        anim = FuncAnimation(fig, update, interval=300, cache_frame_data=False)

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

    else:
        print("Running Anytime TSP in fast mode (no visualization)...\n")
        try:
            for tour, length in solver:
                if length < best_length:
                    best_length = length
                    best_tour = tour[:]
                    print(f"New best length: {best_length:.4f}")
            
                    x = [points[i][0] for i in best_tour] + [points[best_tour[0]][0]]
                    y = [points[i][1] for i in best_tour] + [points[best_tour[0]][1]]
                    tour_plot.set_data(x, y)
                    fig.canvas.draw()

                    plt.figure(fig.number) 
                    plt.title(f"Best tour length: {best_length:.4f}")
                    plt.savefig("best_tour.png")

        except KeyboardInterrupt:
            print("\nComputations stopped.")
            print("=" * 40)
            print("Best tour summary:")
            print(f"Best tour length : {best_length:.4f}")
            print(f"Best tour order  : {best_tour}")
            print("City coordinates :")
            for i, (x, y) in enumerate(points):
                print(f"  City {i}: ({x:.4f}, {y:.4f})")
            print(f"\nBest tour plot saved as 'best_tour.png'")
            print("=" * 40)
            plt.show()

if __name__ == "__main__":
    main()