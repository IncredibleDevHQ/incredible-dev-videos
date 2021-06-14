# Manipulating Shapes
import tensorflow as tf
x = tf.constant([[1], [2], [3]])
print(x.shape) # (3, 1)
reshaped = tf.reshape(x, [1, 3])
print(reshaped.shape) # (1, 3)
# rank_3 : tf.Tensor(
# [[[ 0  1  2  3  4]
#   [ 5  6  7  8  9]]
#  [[10 11 12 13 14]
#   [15 16 17 18 19]]
#  [[20 21 22 23 24]
#   [25 26 27 28 29]]])
print(tf.reshape(rank_3, [-1]))
# tf.Tensor(
# [ 0  1  2  3 .... 29],shape=(30,))
print(tf.reshape(rank_3, [3*2, 5]), "\n")
# tf.Tensor(
# [[ 0  1  2  3  4]
#  ....
#  [25 26 27 28 29]],shape=(6, 5)) 
print(tf.reshape(rank_3, [3, -1]))
# tf.Tensor(
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]],shape=(3, 10))