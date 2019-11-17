'''
creating the dataset of type:

'''
import sys
sys.path.append("./preprocess/general_preprocessing")
sys.path.append("./preprocess/facemarks/using_python")

from resizing_images import resize_images
from train_test_split import train_test_split
from generating_facemarks import create_facemarks

import configparser

cf=configparser.ConfigParser()
cf.read("./config.ini")

import csv

if __name__=="__main__":
    #split the train and test data // trData,clPrtestData,openPrTestData
    print("Splitting the data...")
    dataPaths = []
    dataPaths = train_test_split(cf.get("preprocess","preprocessDataset"))
    print("DONE")
    #resize the data
    print("Resizing the images...")
    print("!ALERT!:resizing inplace!!!")
    dimensionsXY = cf.getint("preprocess","forcedImageSizeXY")
    for d in dataPaths:
        resize_images(d,dimensionsXY,dimensionsXY)
    print("DONE")
    print("Adding facemarks to the dataset")
    for d in dataPaths:
        for im in d:
            facemarks = create_facemarks(im[0])
            im.append(facemarks)
    print("DONE")
    print("Saving the data...")
    for d in dataPaths:
        with open(cf.get("preprocess","csvAllData"),"a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(d)
            csvFile.close()
    print("DONE")
    