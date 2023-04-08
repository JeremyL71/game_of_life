import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import tkinter as tk

def create_initial_grid(N, cell_size=10):
    def on_click(event):
        x, y = event.x // cell_size, event.y // cell_size
        grid[y, x] = 1 - grid[y, x]
        canvas.itemconfig(cell_rects[y, x], fill=('white' if grid[y, x] == 0 else 'black'))

    def start_animation():
        root.destroy()

    root = tk.Tk()
    root.title("Initial Grid")

    canvas = tk.Canvas(root, width=N*cell_size, height=N*cell_size)
    canvas.pack()

    grid = np.zeros((N, N), dtype=int)
    cell_rects = np.empty((N, N), dtype=object)

    for i in range(N):
        for j in range(N):
            cell_rects[i, j] = canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill='white', outline='gray')

    canvas.bind("<Button-1>", on_click)

    start_button = tk.Button(root, text="Start", command=start_animation)
    start_button.pack()

    root.mainloop()

    return grid

def main():
    N = 50
    num_generations = 2

    grid = create_initial_grid(N)

    def count_neighbors(grid, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if grid[(x + i) % N, (y + j) % N] == 1:
                    count += 1
        return count

    def update(frame_number, grid, img):
        new_grid = grid.copy()
        stable = False
        for i in range(N):
            for j in range(N):
                neighbors = count_neighbors(grid, i, j)
                if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1
        if np.array_equal(grid, new_grid):
            stable = True
        img.set_data(new_grid)
        grid[:] = new_grid[:]
        print(grid)
        if np.sum(grid) == 0:
            print(f"jesus cry")
            sys.exit()
        if stable:
            print("La grille est stable.")
            sys.exit()

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(grid, img), frames=num_generations, interval=50, save_count=50)

    plt.show(block=True)
    plt.close()

if __name__ == "__main__":
    main()
