

import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model("sinhalasign.h5")
tfmodel = converter.convert()
open ('model.tflite' , "wb") .write(tfmodel)