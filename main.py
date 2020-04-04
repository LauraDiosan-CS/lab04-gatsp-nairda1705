import networkx
import os
import random
from datetime import datetime
from chromosome import Chromosome
from geneticalgorithm import GA

def readNetwork(fileName):

    graph = networkx.read_gml(fileName, label = 'id')
    network = {}
    mat = []
    degrees = []
    network['noNodes'] = graph.number_of_nodes()
    network['noEdges'] = graph.number_of_edges()

    mat = [[0 for _ in graph.nodes] for _ in graph.nodes]
    degrees = [0 for _ in graph.nodes]
    
    for vertex, neighbour in graph.edges:
        row = vertex - 1
        column = neighbour - 1

        mat[row][column] = mat[column][row] = 1
        degrees[row] += 1
        degrees[column] += 1

    network['mat'] = mat
    network['degrees'] = degrees
    
    return network


def main():
    currentDir = os.getcwd();
    filePath = os.path.join(currentDir, 'football/football.gml')
    network = readNetwork(filePath)
    params = {'generations': 2000, 'size': 300, 'tournamentSize': 30}

    random.seed(datetime.now())

    geneticAlg = GA(params, network)
    generation = 0
    while generation < params['generations']:
        generation += 1
        geneticAlg.nextGeneration()
        print(geneticAlg.bestChromosome().fitness, geneticAlg.worstChromosome().fitness)
    print(geneticAlg.bestChromosome().decoded())
main()
