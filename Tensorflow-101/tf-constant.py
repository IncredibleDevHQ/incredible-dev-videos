import tensorflow as tf
msg = tf.constant('Hello, TensorFlow!')
print(msg)
# tf.Tensor(b'Hello, TensorFlow!', shape=(), dtype=string)
l = tf.constant([1, 2, 3])
print(l)
# tf.Tensor([1 2 3], shape=(3,), dtype=int32)
print(print(tf.constant([1, 2, 3], dtype=tf.float64)))
# tf.Tensor([1. 2. 3.], shape=(3,), dtype=float64)
tf.constant(0, shape=(2, 3))
# <tf.Tensor: shape=(2, 3), dtype=int32, 
# numpy=array([[0, 0, 0],[0, 0, 0]], dtype=int32)>
