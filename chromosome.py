from random import randint, seed, choice

def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm

# permutation-based representation
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam  #problParam has to store the number of nodes/cities
        perm = generateARandomPermutation(problParam['dim'])
        perm.remove(problParam['city'])
        self.__repres = perm
    
    @property
    def repres(self):
        return self.__repres
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l

    def fitness(self):
        mat = self.__problParam['mat']
        city = self.__problParam['city']
        cities = self.__repres
        fitness = mat[city][cities[0]] + mat[cities[len(cities) - 1]][city]
        for i in range(len(cities) - 1):
            fitness += mat[cities[i]][cities[i+1]]
        return fitness
    
    def crossover(self, c):
        # cyclic order
        genes = [None for _ in range(self.__problParam['dim']-1)]
        visited = [False for _ in range(self.__problParam['dim']-1)]
        cycles = []
        k = 0
        while k < self.__problParam['dim'] - 1:
            cycle = [k]
            visited[k] = True
            l = self.repres.index(c.repres[k])
            while l != k:
                cycle.append(l)
                visited[l] = True
                l = self.repres.index(c.repres[l])
            while k < self.__problParam['dim'] - 1 and visited[k]:
                k += 1
            cycles.append(cycle)
        
        for i in range(len(cycles)):
            for pos in cycles[i]:
                genes[pos] = self.repres[pos] if i % 2 == 0 else c.repres[pos]
            
        offspring = Chromosome(self.__problParam)
        offspring.repres = genes
        return offspring
    
    def inversionMutation(self):
        pos1 = randint(0, self.__problParam['dim'] - 2)
        pos2 = randint(0, self.__problParam['dim'] - 2)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1

        for i in range(pos1,pos2):
            self.repres[i], self.repres[i-pos2+pos1] = self.repres[i-pos2+pos1], self.repres[i]

    def k8Mutation(self):
        mid = (self.__problParam['dim'] - 1) // 2
        pos1 = randint(0, mid)
        pos2 = randint(0, mid)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1

        for i in range(pos1,pos2+1):
            self.repres[i], self.repres[i+mid] = self.repres[i+mid], self.repres[i]
         
        
    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.fitness())
    
    def __repr__(self):
        return self.__str__()

    def __gt__(self, c):
        return self.fitness() < c.fitness()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.fitness() == c.fitness()

    def __hash__(self):
        return hash(repr(self))
