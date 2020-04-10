from chromosome import Chromosome
from random import choice, random

class GA:
    def __init__(self, params = None, data = None):
        self.__params = params
        self.__data = data
        self.__population = [Chromosome(data) for _ in range(params['population'])]

    def nextGeneration(self):
        tournament = []
        while len(tournament) < self.__params['tournament']:
            rnd = choice(range(self.__params['population']))
            if choice not in tournament:
                tournament.append(rnd)
                
        pop = self.__population
        c1 = pop[tournament[0]]
        c2 = pop[tournament[1]]
        
        for pos in tournament:
            if pop[pos] > c1:
                c2 = c1
                c1 = pop[pos]
            elif pop[pos] > c2:
                c2 = pop[pos]
                
        offspring = c1.crossover(c2)
        
        if random() <= self.__params['mutation']:
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
