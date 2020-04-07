import os
from geneticalgorithm import GA
from chromosome import Chromosome

def readFromFile(fileName):
    with open(fileName) as file:
        content = [line.strip() for line in file.readlines()]
        dim = int(content.pop(0))
        mat = [[int(number) for number in line.split(',')] for line in content]
        return dim, mat

def main():
    fileName = "hard_02_tsp.txt"
    #fileName = "medium_01_tsp.txt"
    #fileName = "easy_01_tsp.txt"

    currentDir = os.getcwd()
    path = os.path.join(currentDir, fileName)

    dim, mat = readFromFile(path)

    data = {'dim': dim, 'mat': mat, 'city': 0}
    params = {'generations': 5000, 'population': 1000, 'tournament': 100}
    
    ga = GA(params, data)
    gen = 0
    while gen < params['generations']:
        gen += 1
        ga.nextGeneration()
        print(ga.bestChromosome().fitness(), ga.worstChromosome().fitness())
    print(ga.bestChromosome().repres)
main()
