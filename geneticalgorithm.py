from chromosome import Chromosome
from random import choice, uniform, seed
from datetime import datetime

class GA:
    def __init__(self, params, network):
        self.params = params
        self.network = network
        self.population = [Chromosome(network) for _ in range(params['size'])]

    def nextGeneration(self):
        seed(datetime.now())
        inTournament = set()
        while(len(inTournament) != self.params['tournamentSize']):
            inTournament.add(choice(self.population))
        firstParent = max(inTournament)
        inTournament.remove(firstParent)
        secondParent = max(inTournament)
        offspring = firstParent.crossover(secondParent)
        offspring.mutate()

        worstChromosome = self.worstChromosome()
        if(offspring.fitness > worstChromosome.fitness):
            self.population.remove(worstChromosome)
            self.population.append(offspring)

    def bestChromosome(self):
        return max(self.population)

    def worstChromosome(self):
        return min(self.population)
