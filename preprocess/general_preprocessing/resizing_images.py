import numpy
from PIL import Image

def resize_image(imagePath,savePath,x,y):
    image = Image.open(imagePath)
    imageAr = numpy.asarray(image.resize((x,y)))
    image  = Image.fromarray(imageAr)
    image.save(savePath,"JPEG")
    image.close()
def resize_images(imagesPaths,x,y):
    '''
    !ALERT : resizes inplace
    '''
    for d in imagesPaths:
        for seq in d: 
            for im in seq[1]:
                resize_image(im[0],im[0],x,y)

if __name__=="__main__":
    resize_image(r".\datasets\several_faces_dataset\Aaron_Eckhart\0\aligned_detect_0.555.jpg",r".\datasets\several_faces_dataset\Aaron_Eckhart\0\aligned_detect_my555.jpg",250,250)