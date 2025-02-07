import tensorflow as tf
from tensorflow.python.client import device_lib

print("TensorFlow Version:", tf.__version__)

print(device_lib.list_local_devices())

print("cuDNN Available:", tf.test.is_built_with_cuda())
print("GPU Available:", len(tf.config.list_physical_devices('GPU')) > 0)