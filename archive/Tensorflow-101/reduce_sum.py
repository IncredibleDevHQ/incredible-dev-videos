# sum all the elements of the array

import tensorflow as tf

def add_array_elements(arr):
  sum = tf.reduce_sum(arr).numpy()
  return sum

x = tf.constant([[1, 1, 1], [1, 1, 1]])
x.numpy()

add_array_elements(x)

