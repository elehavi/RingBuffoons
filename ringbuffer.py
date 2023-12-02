class RingBuffer:
    """Ring buffer class of specified size w specified # of neurons"""

    def __init__(self, bufSize, numNeurons):
        self.bufSize = bufSize
        self.data = [{("Neuron " + str(x)) : 0 for x in range(numNeurons)} for x in range(bufSize)]
        self.begin = 0
        self.end = 0

    def __repr__(self):
        output = ""
        for i in range(self.bufSize):
            if i == self.begin:
                output = output + "BEGIN\n"
            for j in self.data[i]:
                output = output + j + ":"
                for k in range(self.data[i][j]):
                    output = output + "| "

            if i == self.end:
                output = output + "\n END"
            output = output + "\n-----\n"
        return output
    

x = RingBuffer(10, 1)
print(repr(x))