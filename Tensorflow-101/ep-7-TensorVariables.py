# Variables in Tensorflow
import tensorflow as tf
my_tensor = tf.constant(
    [[1.0, 2.0], [3.0, 4.0]] )
my_var = tf.Variable(my_tensor)
# Variables can be all kinds of types
bool_var = tf.Variable(
    [False, False, False, True])
complex_var = tf.Variable([5+4j,6+1j])
print("Shape: ", my_var.shape)
print("DType: ", my_var.dtype)
print("As NumPy: ", my_var.numpy())
#variables cannot be reshaped.
print(tf.reshape(my_var, ([1,4])))
my_tensor.assign([1, 2])
# Not allowed as it resizes the variable: 
try:
  my_tensor.assign([1.0, 2.0, 3.0])
except Exception as e:
  print(f"{type(e).__name__}: {e}")
#ValueError: 
# Shapes (2,) and (3,) are incompatible