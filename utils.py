
def generateOutputString(chromosome):
    outputString = ""
    output = {}
    for i in range(len(chromosome.repres)):
        # print(chromosome.repres[i])
        if chromosome.repres[i] in output:
            output[chromosome.repres[i]] = output[chromosome.repres[i]] + str(i+1) + " "
        else:
            output[chromosome.repres[i]] = str(i+1) + " "
            # print("nou: "+str(chromosome.repres[i]))
    for x,y in output.items():
        outputString = outputString + str(y) + '\n'
    # outputString = outputString + str(chromosome.fitness)
    return outputString
