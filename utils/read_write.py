'''use this one to read and write various files'''

import csv
import ast
import numpy
def write_csv(d,savePath,method):
    with open(savePath,method) as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(d)
            csvFile.close()
def write_npy(d,savePath):
    nFile = numpy.array(d)
    numpy.save(savePath,nFile)
    print("Writing to .npy success")
def read_csv(path):
    #messed up
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        for row in csv_reader:
            print(row[0])
            t = ast.literal_eval(row[0])
            break
    pass
def read_npy(path):
    nFile = numpy.load(path,allow_pickle=True)
    return nFile

if __name__=="__main__":
   print(None in read_npy(r".\supporting_files\dataPathsFramesAndFacemarks.npy"))