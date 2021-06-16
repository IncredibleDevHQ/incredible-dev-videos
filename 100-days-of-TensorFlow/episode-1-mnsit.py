import tensorflow as tf
# Loading the data
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = 
    mnist.load_data()

# Preprocessing - Normalization
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the network
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# Define a loss function
loss_fn = 
  tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Compile the model
model.compile(optimizer='adam',loss=loss_fn,
              metrics=['accuracy'])
# training
model.fit(x_train, y_train, epochs=2)
# testing
model.evaluate(x_test,y_test) #0.98
# inference
predictions = model(x_test[:1]).numpy()
tf.math.argmax(tf.nn.softmax(predictions).numpy())