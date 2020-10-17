import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file('sinhalasign6.h5')  # Your model's name
model = converter.convert()
file = open('model7.tflite', 'wb')
file.write(model)
