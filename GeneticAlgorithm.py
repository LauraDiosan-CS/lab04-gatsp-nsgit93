from random import randint, uniform
from Chromosome import Chromosome

class GA:
    def __init__(self, param=None, fileRepo=None):
        self.__param = param
        self.__fileRepo= fileRepo
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__fileRepo)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__param['function'](c,self.__fileRepo.getDistante())

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2


    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            prob = randint(0,1)
            if prob == 1:
                off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize']-1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            prob = randint(0, 1)
            if prob == 1:
                off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
