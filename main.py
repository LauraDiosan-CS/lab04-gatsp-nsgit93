# from ReadWriteData import *
from GeneticAlgorithm import GA
import warnings
from utils import *
from FileRepo import *
warnings.simplefilter('ignore')

#Stefan Nitica, 225/2


# evaluate the quality of previous communities inside a network
# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/modularity.pdf
def fitness(chromosome,matrix):
    sum = matrix[chromosome.begin][chromosome.repres[0]]
    intermediateDim = len(chromosome.repres)
    for i in range(intermediateDim-1):
        sum = sum + matrix[chromosome.repres[i]][chromosome.repres[i+1]]
    sum = sum + matrix[chromosome.repres[intermediateDim-1]][chromosome.end]
    return sum

#construct network from gml file
def main():
    inputFileName = "medium_02_tsp.txt"
    outputFileName = "medium_02_tsp_computed.txt"
    # inputFileName = "hard_02_tsp_plain_coord.txt"
    # outputFileName = "hard_02_tsp_plain_coord_computed.txt"

    repo = FileRepository(inputFileName,outputFileName)
    repo.readFromFile()
    # repo.readFromFilePlainCoord()

    # initialise GA parameters
    gaParam = {'popSize': 100, 'noGen': 1000,'function': fitness}

    ga = GA(gaParam, repo)
    ga.initialisation()
    ga.evaluation()
    bestChromo = ga.bestChromosome()
    for g in range(gaParam['noGen']):
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g) + ' is: ' + str(bestChromo))
    repo.writeToFile(str(bestChromo))


main()

