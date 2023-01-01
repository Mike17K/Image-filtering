from PIL import Image
import numpy as np
import math
import sys




def f(X,n):
    dataMatlab=[
        116.358502790926,
-4.02681194230038,
0.490712205518890,
0.0582310468874797,
0.000599476933138634,
-0.000197674433276772,
-1.44000356960759e-06]

    a0=dataMatlab[0]
    a1x=dataMatlab[1]
    a1y=dataMatlab[2]
    a2x=dataMatlab[3]
    a2y =dataMatlab[4]
    a3x =dataMatlab[5]
    a3y =dataMatlab[6]
    if X[2]<a0+a1x*X[0]+a1y*X[1]+a2x*X[0]*X[0]+a2y*X[1]*X[1]+a3x*X[0]*X[0]*X[0]+a3y*X[1]*X[1]*X[1]:
        return X[n]

    return 0#int(X[n]*0.9)

    
def filter(arrRef,arrCopy):
    
    hight = len(image_array)
    width = len(image_array[0])
    
    for y in range(hight):
        for x in range(width):
            temp = arrRef[y][x]            
            arrCopy[y][x]=[f(temp,0),f(temp,1),f(temp,2)]

def smooth(arrRef,arrCopy):
    hight = len(image_array)
    width = len(image_array[0])
    
    for y in range(1,hight-1):
        for x in range(1,width-1):
            temp = arrRef[y][x]
            '''
            arrCopy[y][x][0]=int()/9)
            arrCopy[y][x][1]=int()/9)
            arrCopy[y][x][2]=int()/9)
            '''



#find image (add code)
filename = "image.jpg"

#image open
try:
    im = Image.open(filename)
except:
    sys.exit()

image_array = np.array(im) #create table of the image
image_copy = np.array(im) #create copy table of the image
image_copy_2 = np.array(im) #create copy table of the image

array_y = len(image_array)
array_x = len(image_array[0])

print('image dimentions are: ',end='')
print('y: '+ str(array_y) +' x: ' +str(array_x))


filter(image_array,image_copy)
#smooth(image_copy,image_copy_2)

######################################


####################################

#save to file
im = Image.fromarray(image_copy)
im.save(filename[:-4]+'_filtered'+'.png')





































