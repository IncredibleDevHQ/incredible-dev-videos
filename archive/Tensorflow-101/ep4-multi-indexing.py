# Multi Indexing a Tensor
import tensorflow as tf
rank_2 = tf.constant(
[[1, 2],[3, 4],[5, 6]], dtype=tf.float16)

print(rank_2[1, 1].numpy())
# 4.0

print("Second row:", rank_2[1, :].numpy())
# Second row: [3. 4.]

print("Second column:", rank_2[:, 1].numpy())
# Second column: [2. 4. 6.]

# Skip first row :
rank_2[1:, :].numpy()
# [[3. 4.] [5. 6.]]