import math
'''if distances are computed between the facepoints of the images'''

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from sklearn import preprocessing
'''
two types of distances between images facepoints. 
1) distance betweeen facepoints of the same index
2) distance between differences between point sand n next points. 
        ex: d(a[i]-a[i+1],b[i]-b[i+1])
'''

def facePoints68_DistBetweenPoints(imA,imB,distType="L2"):
    facePointsA = imA[1][0][2][1]
    facePointsB = imB[1][0][2][1]
    dist = 0
    if distType == "L2":
        for i,p in enumerate(facePointsA):
            dist+=math.sqrt(pow(p[0]-facePointsB[i][0],2)+pow(p[1]-facePointsB[i][1],2))
        return dist
    elif distType == "L1":
        for i,p in enumerate(facePointsA):
            dist+=abs(p[0]-facePointsB[i][0])+abs(p[1]-facePointsB[i][1])
        return dist
def facePoints68_DistToNNextPoints(imA,imB,distType="L2",nNextPoints=36):
    #using the zero points of the sequences only
    #print(imA)
    facePointsA = imA[1][0][2][1]
    facePointsB = imB[1][0][2][1]
    dist=0
    if "normalize" in distType:
        facePointsA = preprocessing.scale(facePointsA)
        facePointsB = preprocessing.scale(facePointsB)
    if "L2" in distType:
        for i,_ in enumerate(facePointsA):
            if i<len(facePointsA)-nNextPoints:
                distInA = facePointsA[i]-facePointsA[i+1]
                distInB = facePointsB[i]-facePointsB[i+1]
                dist+=math.sqrt(pow(distInA[0]-distInB[0],2)+pow(distInA[1]-distInB[1],2))
            else: break
            #print(dist)
        return math.sqrt(dist)
    if "L1" in distType:
        for i,_ in enumerate(facePointsA):
            if i<len(facePointsA)-nNextPoints:
                distInA = facePointsA[i]-facePointsA[i+1]
                distInB = facePointsB[i]-facePointsB[i+1]
                dist+= abs(distInA[0]-distInB[0])+abs(distInA[1]-distInB[1])
            else: break
        return dist
    print("try another distance type")
            
        

if __name__=="__main__":
    import sys
    sys.path.append("./utils")
    from read_write import read_npy
    import configparser
    cf = configparser.ConfigParser()
    cf.read("./config.ini")

    dataSet = read_npy(cf.get("datasets","npyAllData"))
    imA = dataSet[0][0]
    imB = dataSet[0][1]
    dist = facePoints68_DistBetweenPoints(imA,imB,"L2")
    print(dist)
    dist = facePoints68_DistBetweenPoints(imA,imB,"L1")
    print(dist)
    dist = facePoints68_DistToNNextPoints(imA,imB,"L2",1)
    print(dist)
    dist = facePoints68_DistToNNextPoints(imA,imB,"L1",1)
    print(dist)