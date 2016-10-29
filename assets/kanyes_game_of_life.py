'''
Author: Piyush Agade

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                        Kanye's Game of Life

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
import os
import random as r
from sys import stdout

from PIL import Image
from matplotlib import pyplot as plt
from matplotlib._png import read_png
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from numpy import array
import imageio

# ***********************************************************************
#                       Changeable system variables
# ***********************************************************************

# Culture dimensions
width = 15
height = 15

# Culture behavioral parmaters
life_of_culture = 10
age_of_culture = 0

no_of_seeds = 168

# GIF parameters
fps = 1     # Higher the fs, faster the gif animation will be.


# **********************************************************************
#                       Nothing to be changed below
# **********************************************************************

culture = array([[0 for i in range(width)] for j in range(height)])

seeds = []

for _ in range(no_of_seeds):
    seeds.append((r.randint(0, height - 1), r.randint(0, width - 1)))

population = 0

kim = read_png('assets/kim.png')
imagebox = OffsetImage(kim, zoom=.1)
kim_pos = [0,0]

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
                r = next_gen[_, __ + 1]
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
    fig = plt.figure()
    plt.imshow(culture, interpolation = 'nearest')
    plt.title('Generation: ' + str(age_of_culture) + '/' + str(life_of_culture) + '\nPopulation: ' + str(sum(sum(culture))))
    plt.savefig('png/' + str(age_of_culture))
    writeGIF()


def writeGIF():
    file_names = sorted((fn for fn in os.listdir('png') if fn.endswith('.png')), key = lambda s: (s[5:]))
    readImages = []
    for file_names in file_names:
        readImages.append(imageio.imread('./png/' + file_names))
        stdout.write("\r%d" % age_of_culture + '/' + str(life_of_culture) + ' generations recorded.')

    imageio.mimsave('./gif/animation.gif', readImages, fps = fps)

def putKim(culture):
    for _ in range(width):
        for __ in range(height):
            if culture[_,__] == 1:
                fig = plt.gcf()
                fig.clf()
                ax = plt.subplot(111)

                # add a first image
                imagebox = OffsetImage(kim, zoom=.1)
                xy = [0.25, 0.45]               # coordinates to position this image

                ab = AnnotationBbox(imagebox, xy,
                    xybox=(30., -30.),
                    xycoords='data',
                    boxcoords="offset points")
                ax.add_artist(ab)


if __name__ == '__main__':
    # simulate the alphas
    culture = plant_seeds(seeds, culture)
    print_culture(culture)


    # simulate the descendants
    while age_of_culture != life_of_culture:
        culture = simulate()
        age_of_culture += 1
        print_culture(culture)


    # putKim(culture)

    # announce completion of the program
    stdout.write("\nGIF generated in ./gif.")


