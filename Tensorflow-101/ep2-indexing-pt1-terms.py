# Indexing - Shapes terminology
import tensorflow as tf
rank_4 = tf.zeros([3, 2, 4, 5])
# Shape: The length (no of elements) of each of the axes
print("Shape of tensor:", rank_4.shape) 
# Shape of tensor: (3, 2, 4, 5)
# Rank: Number of tensor axes. 
print("Number of axes:", rank_4.ndim) # Number of axes: 4
# Axis or Dimension: A particular dimension of a tensor.
print("Elements along axis 0 of tensor:", rank_4.shape[0])
# Elements along axis 0 of tensor: 3
# Size: The total number of items in the tensor
print("Total number of elements (3*2*4*5): ", tf.size(rank_4).numpy())
# Total number of elements (3*2*4*5):  120