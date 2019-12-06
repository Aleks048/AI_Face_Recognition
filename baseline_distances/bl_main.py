
'''collects the predictions of the distance methods on the dataset'''

from DistanceFunction import DistanceFunction
def predictions(trData,testData,distFunc:DistanceFunction):
    '''
    args:
        useSeq: whether we treat the sequence as a single datapoint or not 
    '''
    closestIndices = []
    for testDp in testData:
        print("new test dp")
        closestIndex = -1
        currDistance = float("inf")
        for i,trDp in enumerate(trData):
            tempDistance = distFunc.calculateDistance(testDp,trDp)
            if (tempDistance<currDistance) and (trData[i][1]!=testDp[1]):                
                closestIndex = i
                currDistance = tempDistance
        #print([testDp[0],trData[closestIndex][0]])
        closestIndices.append([testDp[0],trData[closestIndex][0]])#get the name
    return closestIndices


if __name__=="__main__":
    def testSimple():
        import random
        def testDist (x,y):
            return abs(x-y)
        x = random.sample(range(0,10),10)
        y = random.sample(range(0,20),3)
        print("x = ",x)
        print("y =",y)
        print("closest indices",predictions(x,y,testDist))
    def testImages():
        import sys
        import numpy
        sys.path.append("./preprocess/general_preprocessing")
        from train_test_split import train_test_split
        train_test_split(".\datasets\several_faces_dataset")
    def testFacepoints():
        pass
        # import numpy
        # import sys
        # sys.path.append("./utils")
        # from read_write import read_npy
        # import configparser
        # cf = configparser.ConfigParser()
        # cf.read("./config.ini")
        # from facePointsDist import facePoints68Dist
        # from facePointsDist import facePoints68L2Dist

        # dataSet = read_npy(cf.get("datasets","npyAllDataTest"))
        # print("l1_distances/open protocol",[predictions(dataSet[0],dataSet[2],facePoints68_DistBetweenPoints)])
        # print("l2_distances/open protocol",predictions(dataSet[0],dataSet[2],facePoints68_DistBetweenPoints))
        #print("l1_distances/open protocol",distances(dataSet[0],dataSet[2],facePoints68L1Dist))
        #print("l1_distances/open protocol",distances(dataSet[0],dataSet[2],facePoints68L2Dist))
    def testFacepointsWithSeq():
        print("hi")
        import numpy
        import sys
        sys.path.append("./utils")
        from read_write import read_npy
        import configparser
        cf = configparser.ConfigParser()
        cf.read("./config.ini")
        from distanceBetweenFacePoints import facePoints68_DistBetweenPoints
        from distanceBetweenFacePoints import facePoints68_DistToNNextPoints
        from distanceBetweenSeq import distanceBetweenSeq
        from DistanceFunction import DistanceSeqFunction
        dataSet = read_npy(cf.get("datasets","npyAllDataTest"))
        # seqA = dataSet[0][1]
        # seqB = dataSet[2][0]


        distFunc = DistanceFunction(facePoints68_DistToNNextPoints,"normalizedL1")
        distSeqFunc = DistanceSeqFunction(distFunc,"normalizedL1",distanceBetweenSeq)
        #print(seqB[1][0][2][1])
        print("hi")
        pred = predictions(dataSet[0],dataSet[1],distSeqFunc)
        print(len([i for i in pred if i[0]==i[1]]))
        print("accuracy: ",len([i for i in pred if i[0]==i[1]])/len(pred))
       # print(numpy.shape(dataSet[2]))

    testFacepointsWithSeq()
