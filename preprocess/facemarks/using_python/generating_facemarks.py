import os
import cv2
import numpy
import configparser


def create_facemarks(imgPath):
    '''
    returnin array of type [[x,y,w,h of fraceframe: int],[68 x,y coordinates of the facemarks: float?]]
    '''   
    img = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
    faces = face_cascade.detectMultiScale(img,1.3,5)  
    for (x,y,w,h) in faces:
        #create landmarks for each detected face, we know each image only contains one face
        #landmarks is a 4D array  len(landmarks) = number of faces in a image 
        ok, landmarks = facemark.fit(img, faces)
        return [faces,landmarks[0][0]]
        
if __name__=="__main__":
    print("testing")
    face_cascade = cv2.CascadeClassifier("./supporting_files/preprocess/facemarks/haarcascade_frontalface_default.xml") 
    facemark = cv2.face.createFacemarkLBF()
    facemark.loadModel("./supporting_files/preprocess/facemarks/lbfmodel.yaml")
    create_facemarks(r"C:\Users\ytr16\Downloads\AI project face recognision\code\datasets\several_faces_dataset\Aaron_Eckhart\0\aligned_detect_0.556.jpg")
else:
    cf = configparser.ConfigParser()
    cf.read(r".\config.ini")
    face_cascade = cv2.CascadeClassifier(cf.get("preprocess","cvCascadeClasifier")) 
    facemark = cv2.face.createFacemarkLBF()
    facemark.loadModel(cf.get("preprocess","cvLbfModel"))