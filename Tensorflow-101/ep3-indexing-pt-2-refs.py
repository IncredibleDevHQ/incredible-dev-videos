# Indexing tensors
import tensorflow as tf
rank_1 = tf.constant([0,1,1,2,3,5,8,13,21,34])
print(rank_1.numpy())
# [ 0  1  1  2  3  5  8 13 21 34]
# Rules of indexing
print("First:", rank_1[0].numpy())
# First: 0
print("Last:", rank_1[-1].numpy())
# Last: 34
print("From 2, before 7:", rank_1[2:7].numpy())
# From 2, before 7: [1 2 3 5 8]
print("From 4 to the end:", rank_1[4:].numpy())
# From 4 to the end: [ 3  5  8 13 21 34]
print(rank_1[::-1].numpy())
# [34 21 13  8  5  3  2  1  1  0]