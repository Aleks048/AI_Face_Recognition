import tensorflow as tf


#based on https://github.com/sanku-lib/image_triplet_loss/blob/master/model.py

#triplet loss
class TripletLoass:
    def conv_net(self,x,reuse=False):
        with tf.name_scope("model"):
            with tf.variable_scope("conv1") as scope:
                net = tf.contrib.layers.conv2d(x, 32, [7, 7], activation_fn=tf.nn.relu, padding='SAME',
                                               weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                               scope=scope, reuse=reuse)
                net = tf.contrib.layers.max_pool2d(net, [2, 2], padding='SAME')

            with tf.variable_scope("conv2") as scope:
                net = tf.contrib.layers.conv2d(net, 64, [5, 5], activation_fn=tf.nn.relu, padding='SAME',
                                               weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                               scope=scope, reuse=reuse)
                net = tf.contrib.layers.max_pool2d(net, [2, 2], padding='SAME')

            with tf.variable_scope("conv3") as scope:
                net = tf.contrib.layers.conv2d(net, 128, [3, 3], activation_fn=tf.nn.relu, padding='SAME',
                                               weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                               scope=scope, reuse=reuse)
                net = tf.contrib.layers.max_pool2d(net, [2, 2], padding='SAME')

            with tf.variable_scope("conv4") as scope:
                net = tf.contrib.layers.conv2d(net, 256, [1, 1], activation_fn=tf.nn.relu, padding='SAME',
                                               weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                               scope=scope, reuse=reuse)
                net = tf.contrib.layers.max_pool2d(net, [2, 2], padding='SAME')

            with tf.variable_scope("conv5") as scope:
                net = tf.contrib.layers.conv2d(net, 28, [1, 1], activation_fn=None, padding='SAME',
                                               weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                               scope=scope, reuse=reuse)
                net = tf.contrib.layers.max_pool2d(net, [2, 2], padding='SAME')

            net = tf.contrib.layers.flatten(net)

        return net
    def triplet_loss(self, model_a, model_pos, model_neg, margin):
            #the idea is to 
            dist1 = tf.sqrt(tf.reduce_sum(tf.pow(model_a - model_pos, 2), 1, keepdims=True))
            dist2 = tf.sqrt(tf.reduce_sum(tf.pow(model_a - model_neg, 2), 1, keepdims=True))
            return tf.reduce_mean(tf.maximum(dist1 - dist2 + margin, 0))