import numpy as np

class RingBuffer:
    """Ring buffer class of specified size w specified # of neurons"""

    def __init__(self, bufSize, numNeurons):
        self.bufSize = bufSize
        self.numNeurons = numNeurons
        self.data = [{x : 0 for x in range(numNeurons)} for x in range(bufSize)]
        self.oldest = 0
        self.curpos = 0

    def __repr__(self):
        output = ""
        for i in range(self.bufSize):
            if i == self.oldest % self.bufSize:
                output = output + "OLDEST\n"
            for j in self.data[i]:
                output = output + "Neuron " + str(j) + ":"
                for k in range(self.data[i][j]):
                    output = output + "|"
                output += "\n"
            if i == self.curpos % self.bufSize:
                output = output + "\n CURRENT"
            output = output + "\n-----\n"
        return output

    def add(self, spikesPerNeuron):
        """ Takes in an ordered list that has
            the number of spikes for each neuron.
            Adds it to the current bin.
            Increments bin """
        currBin = self.data[self.curpos % self.bufSize]
        for i in range(self.numNeurons):
            currBin[i] = spikesPerNeuron[i]
        self.curpos += 1


def calcBufSizebyPhase(data):
    """Calculates number of buffer slots
        based on # of theta phases"""
        #neurons would shift pi/8 ahead of theta phase each time
        #keep track of switches from bin to bin
        #mulyiply by pi/8 to find where u r in rhythm
        # track offset between neurons using theta cycle for bins
    pass

x = RingBuffer(5, 2)
x.add([3, 0])
x.add([2, 1])
x.add([0,2])
x.add([1,3])
x.add([2,2])
print(repr(x))

#TODO/goals: 
# main function takes a certain data set, calculates buffer size, 
# and inputs it into a ring buffer.
# how is the data formatted? how should we parse it to gt the stuff we need?