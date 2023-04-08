# Game of Life

This is a Python implementation of Conway's Game of Life, a cellular automaton that simulates the evolution of a population of cells. The program creates an initial grid and allows the user to interactively select which cells are alive or dead. The program then updates the grid according to the rules of the game, and displays the evolution of the grid using matplotlib animation.

## Installation

To run this program, you will need Python 3.x, as well as the following libraries:

    numpy
    matplotlib
    tkinter


These can be installed using pip (managed by pipenv):

    pipenv install
    pipenv run python -m game_of_life

## Usage

To run the program, simply execute the main() function in the game_of_life.py file. The program will create an initial grid, which you can interact with using the mouse. Click on a cell to toggle it between alive (black) and dead (white). Once you are satisfied with the initial configuration, click the "Start" button to begin the simulation.

The simulation will run for a fixed number of generations (specified by the num_generations variable in main()). The program will print the state of the grid at each generation, and will terminate when one of the following conditions is met:

The grid becomes empty
The grid stabilizes (i.e., the state of the grid is unchanged from one generation to the next)

## Customization

You can customize the size of the grid and the size of each cell by changing the N and cell_size variables in create_initial_grid(). You can also adjust the speed of the animation by changing the interval parameter in animation.FuncAnimation().