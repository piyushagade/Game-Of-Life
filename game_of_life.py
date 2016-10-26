'''
Author: Piyush Agade

+++++++++++++++++++++++++++++++++++++++++++

         Conway's Game of Life

+++++++++++++++++++++++++++++++++++++++++++
'''

from numpy import array
from matplotlib import pyplot as plt
import random as r

# System variables
width = 5
height = 5
culture = array([[0 for i in range(width)] for j in range(height)])

life_of_culture = 10
age_of_culture = 0

no_of_seeds = 16

seeds = []
for _ in range(no_of_seeds):
    seeds.append((r.randint(0, height - 1), r.randint(0, width - 1)))


def simulate():
    next_gen = culture
    for _ in range(width):
        for __ in range(height):
            try:
                neighbours = [culture[_ - 1, __ - 1], culture[_ - 0, __ - 1], culture[_ + 1, __ - 1],
                              culture[_ - 1, __ - 0], culture[_ + 1, __ - 0], culture[_ - 1, __ + 1],
                              culture[_ + 1, __ - 0], culture[_ + 1, __ + 1]]
                immediate_neighbours = [culture[_ - 1, __], culture[_, __ - 1],
                                        culture[_, __ + 1], culture[_ + 1, __]]
                no_of_alive_neighbours = sum(immediate_neighbours)
            except IndexError as ie:
                pass

            '''
            Any live cell with fewer than two live neighbours dies, as if caused by under-population.
            Any live cell with two or three live neighbours lives on to the next generation.
            Any live cell with more than three live neighbours dies, as if by over-population.
            Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            '''

            if no_of_alive_neighbours < 2:
                next_gen[_, __] = 0
            elif no_of_alive_neighbours > 3:
                next_gen[_, __] = 0
            elif (no_of_alive_neighbours == 3):
                next_gen[_, __] = 1
    return next_gen


def plant_seeds(seeds, culture):
    for seed in seeds:
        culture[seed[0], seed[1]] = 1
    return culture

def members():
    next_gen = culture
    for _ in range(width):
        for __ in range(height):
             try:
                 u = culture[_ - 1, __]
             except IndexError as ie:
                 u = 0
             try:
                 l = culture[_, __ - 1]
             except IndexError as ie:
                 l = 0
             try:
                 r = culture[_, __+ 1]
             except IndexError as ie:
                 r = 0
             try:
                 d = culture[_ + 1, __]
             except IndexError as ie:
                 d = 0

             immediate_neighbours = [u, l, r, d]
             no_of_alive_neighbours = sum(immediate_neighbours)
             print _,__,culture[_,__], immediate_neighbours


def print_culture(culture):
    plt.figure(age_of_culture)
    plt.imshow(culture, interpolation = 'nearest')
    plt.show()
    # print culture


if __name__ == '__main__':
    culture = plant_seeds(seeds, culture)
    members()
    print_culture(culture)

    while age_of_culture != life_of_culture:
        culture = simulate()
        age_of_culture += 1
        print_culture(culture)
