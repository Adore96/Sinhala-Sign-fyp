import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("model6.tflite")
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quant_model)
