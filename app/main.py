import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    # Définition de la taille de la grille et du nombre de générations à simuler
    N = 50
    num_generations = 2

    # Matrice de cellules de départ
    start_matrix = np.array([[0, 0, 0, 0, 0],
                            [0, 1, 1, 0, 0],
                            [0, 0, 0, 1, 1],
                            [1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0]])

    # Initialisation de la grille avec les cellules de départ
    grid = np.zeros((N, N))
    start_row = (N // 2) - (start_matrix.shape[0] // 2)
    start_col = (N // 2) - (start_matrix.shape[1] // 2)
    grid[start_row:start_row+start_matrix.shape[0], start_col:start_col+start_matrix.shape[1]] = start_matrix

    # Fonction pour calculer le nombre de voisins d'une cellule
    def count_neighbors(grid, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if grid[(x + i) % N, (y + j) % N] == 1:
                    count += 1
        return count

    # Fonction pour mettre à jour la grille selon les règles du jeu de la vie
    def update(frame_number, grid, img):
        new_grid = grid.copy()
        for i in range(N):
            for j in range(N):
                neighbors = count_neighbors(grid, i, j)
                if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1
        img.set_data(new_grid)
        grid[:] = new_grid[:]
        if np.sum(grid) == 0:  # Si toutes les cellules sont mortes
            return []  # Arrêter l'animation
        return img,

    # Initialisation de l'animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(grid, img), frames=num_generations, interval=50, save_count=50)

    # Affichage de l'animation
    plt.show(block=True)
    plt.close() # Fermer la fenêtre de matplotlib après la fin de l'animation

if __name__ == "__main__":
    main()
