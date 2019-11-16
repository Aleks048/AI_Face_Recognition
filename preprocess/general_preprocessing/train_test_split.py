import os
import random
'''
the idea here is that for evaluation we have 2 protocols:
    1) closed protocol - the tested images were in the DB. task - find the ID of a person.
    2) open protocol - the tested images were not in the DB. task - decide whether the person is in the DB or not.
'''
def train_test_plit(root_str,train_percent:float=0.8):
    nNamesMoreThanOneVideo = 2827#known from before
    
    labels = []
    trainFoldersPaths = []
    closedProtocolTestFoldersPaths = []
    openProtocolTestFoldersPaths = []
    trainFilesPaths = []
    closedProtocolTestFilesPaths = []
    openProtocolTestFilesPaths = []

    #used to count the closed protocol images when we do train and test split
    closedPrIndex = 0
    
    #the sorted indices that we will be set as test for closed protocol evaluation 
    #note: using range of 3 to avoid that all of the videos of one name fall into testing
    closedPrTestIndices = random.sample(range(0,nNamesMoreThanOneVideo,3),int(nNamesMoreThanOneVideo*(1-train_percent)))
    closedPrTestIndices.sort()

    for root,subdirs,files in os.walk(root_str):
        if len(subdirs)>1 and root!=root_str:
            
            for subdir in subdirs:
                if closedPrIndex in closedPrTestIndices:
                    closedProtocolTestFoldersPaths.append(root+"\\"+subdir)
                else:
                    trainFoldersPaths.append(root+"\\"+subdir)
                closedPrIndex+=1
        elif len(subdirs)==1 and root!=root_str:
            openProtocolTestFoldersPaths.append(root+"\\"+subdirs[0])
        elif root!=root_str:
            if root in trainFoldersPaths:
                for file in files:
                    trainFilesPaths.append(root+"/"+file)
            if root in closedProtocolTestFoldersPaths:
                for file in files:
                    closedProtocolTestFilesPaths.append(root+"/"+file)
            if root in openProtocolTestFoldersPaths:
                for file in files:
                    openProtocolTestFilesPaths.append(root+"/"+file)
            pass
    print(len(trainFilesPaths))
    print(len(closedProtocolTestFilesPaths))
    print(len(openProtocolTestFilesPaths))
    return trainFilesPaths,closedProtocolTestFilesPaths,openProtocolTestFilesPaths

if __name__=="__main__":
    print ("testing...")
    print(os.getcwd())
    train_test_plit(r".\datasets\aligned_images_DB")