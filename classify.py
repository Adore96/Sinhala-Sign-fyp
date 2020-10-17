# python classify.py --model sinhalasign6.h5 --labelbin lb.pickle --image TestingImages/5.jpg
# 1 ,

import argparse
import pickle

import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
                help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
                help="path to label binarizer")
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
output = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label
# binarizer - check this again.
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

word = ""

# build the label and draw the label on the image
label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, word)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2)

# show the output image
print("[INFO] {}".format(label))
print("[INFO] Image Size ", image.shape)
# print(model.summary())
cv2.imshow("Output", output)
cv2.waitKey(0)
