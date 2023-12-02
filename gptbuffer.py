import numpy as np
import math

class GPTbuffer:
    """Ring buffer class of specified size w specified # of neurons"""

    def __init__(self, bufSize, numNeurons, sigma):
        self.bufSize = bufSize
        self.numNeurons = numNeurons
        self.sigma = sigma
        self.data = [{x : 0 for x in range(numNeurons)} for x in range(bufSize)]
        self.oldest = 0
        self.curpos = 0

    def __repr__(self):
        output = ""
        for i in range(self.bufSize):
            if i == self.oldest:
                output += "OLDEST\n"
            for j in self.data[i]:
                output += "Neuron " + str(j) + ":"
                for k in range(self.data[i][j]):
                    output += "|"
                output += "\n"
            if i == self.curpos:
                output += "CURRENT\n"
            output += "-----\n"
        return output

    def gaussian_spike_count(self, neuron_id, phase):
        mu = phase * (math.pi / 8)  # Mean for the Gaussian distribution
        return int(np.random.normal(mu, self.sigma))

    def add(self, phase):
        for neuron_id in range(self.numNeurons):
            spike_count = self.gaussian_spike_count(neuron_id, phase)
            self.data[self.curpos][neuron_id] = spike_count
        self.curpos = (self.curpos + 1) % self.bufSize
        if self.curpos == self.oldest:
            self.oldest = (self.oldest + 1) % self.bufSize


gbuff = GPTbuffer(5, 2, 5)
gbuff.add(1)
gbuff.add(3)
print(gbuff)