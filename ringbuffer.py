class RingBuffer:
    """Ring buffer class of specified size w specified # of neurons"""

    def __init__(self, bufSize, numNeurons):
        self.bufSize = bufSize
        self.data = [{x : 0 for x in range(numNeurons)} for x in range(bufSize)]
        self.oldest = 0
        self.curpos = 0

    def __repr__(self):
        output = ""
        for i in range(self.bufSize):
            if i == self.oldest:
                output = output + "OLDEST\n"
            for j in self.data[i]:
                output = output + "Neuron " + str(j) + ":"
                for k in range(self.data[i][j]):
                    output = output + "|"

            if i == self.curpos:
                output = output + "\n CURRENT"
            output = output + "\n-----\n"
        return output

    def add(self, spikesPerNeuron):
        pass

def calcBufSizebyPhase:
    """Calculates number of buffer slots
        based on # of theta phases"""
        #neurons would shift pi/8 ahead of theta phase each time
        #keep track of switches from bin to bin
        #mulyiply by pi/8 to find where u r in rhythm
        # track offset between neurons using theta cycle for bins

x = RingBuffer(10, 1)
x.data[0][0] = 3
print(repr(x))