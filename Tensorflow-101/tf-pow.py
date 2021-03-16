import tensorflow as tf
# You can create constants in TF to hold specific values
def power(a, b):
  return tf.pow(a,b)

a = tf.constant(2)
b = tf.constant(4)

c = power(a, b)

tf.print(c) #prints a power b
