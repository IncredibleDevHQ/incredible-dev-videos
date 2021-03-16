import tensorflow as tf
# You can create constants in TF to hold specific values
a = tf.constant(1)
b = tf.constant(2)

c = a + b
d = a * b

tf.print(c) // output: 3
tf.print(d) // output: 2
