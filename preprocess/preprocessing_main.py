'''
creating the dataset of images of the same size of type:
[[persons name,[filePath,name,[[frame coordinates],[facemarks pairs]]]]]
there are 3 datasets merged into 1.
    1)training dataset
    2)closed testing protocol dataset
    3)open testing protocol dataset
'''
import sys
sys.path.append("./preprocess/general_preprocessing")
sys.path.append("./preprocess/facemarks/using_python")
sys.path.append("./utils")

from resizing_images import resize_images
from train_test_split import train_test_split
from generating_facemarks import collect_facemarks
from read_write import write_csv
from read_write import write_npy

import configparser


cf=configparser.ConfigParser()
cf.read("./config.ini")

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

    #uncomment if resize needed
    #resize_images(dataPaths,dimensionsXY,dimensionsXY)
    #augment with facemarks
    #NOTE: we remove the images that the model fails to produce facemarks to
    print("Adding facemarks to the dataset")
    collect_facemarks(dataPaths)
    
    print("DONE")
    print("Saving the data...")
    write_npy(dataPaths,cf.get("datasets","npyAllDataTest"))
    print("DONE")
    