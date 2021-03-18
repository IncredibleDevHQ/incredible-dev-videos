# Indexing tensors
rank_1_tensor = tf.constant([0, 1, 2, 3, 5])
print(rank_1_tensor.numpy())
# Output : [ 0  1  2  3  5]
# Rules of indexing
print("First:", rank_1_tensor[0].numpy())
# First: 0
print("Last:", rank_1_tensor[-1].numpy())
# Last: 34
print("From 2, before 7:", rank_1_tensor[2:7].numpy())
# From 2, before 7: [1 2 3 5 8]
print("From 4 to the end:", rank_1_tensor[4:].numpy())
# From 4 to the end: [ 3  5  8 13 21 34]
print("Reversed:", rank_1_tensor[::-1].numpy())
# Reversed: [5  3  2  1  1  0]
