'''
takes the desired amount of samples from the dataset and returns them
'''
import random
import numpy
def sampleDataset(dataset,nSamples):
    indices  = random.sample(range(0,numpy.shape(dataset)[0]),nSamples)
    outShape = numpy.shape(dataset)
    outShape[0] = nSamples
    out = numpy.empty(outShape)
    for i,index in enumerate(indices):
        out[i]=dataset[index]
    return out
