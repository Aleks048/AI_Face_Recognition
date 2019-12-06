'''preprocess done on the data to do SVM'''

def preprocessSVM(data,type="",nImages=10):
    if type=="seq":# if we use the sequences as a whole
        flatten = lambda l: [i for ind,im in enumerate(l) for sub in im[2][1] for i in sub if ind<nImages]
        outData = [flatten(ps[1]) for ps in data]
        labels = [ps[0] for ps in data]

    elif type=="zeroPoints":#if we only use the first points of the sequences
        flatten = lambda l: [i for sub in l[2][1] for i in sub]
        outData = [flatten(ps[1][0]) for ps in data]
        labels = [ps[0] for ps in data]
    elif type=="duplPoints":#if we use the points from sequences independently
        flatten = lambda l: [i for sub in l[2][1] for i in sub]
        outData = [flatten(ps) for ps in data]
        labels = [ps[0] for ps in data]
    else:
        raise("no such type dummy")
    
    return outData,labels
def getRidOfSeq(data):
    return [i for seq in data for i in seq[1]]