import tensorflow as tf
# You can create constants in TF to hold specific values
a = tf.constant(1)
b = tf.constant(2)

c = tf.add(a,b) 
d = tf.multiply(a, b)

tf.print(c)
tf.print(d)
