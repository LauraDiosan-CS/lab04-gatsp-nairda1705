from chromosome import Chromosome
from random import choice, random

class GA:
    def __init__(self, params = None, data = None):
        self.__params = params
        self.__data = data
        self.__population = [Chromosome(data) for _ in range(params['population'])]

    def nextGeneration(self):
        tournament = set()
        while len(tournament) < self.__params['tournament']:
            tournament.add(choice(self.__population))

        c1 = max(tournament)
        tournament.remove(c1)
        c2 = max(tournament)
        offspring = c1.crossover(c2)
        offspring.inversionMutation()

        worst = self.worstChromosome()
        if offspring > worst:
            self.__population.remove(worst)
            self.__population.append(offspring)

    def population(self):
        return self.__population

    def worstChromosome(self):
        return min(self.__population)
    
    def bestChromosome(self):
        return max(self.__population)
