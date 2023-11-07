import tensorflow as tf

# Define constants
a = tf.constant(5)
b = tf.constant(3)

# Perform basic mathematical operations
sum_result = tf.add(a, b)
product_result = tf.multiply(a, b)

# Print the results
with tf.Session() as sess:
    print(f"Sum: {sess.run(sum_result)}")
    print(f"Product: {sess.run(product_result)}")
