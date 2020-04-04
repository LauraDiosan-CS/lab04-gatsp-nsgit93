from math import sqrt, pow

class FileRepository:
    def __init__(self, inputFileName, outputFileName):
        self.__inputFileName = inputFileName
        self.__outputFileName = outputFileName
        self.__distante = []
        self.__nrOrase = 0
        self.__begin = 0
        self.__end = 0
        # self.readFromFile()


    def readFromFile(self):
        with open(self.__inputFileName,'r') as inputFile:
            # print(file.readline().strip('\n'))
            self.__nrOrase = int(inputFile.readline().strip("\n"))
            contor = 0
            while contor < self.__nrOrase:
                linie = inputFile.readline().strip("\n").strip().split(",")
                distante = []
                for i in range(0,self.__nrOrase):
                    distante.append(int(linie[i]))
                self.__distante.append(distante)
                contor = contor + 1
            self.__begin = int(inputFile.readline().strip("\n"))
            self.__end = int(inputFile.readline().strip("\n"))

    def euclideanDistance(self,x1, y1, x2, y2):
        return sqrt(pow((x1-x2),2) + pow((y1-y2),2))


    def readFromFilePlainCoord(self):
        coordonate = []
        with open(self.__inputFileName,'r') as inputFile:
            self.__nrOrase = int(inputFile.readline().strip("\n"))
            # coordonate = []
            for _ in range(self.__nrOrase):
                coordonate.append((0,0))
            contor = 0
            while contor < self.__nrOrase:
                linie = inputFile.readline().strip("\n").split(" ")
                coordonate[int(linie[0])-1] = (int(linie[1]),int(linie[2]))
                contor = contor + 1
            self.__begin = int(inputFile.readline().strip("\n"))
            self.__end = int(inputFile.readline().strip("\n"))
        for i in range(self.__nrOrase):
            distante = []
            for j in range(self.__nrOrase):
                distante.append(self.euclideanDistance(coordonate[i][0],coordonate[i][1],coordonate[j][0],coordonate[j][1]))
            self.__distante.append(distante)

    def writeToFile(self,linie):
        with open(self.__outputFileName,'w') as outputFile:
            outputFile.write(str(self.__nrOrase)+"\n")
            outputFile.write(linie)


    def getDistante(self):
        return self.__distante

    def getNrOrase(self):
        return self.__nrOrase

    def getBegin(self):
        return self.__begin

    def getEnd(self):
        return self.__end

