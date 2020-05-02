import cv2
import numpy as np
import os
from PIL import Image

# place the movie name below,dont forget to mention the movie format also
video = cv2.VideoCapture('movie.mov')

# before running the code sample make a file called 'data' in the same directory
try:
    if not os.path.exists('data'):
        os.mkdir('data')
except OSError:
    print('Error : Creating folder to save images')

# removing garbage values
currentframe = 0
total = 0
total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


# saving the images
while currentframe <= total-1:
    ret, frame = video.read()
    name = './data/frame' + str(currentframe) + '.jpg'
    print('creating ' + name)
    cv2.imwrite(name, frame)

    # img = cv2.imread('./data/')
    # print('Rotating images ' + name)
    # img = img.rotate(270, expand=True)
    # img.save('r'+name, frame)
    currentframe += 1

print('Total Number of Frames in the Video :' + str(total))
video.release()
cv2.destroyAllWindows()
