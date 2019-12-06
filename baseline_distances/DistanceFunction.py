class DistanceFunction:
    '''
    represents a distance function that measures similarity between objects
    '''
    def __init__(self,distFunc,distType="L2"):
        self.distFunc = distFunc
        self.distType = distType
    def calculateDistance(self,imA,imB):
        return self.distFunc(imA,imB,self.distType)
class DistanceSeqFunction(DistanceFunction):
    '''
    represents a distance function that measures similarity between sequences of objects
    '''
    def __init__(self,distFunc:DistanceFunction,distType="L2",seqDistFunc=None):
        super().__init__(distFunc.distFunc,distType)
        self.seqDistFunc = seqDistFunc
    def calculateDistance(self,seqA,seqB):
        return self.seqDistFunc(seqA,seqB,self.distFunc,self.distType)