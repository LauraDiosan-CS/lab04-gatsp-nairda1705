import os
import math
from geneticalgorithm import GA
from chromosome import Chromosome

def readBerlin(fileName):
    with open(fileName) as file:
        content = [line.strip().split(' ') for line in file.readlines()]
        coords = [[int(float(number)) for number in coord] for coord in content]

    mat = [[0 for _ in range(len(coords))] for _ in range(len(coords))]
    for coord in coords:
        m = coord[0]
        mx = coord[1]
        my = coord[2]

        for neighbor in coords:
            n = neighbor[0]
            nx = neighbor[1]
            ny = neighbor[2]

            mat[m-1][n-1] = math.sqrt((mx - nx) ** 2 + (my - ny) ** 2)

    return len(mat), mat

def readFromFile(fileName):
    with open(fileName) as file:
        content = [line.strip() for line in file.readlines()]
        dim = int(content.pop(0))
        mat = [[int(number) for number in line.split(',')] for line in content]
        return dim, mat

def main():
    fileName = "berlin52.txt"
    #fileName = "hard_02_tsp.txt"
    #fileName = "medium_01_tsp.txt"
    #fileName = "easy_01_tsp.txt"

    currentDir = os.getcwd()
    path = os.path.join(currentDir, fileName)

    dim, mat = readBerlin(fileName)
    #dim, mat = readFromFile(path)

    data = {'dim': dim, 'mat': mat}
    params = {
        'generations': 10000,
        'population': 700,
        'tournament': 450,
        'mutation': 0.75
    }
    
    ga = GA(params, data)
    prevBest = ga.bestChromosome()
    gen = 0
    while gen < params['generations']:
        gen += 1
        ga.nextGeneration()
        curBest = ga.bestChromosome()
        if curBest > prevBest:
            prevBest = curBest
            print("gen:", gen, "-", curBest.fitness())
            
main()
