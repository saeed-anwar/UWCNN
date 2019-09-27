from utils import ( 
  imsave,
  prepare_data
)

import time
import os
import matplotlib.pyplot as plt
import re
import numpy as np
import tensorflow as tf
import scipy.io as scio
from ops import *

class T_CNN(object):

  def __init__(self, 
               sess, 
               image_height=230,
               image_width=310,
               label_height=230, 
               label_width=310,
               batch_size=1,
               c_dim=3, 
               checkpoint_dir=None, 
               sample_dir=None,
               test_image_name = None,
               id = None
               ):

    self.sess = sess
    self.is_grayscale = (c_dim == 1)
    self.image_height = image_height
    self.image_width = image_width
    self.label_height = label_height
    self.label_width = label_width
    self.batch_size = batch_size
    self.dropout_keep_prob=0.5
    self.test_image_name = test_image_name
    self.id = id
    self.c_dim = c_dim
    self.df_dim = 64
    self.checkpoint_dir = checkpoint_dir
    self.sample_dir = sample_dir

    self.build_model()

  def build_model(self):
    self.images = tf.placeholder(tf.float32, [self.batch_size, self.image_height, self.image_width, self.c_dim], name='images')
    self.pred_h = self.model()


    self.saver = tf.train.Saver()
    
  def train(self, config):


    # Stochastic gradient descent with the standard backpropagation,var_list=self.model_c_vars
    image_test =  get_image(self.test_image_name,is_grayscale=False)
    shape = image_test.shape
    expand_test = image_test[np.newaxis,:,:,:]
    expand_zero = np.zeros([self.batch_size-1,shape[0],shape[1],shape[2]])
    batch_test_image = np.append(expand_test,expand_zero,axis = 0)

    tf.global_variables_initializer().run()
    
    
    counter = 0
    start_time = time.time()

    if self.load(self.checkpoint_dir):
      print(" [*] Load SUCCESS")
    else:
      print(" [!] Load failed...")
    result_h = self.sess.run(self.pred_h, feed_dict={self.images: batch_test_image})

    _,h ,w , c = result_h.shape
    for id in range(0,1):

        result_h0 = result_h[id,:,:,:].reshape(h , w , 3)
        image_path0 = os.path.join(os.getcwd(), config.sample_dir)
        final = (result_h0+1.)/2 
        #image_path = os.path.join(image_path0, "%2dtest_dehaze.bmp"%(self.id))
        image_path = os.path.join(image_path0, self.test_image_name+'_out.png')
        imsave_lable(final, image_path)


  def model(self):

    with tf.variable_scope("model_h") as scope:
        if self.id > 0: 
          scope.reuse_variables()
        image_conv1 = tf.nn.relu(conv2d(self.images, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze1"))
        image_conv2 = tf.nn.relu(conv2d(image_conv1, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze2"))
        image_conv3 = tf.nn.relu(conv2d(image_conv2, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze3"))
        dehaze_concat1 = tf.concat(axis = 3, values = [image_conv1,image_conv2,image_conv3,self.images])
        image_conv4 = tf.nn.relu(conv2d(dehaze_concat1, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze4"))
        image_conv5 = tf.nn.relu(conv2d(image_conv4, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze5"))
        image_conv6 = tf.nn.relu(conv2d(image_conv5, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze6"))
        dehaze_concat2 = tf.concat(axis = 3, values = [dehaze_concat1,image_conv4,image_conv5,image_conv6])
        image_conv7 = tf.nn.relu(conv2d(dehaze_concat2, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze7"))
        image_conv8 = tf.nn.relu(conv2d(image_conv7, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze8"))
        image_conv9 = tf.nn.relu(conv2d(image_conv8, 16, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze9"))
        dehaze_concat3 = tf.concat(axis = 3, values = [dehaze_concat2,image_conv7,image_conv8,image_conv9])
        image_conv10 = conv2d(dehaze_concat3, 3, k_h=3, k_w=3, d_h=1, d_w=1,name="conv2d_dehaze10")
        out = tf.add(self.images , image_conv10)
    return out

  def save(self, checkpoint_dir, step):
    model_name = "coarse.model"
    model_dir = "%s_%s" % ("coarse", self.label_height)
    checkpoint_dir = os.path.join(checkpoint_dir, model_dir)

    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)

    self.saver.save(self.sess,
                    os.path.join(checkpoint_dir, model_name),
                    global_step=step)

  def load(self, checkpoint_dir):
    print(" [*] Reading checkpoints...")
    model_dir = "%s_%s" % ("coarse", self.label_height)
    checkpoint_dir = os.path.join(checkpoint_dir, model_dir)

    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
        ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
        self.saver.restore(self.sess, os.path.join(checkpoint_dir, ckpt_name))
        return True
    else:
        return False
