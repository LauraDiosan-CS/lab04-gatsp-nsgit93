from random import randint


class Chromosome:
    def __init__(self, fileRepo):
        self.__fileRepo= fileRepo
        self.__repres = []
        self.__begin = self.__fileRepo.getBegin()-1
        self.__end = self.__fileRepo.getEnd()-1
        dim = self.__fileRepo.getNrOrase()
        checked = []
        for _ in range(dim):
            checked = checked + [False]
        checked[self.__begin] = True
        checked[self.__end] = True
        for i in range(dim):
            if not checked[i]:
                self.__repres.append(i)
        pos1 = randint(0,dim-3)
        pos2 = randint(0,dim-3)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]
        # print("after init")
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def begin(self):
        return self.__begin

    @property
    def end(self):
        return self.__end

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        dim = self.__fileRepo.getNrOrase()

        pos1 = randint(-1, dim - 1)
        pos2 = randint(-1, dim - 1)
        while pos1 == self.__begin or pos1 == self.__end:
            pos1 = randint(-1, dim - 1)
        while pos2 == self.__begin or pos2 == self.__end:
            pos2 = randint(-1, dim - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < dim - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__fileRepo)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # insert mutation
        dim = self.__fileRepo.getNrOrase()-2
        pos1 = randint(0, dim - 1)
        pos2 = randint(0, dim - 1)
        while pos1 == self.__begin or pos1 == self.__end:
            pos1 = randint(0, dim - 1)
        while pos2 == self.__begin or pos2 == self.__end:
            pos2 = randint(0, dim - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def __str__(self):
        string = ""
        string = string + str(self.__begin+1) + ", "
        for elem in self.__repres:
            string = string + str(elem+1) + ", "
        string = string + str(self.__end+1) + '\n'
        string = string + str(self.fitness) + "\n"
        return string

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __gt__(self, c):
        return self.__fitness > c.__fitness