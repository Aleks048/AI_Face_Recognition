import numpy
from PIL import Image

def resize_image(imagePath,savePath,x,y):
    image = Image.open(imagePath)
    imageAr = numpy.asarray(image.resize((x,y)))
    image  = Image.fromarray(imageAr)
    image.save(savePath,"JPEG")
def resize_images(imagesPaths,x,y):
    '''
    !ALERT : resizes inplace
    '''
    for imP in imagesPaths:
        resize_image(imP,imP,x,y)

if __name__=="__main__":
    resize_image(r".\datasets\several_faces_dataset\Aaron_Eckhart\0\aligned_detect_0.555.jpg",r".\datasets\several_faces_dataset\Aaron_Eckhart\0\aligned_detect_my555.jpg",250,250)