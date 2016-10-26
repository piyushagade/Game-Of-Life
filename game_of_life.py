'''
Author: Piyush Agade

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

         Conway's Game of Life

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
import os
import random as r
from sys import stdout

from matplotlib import pyplot as plt
from numpy import array

# ***********************************************************************
# Changeable system variables
width = 15
height = 15
culture = array([[0 for i in range(width)] for j in range(height)])

life_of_culture = 10
age_of_culture = 0

no_of_seeds = 168

# **********************************************************************
seeds = []
for _ in range(no_of_seeds):
    seeds.append((r.randint(0, height - 1), r.randint(0, width - 1)))

population = 0

def simulate():
    next_gen = culture
    for _ in range(width):
        for __ in range(height):
            if _ == 0 or __ == 0:
                if _ == 0:
                    u = 0
                if __ == 0:
                    l = 0
            else:
                u = next_gen[_ - 1, __]
                l = next_gen[_, __ - 1]
            try:
                r = next_gen[_, __+ 1]
            except IndexError:
                r = 0
            try:
                d = next_gen[_ + 1, __]
            except IndexError:
                d = 0

            immediate_neighbours = [u, l, r, d]
            no_of_alive_neighbours = sum(immediate_neighbours)
            # print _,__,next_gen[_,__], immediate_neighbours


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


def print_culture(culture):
    plt.figure(age_of_culture)
    plt.imshow(culture, interpolation = 'nearest')
    plt.title('Generation: ' + str(age_of_culture) + '/' + str(life_of_culture) + '\nPopulation: ' + str(sum(sum(culture))))
    plt.savefig('png/'+ str(age_of_culture))
    # plt.show()
    writeGIF()

def writeGIF():
    file_names = sorted((fn for fn in os.listdir('png') if fn.endswith('.png')), key=lambda s: (s[5:]))
    import imageio
    readImages = []
    for file_names in file_names:
        readImages.append(imageio.imread('./png/' + file_names))
        stdout.write("\r%d" % age_of_culture + '/' + str(life_of_culture) + ' generations recorded.')

    imageio.mimsave('./gif/animation.gif', readImages, fps = 1)

if __name__ == '__main__':
    culture = plant_seeds(seeds, culture)
    print_culture(culture)

    while age_of_culture != life_of_culture:
        culture = simulate()
        age_of_culture += 1
        print_culture(culture)

    stdout.write("\nGIF generated in ./gif.")
