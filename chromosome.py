from datetime import datetime
import random

class Chromosome:
    #Init
    def __init__(self, network):
        random.seed(datetime.now())
        self.network = network
        self.fitness = 0.0
        #Locus-based representation
        self.genes = [random.choice(self.__getNeighbourListFromAdjacencyMatrix(i))
                             for i in range(network['noNodes'])]
        self.evaluateChromosome()
    
    #Public Methods
    
    def crossover(self, other):
        numberOfNodes = self.network['noNodes']
        bitMask = [random.randint(0,1) for _ in range(numberOfNodes)]

        offspring = Chromosome(self.network)
        offspring.genes = [self.genes[i] if bitMask[i] == 0 else other.genes[i]
                           for i in range(numberOfNodes)]
        offspring.evaluateChromosome()
        return offspring

    def mutate(self):
        geneToMutate = random.choice(range(self.network['noNodes']))
        allele = self.genes[geneToMutate]
        
        newAllele = random.choice(self.__getNeighbourListFromAdjacencyMatrix(allele))
        self.genes[geneToMutate] = newAllele
        
        self.evaluateChromosome()

    def evaluateChromosome(self):
        self.fitness = self.__modularity(self.__decoded())

    def decoded(self):
        return self.__decoded()

    #Private Methods

    def __getNeighbourListFromAdjacencyMatrix(self, node):
        '''
        Helper function that returns the neighbour list
        of a specified node from the adjacency matrix
        '''
        adjMat = self.network['mat']
        
        neighbourList = [node]
        neighbourList += [i for i in range(len(adjMat))
                if adjMat[node][i] == 1]
        return neighbourList

    def __decoded(self):
        '''
        If we can see the locus-based representation as an undirected graph then
        the number of communities is the number of components in the graph
        '''

        rng = range(len(self.genes))
        visited = [False for _ in rng]
        neighbours = [set() for _ in rng]
        communities = [0 for _ in rng]
        community = 0

        for i in rng:
            neighbours[i].add(self.genes[i])
            neighbours[self.genes[i]].add(i)

        stack = []

        for i in rng:
            if not visited[i]:
                stack.append(i)
                community += 1
                while stack:
                    node = stack.pop()
                    communities[node] = community
                    visited[node] = True
                    for neighbour in neighbours[node]:
                        if not visited[neighbour]:
                            stack.append(neighbour)

        return communities

    def __modularity(self, communities):
        noNodes = self.network['noNodes']
        noEdges = self.network['noEdges']
        degrees = self.network['degrees']
        mat = self.network['mat']
        
        M = 2 * noEdges
        Q = 0.0
        for i in range(noNodes):
            for j in range(noNodes):
                if (communities[i] == communities[j]):
                   Q += (mat[i][j] - degrees[i] * degrees[j] / M)
        return Q * 1 / M

    def __eq__(self, other):
        for i in range(len(self.genes)):
            if self.genes[i] != other.genes[i]:
                return False
        return True

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __hash__(self):
        return hash(repr(self))
            
