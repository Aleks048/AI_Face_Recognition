'''
if we use each sequence as a datapoint
'''

def distanceBetweenSeq(seqA,seqB,distBetweenIm,distType):
    dist = 0
    for i,imA in enumerate(seqA[1]):
        distIm = 0#distance from a particular image in seqA
        for j,imB in enumerate(seqB[1]):
            if j<10:
                distIm+=distBetweenIm([seqA[0],[imA]],[seqB[0],[imB]],distType)
            else:
                break
        if i<10:
            dist+=distIm/len(seqB)
        else:
            break
    dist= dist/len(seqA)
    return dist