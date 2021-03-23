# Broadcasting
import tensorflow as tf
x = tf.constant([1, 2, 3])
y = tf.constant(2)
z = tf.constant([2, 2, 2])
tf.print(tf.multiply(x, 2)) #[2 4 6]
tf.print(x * y) #[2 4 6]
tf.print(x * z) #[2 4 6]
x = tf.reshape(x,[3,1])
y = tf.range(1, 5)
print(tf.multiply(x, y))
# [[ 1  2  3  4]
#  [ 2  4  6  8]
#  [ 3  6  9 12]]
x_stretch = tf.constant(
    [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]])
y_stretch = tf.constant(
    [[1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]])
print(x_stretch * y_stretch)
print(tf.broadcast_to(
    tf.constant([1, 2, 3,4]), [3, 4]
    ))