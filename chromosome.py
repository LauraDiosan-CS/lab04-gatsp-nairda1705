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
        self.__repres = generateARandomPermutation(problParam['dim'])
        self.__fitness = 0
        self.computeFitness()

    @property
    def repres(self):
        return self.__repres
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l

    def fitness(self):
        return self.__fitness
    
    def crossover(self, c):
        pos1 = randint(0, self.__problParam['dim'] - 1)
        pos2 = randint(0, self.__problParam['dim'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1 
        k = 0
        newrepres = self.__repres[pos1 : pos2]
        for el in c.__repres[pos2:] +c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['dim'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        offspring.computeFitness()
        return offspring

    
    def inversionMutation(self):
        pos1 = randint(0, self.__problParam['dim'] - 1)
        pos2 = randint(0, self.__problParam['dim'] - 1)
        
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1

        for i in range(pos1, (pos1+pos2+1)//2):
            self.repres[i], self.repres[pos2-i+pos1] = self.repres[pos2-i+pos1], self.repres[i]

        self.computeFitness()
        
    def computeFitness(self):
        fit = 0
        for i in range(self.__problParam['dim']-1):
            fit += self.__problParam['mat'][self.repres[i]][self.repres[i+1]]
        self.__fitness = fit

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
