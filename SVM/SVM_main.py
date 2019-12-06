'''fits SVM and does PAC '''

def fitSvm(trsinData,trainLabels):
    clf = svm.LinearSVC(multi_class="crammer_singer",max_iter=10,)
    clf.fit(trsinData,trainLabels)
    return clf
def testSVM(model,testData,testLabels):
    predictions = model.predict(testData)
    return list(zip(testLabels,predictions))
   
if __name__ == "__main__":
    import numpy
    from sklearn import svm
    from sklearn.decomposition import PCA
    
    from copy import deepcopy
    from random import shuffle

    from sys import path
    path.insert(0,"./utils")
    path.insert(0,"./preprocess/SVM")
    
    from read_write import read_npy
    from preprocessSVM import *

    #read the datasets
    import configparser
    cf = configparser.ConfigParser()
    cf.read("./config.ini")

    dataset = read_npy(cf.get("datasets","npyAllDataTest"))
    
    trainData = dataset[0]
    testClosedData = dataset[1]
    
    '''if we want to use the points separately'''
    # trainData = getRidOfSeq(trainData)
    # testClosedData = getRidOfSeq(testClosedData)

    print(numpy.shape(trainData))
    print(numpy.shape(trainData[0]))

    # shuffle(trainData)
    # shuffle(testClosedData)
    #print(trainData[0])
    preparedTrainData,preparedTrainLabels = preprocessSVM(trainData,"zeroPoints",2)
    print(numpy.shape(trainData[0]))
    testClosedData,testClosedLabels = preprocessSVM(testClosedData,"zeroPoints",2)
    
    # print(preparedTrainData[0])
    # pca = PCA(n_components=60)
    # preparedTrainData = pca.fit_transform(preparedTrainData,preparedTrainLabels)
    # testClosedData = pca.fit_transform(testClosedData,testClosedLabels)
    # print(preparedTrainData[0])
    print("hi1")
    model = fitSvm(preparedTrainData,preparedTrainLabels)
    print("hi2")
    evaluation = testSVM(model,testClosedData,testClosedLabels)
    print("hi3")
    print(len([i for i in evaluation if i[0]==i[1]]))
    print("accuracy: ",len([i for i in evaluation if i[0]==i[1]])/len(evaluation))

    # trainData = dataset[0] 
    # testClosedData = dataset[1]
    # testOpenData = dataset[2]
    # trainData,trainLabels = preprocessSVM(trainData,"points",10)
    # testClosedData,testClosedLabels = preprocessSVM(testClosedData,"points",10)
    # testOpenData,testOpenLabels = preprocessSVM(testOpenData,"points",10)

    # model = fitSvm(trainData,trainLabels)
    # evaluation = testSVM(model,testClosedData,testClosedLabels)
    # print(evaluation)