import tensorflow as tf
import PythonPong
import numpy as np
import random

#Up, Down, Stay
ACTIONS = 3 

#Learning rate
GAMMA = 0.99

#for updating our gradient or training over time
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05

#Frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000

#Exprerience store
REPLAY_MEMORY = 500000

#Batch size to train on
BATCH = 100

def createGraph():
    W_conv1 = tf.Variable(tf.zeros([8,8,4,32]))
    b_conv1 = tf.Variable(tf.zeros([32]))

    W_conv2 = tf.Variable(tf.zeros([4,4,32,64]))
    b_conv2 = tf.Variable(tf.zeros([64]))

    W_conv3 = tf.Variable(tf.zeros([3,3,64,64]))
    b_conv3 = tf.Variable(tf.zeros([64]))


