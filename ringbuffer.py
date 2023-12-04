import numpy as np
import math

class RingBuffer:
    """Ring buffer class of specified size w specified # of neurons"""

    def __init__(self, numNeurons=3, binSize=math.pi/4):
        self.binSize = binSize
        self.numBins = calcNumBinsbyPhase(binSize, numNeurons) # each bin represents 2pi (one period of theta)
        self.numNeurons = numNeurons #each neurons spike should take 3 periods
        self.data = [{x : 0 for x in range(numNeurons)} for x in range(self.numBins)]
        self.oldest = 0
        self.curpos = 0

    def __repr__(self):
        output = ""
        for i in range(self.numBins):
            if i == 0:
                binTitle = "PT"
            else:
                binTitle = str(self.binSize/(math.pi)*i) + "π"
            output = output + "\n--"+ binTitle +"--\n"
            if i == self.oldest % self.numBins:
                output = output + "OLDEST\n"
            for j in self.data[i]:
                output = output + "Neuron " + str(j) + ":"
                for k in range(self.data[i][j]):
                    output = output + "|"
                output += "\n"
            if i == self.curpos % self.numBins:
                output = output + "\n CURRENT"
        output = output + "\n-----\n"
        return output




    def add(self, spikesPerNeuron):
        """ Takes in an ordered list that has
            the number of spikes for each neuron.
            Adds it to the current bin.
            Increments bin """
        if self.curpos == self.oldest:
            self.oldest +=1
        currBin = self.data[self.curpos % self.numBins]
        for i in range(self.numNeurons):
            currBin[i] = spikesPerNeuron[i]
        self.curpos += 1
    
    

def calcNumBinsbyPhase(binSize, numNeurons):
    """Calculates number of buffer slots
        based on # of theta phases"""
    totalWave = 6*math.pi + 2*math.pi*(numNeurons-1)
    return int(totalWave/binSize)

def generateData(binSize, numNeurons):
    # each neuron starts @ 2pi/binsize-1
    # sample from gaussian
    pass

#tests
x = RingBuffer()
x.add([3, 0, 0])
x.add([2, 1, 0])
print(repr(x))

#TODO:generate data gaussianly

#TODO/goals: 
# main function takes a certain data set, calculates buffer size, 
# and inputs it into a ring buffer.
# how is the data formatted? how should we parse it to gt the stuff we need?