'''generates train and test data'''

import os
import random

'''
the idea here is that for evaluation we have 2 protocols:
    1) closed protocol - the tested images were in the DB. task - find the ID of a person.
    2) open protocol - the tested images were not in the DB. task - decide whether the person is in the DB or not.
so train test split generates 3 arrays put together:
    1) train array
    2) cloed protocol test array
    3) open protocol test array
'''
def train_test_split(root_str,train_percent:float=0.8):
    nNamesMoreThanOneVideo = 2827#known from before
    
    '''where we store info'''
    trainFoldersPaths = []#path to folders of the images used in training
    closedProtocolTestFoldersPaths = []#path to folders of the images used in closed protocol testing
    openProtocolTestFoldersPaths = []#path to folders of the images used in open protocol testing
    trainFilesPaths = []#[path,name,[faceframe,facelpoints]] of the images used in training
    closedProtocolTestFilesPaths = []#[path,name,[faceframe,facelpoints]] of the images used in closed protocol testing
    openProtocolTestFilesPaths = []#[path,name,[faceframe,facelpoints]] of the images used in open protocol testing
    
    '''closed protocol index: used to select random images for closed protocol testing'''
    #closedPrIndex used to count the closed protocol images when we do train and test split
    closedPrIndex = 0
    #the sorted indices that we will be set as test for closed protocol evaluation 
    #note: using step 3 to avoid that all of the videos of one name fall into testing
    closedPrTestIndices = random.sample(range(0,nNamesMoreThanOneVideo,3),int(nNamesMoreThanOneVideo*(1-train_percent)))
    closedPrTestIndices.sort()#sorting just to speedup search

    '''travesing the subfolders and files'''
    for root,subdirs,files in os.walk(root_str):
        #collecting paths to the folders
        if len(subdirs)>1 and root!=root_str:  
            # we have more than one video for the person and therefore use it either for           
            for subdir in subdirs:
                if closedPrIndex in closedPrTestIndices:
                    closedProtocolTestFoldersPaths.append(os.path.join(root,subdir))
                else:
                    trainFoldersPaths.append(os.path.join(root,subdir))
                closedPrIndex+=1
        elif len(subdirs)==1 and root!=root_str:
            #if we have only one folder in the images directory
            openProtocolTestFoldersPaths.append(os.path.join(root,subdirs[0]))
        #collecting paths to the images
        elif root!=root_str:
            personsName = root.replace(root_str,"")[1:-2]#name of the person in the video
            if root in trainFoldersPaths:
                seq = []
                for file in files:     
                    seq.append([os.path.join(root,file),personsName])
                trainFilesPaths.append([personsName,seq])
            if root in closedProtocolTestFoldersPaths:
                seq = []
                for file in files:
                    seq.append([os.path.join(root,file),personsName])
                closedProtocolTestFilesPaths.append([personsName,seq])
            if root in openProtocolTestFoldersPaths:
                seq = []
                for file in files:
                    seq.append([os.path.join(root,file),personsName])
                openProtocolTestFilesPaths.append([personsName,seq])
    
    '''cheching results'''
    print("number of train images: ", len(trainFilesPaths))
    print("number of closed protocol test images: ", len(closedProtocolTestFilesPaths))
    print("number of open protocol test images", len(openProtocolTestFilesPaths))
    return [trainFilesPaths,closedProtocolTestFilesPaths,openProtocolTestFilesPaths]

if __name__=="__main__":
    print ("testing...")
    train_test_split(r".\datasets\several_faces_dataset")