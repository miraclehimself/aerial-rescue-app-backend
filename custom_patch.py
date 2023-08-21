# custom_patches.py
import tensorflow.compat.v1 as tf

def custom_tf_patch():
    tf.disable_v2_behavior()

# Apply the monkey patch
custom_tf_patch()