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
import imageio

# ***********************************************************************
#                       Changeable system variables
# ***********************************************************************

# Culture dimensions
width = 50
height = 50

# Culture behavioral parmaters
life_of_culture = 20
age_of_culture = 0

no_of_seeds = 8868

# GIF parameters
fps = 1     # Higher the fs, faster the gif animation will be.

# First generation

# 1. Glider
seeds = [(2,1),(3,2),(3,3),(2,3),(1,3)]

# 2. Mini Bomb
seeds = [(1,2),(2,1),(2,2),(2,3),(3,1),(3,3),(4,2)]

x = 5
y = 0
copies = 1



# **********************************************************************
#                       Nothing to be changed below
# **********************************************************************
temp_x = x
temp_y = y
for _ in range(copies):
    seeds += ((2+y,1+x),(3+y,2+x),(3+y,3+x),(2+y,3+x),(1+y,3+x))
    x += temp_x
    y += temp_y

culture = array([[0 for i in range(width)] for j in range(height)])
#
# for _ in range(no_of_seeds):
#     seeds.append((r.randint(0, height - 1), r.randint(0, width - 1)))

population = 0


def simulate():
    next_gen = array([[0 for i in range(width)] for j in range(height)])
    for _ in range(width):
        for __ in range(height):

            if _ == 0 or __ == 0:
                if _ == 0:
                    u = 0
                if __ == 0:
                    l = 0
            else:
                u = culture[_ - 1, __]
                l = culture[_, __ - 1]
            try:
                r = culture[_, __ + 1]
            except IndexError:
                r = 0
            try:
                d = culture[_ + 1, __]
            except IndexError:
                d = 0
            try:
                ur = culture[_ - 1, __ + 1]
            except IndexError:
                ur = 0
            try:
                dr = culture[_ + 1, __ + 1]
            except IndexError:
                dr = 0
            try:
                dl = culture[_ + 1, __ - 1]
            except IndexError:
                dl = 0
            try:
                ul = culture[_ - 1, __ - 1]
            except IndexError:
                ul = 0

            immediate_neighbours = [u, l, r, d]
            neighbours = [ul, u, ur, l, r, dl, d, dr]
            no_of_alive_neighbours = sum(neighbours)



            '''
            Any live cell with fewer than two live neighbours dies, as if caused by under-population.
            Any live cell with two or three live neighbours lives on to the next generation.
            Any live cell with more than three live neighbours dies, as if by over-population.
            Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            '''

            if no_of_alive_neighbours < 2 and culture[_,__] == 1:
                next_gen[_, __] = 0
            elif no_of_alive_neighbours in (2,3) and culture[_,__] == 1:
                next_gen[_, __] = 1
            elif no_of_alive_neighbours > 3 and culture[_,__] == 1:
                next_gen[_, __] = 0
            elif (no_of_alive_neighbours == 3) and culture[_,__] == 0:
                next_gen[_, __] = 1


            # Condensed if-else
            # if culture[_,__] == 1:
            #     if no_of_alive_neighbours not in (2,3):
            #         next_gen[_,__] = 0
            #     else:
            #         next_gen[_,__] = 1
            # else:
            #     if no_of_alive_neighbours == 3:
            #         next_gen[_,__] = 1


    return next_gen


def plant_seeds(seeds, culture):
    for seed in seeds:
        try:
            culture[seed[0], seed[1]] = 1
        except IndexError:
            pass
    return culture


def print_culture(culture):
    plt.figure(age_of_culture)
    plt.imshow(culture, interpolation = 'nearest')
    plt.title(
        'Generation: ' + str(age_of_culture) + '/' + str(life_of_culture) + '\nPopulation: ' + str(sum(sum(culture))))
    plt.savefig('png/' + str(age_of_culture))
    # plt.show()
    writeGIF()


def writeGIF():
    file_names = sorted((fn for fn in os.listdir('png') if fn.endswith('.png')), key = lambda s: (s[5:]))
    readImages = []
    for file_names in file_names:
        readImages.append(imageio.imread('./png/' + file_names))
        stdout.write("\r%d" % age_of_culture + '/' + str(life_of_culture) + ' generations recorded.')

    imageio.mimsave('./gif/animation.gif', readImages, fps = fps)


if __name__ == '__main__':
    #simulate the alphas
    culture = plant_seeds(seeds, culture)
    print_culture(culture)

    # simulate the descendants
    while age_of_culture != life_of_culture:

        culture = simulate()
        age_of_culture += 1
        print_culture(culture)




    # announce completion of the program
    stdout.write("\nGIF generated in ./gif.")
