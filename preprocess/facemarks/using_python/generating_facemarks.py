import os
import cv2
import csv
from ipynb.fs.full.config import getItem_string

face_cascade = cv2.CascadeClassifier(getItem_string("opencv","cascadeclassifier")) 
facemark = cv2.face.createFacemarkLBF()


def saveCSV(data):
    #store all names
    names = []
    #no A face image in A directory
    noFaceImg=[]
    #unrecognized face 
    unrecognized=[]
    #read directies in the path
    path_list=os.listdir(data)
    #sort directies
    path_list.sort()  
    #read all face images from directory
    for subDirname in path_list:
        #each subDirname represents a person
        subjectPath = os.path.join(data,subDirname)
        if os.path.isdir(subjectPath):    
            #store face images of a person
            images = []
            #for each face image of a person
            for fileName in os.listdir(subjectPath):
                imgPath = os.path.join(subjectPath,fileName)
                #convert into grascale
                img = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
                images.append(img)          
            #for each person, there could be many face images,therefore many facemarks, store them in a list
            landmark=[]
            #if there exist a image
            if len(images)>0:  
                #for each person 
                for face_image in images:
                    #detect faces
                    faces = face_cascade.detectMultiScale(face_image,1.3,5)  
                    for (x,y,w,h) in faces:
                        #create landmarks for each detected face, we know each image only contains one face
                        #landmarks is a 4D array  len(landmarks) = number of faces in a image 
                        ok, landmarks = facemark.fit(face_image, faces)
                        #if there are more than one face images from one person, add all facemarks of him into a list 
                        for i in landmarks[0][0]:#landmarks[0][0] = [[x,y] [x,y] [x,y] [x,y]], innner array are coordinates
                            landmark.append(i) # i is a coordinate 
                #save landmarks into csv
                f=open(getItem_string("opencv","landmarkcsv"),'a')
                writer = csv.writer(f,lineterminator='\n')
                if len(landmark)>0:
                    #add that detected person in a names list 
                    names.append(subDirname)
                    #if landmarks is detected successfully, we just choose first one (there could be more than one landmarks in list)
                    for i in range(68):
                        writer.writerow(landmark[i])
                else :
                   unrecognized.append(subDirname)
                f.close()
            else:#no face images
                noFaceImg.append(subDirname) 
            with open(getItem_string("opencv","outputtxt"),"w") as f:
                for i in names:
                    f.write(i)
                    f.write('\n')
    return names,len(names),noFaceImg,unrecognized