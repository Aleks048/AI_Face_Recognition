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
    def test():
        import random
        def testDist (x,y):
            return abs(x-y)
        x = random.sample(range(0,10),10)
        y = random.sample(range(0,20),3)
        print("x = ",x)
        print("y =",y)
        print("closest indices",distances(x,y,testDist))
    test()
