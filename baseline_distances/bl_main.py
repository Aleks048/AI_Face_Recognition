def distances(trData,testData,distFunc):
    closestIndices = []
    for testDp in testData:
        closestIndex = -1
        currDistance = float("inf")
        for i,trDp in enumerate(trData):
            tempDistance = distFunc(testDp,trDp)
            if tempDistance<currDistance:
                closestIndex = i
                currDistance = tempDistance
        closestIndices.append(closestIndex)
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
        print("closest indices",distances(x,y,testDist))
    def testImages():
        import sys
        import numpy
        sys.path.append("./preprocess/general_preprocessing")
        from train_test_split import train_test_split
        train_test_split(".\datasets\several_faces_dataset")


    testImages()
