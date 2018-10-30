# Setting up TensorFlow TF-Records

In this video and scripts, we take directories of images with category labels (e.g. cows, pigs, sheep, ... etc) and output tf record files used in [Tensorflow slims's transfer learning](https://github.com/tensorflow/models/tree/master/research/slim). 



**_build_image_data.py alterations:_**

1. Download/checkout: [build_image_data.py](https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_image_data.py)

2. Change the following lines:
    * Line 78 to: `tf.app.flags.DEFINE_string('train_directory', 'DATA/train/', ` ...
    * Line 80 to: `tf.app.flags.DEFINE_string('validation_directory', 'DATA/validate/', ...`
    * Line 88 to: `tf.app.flags.DEFINE_string('output_directory', 'C:\\Users\\dalemeli\\Desktop\\youtubetutorials\\TensorflowRecords\\tmp\\',` ...
    * Line 106: `tf.app.flags.DEFINE_string('labels_file', 'DATA/labels.txt', 'Labels file')`
    * Line 258: `output_filename = '%s-%.5d-of-%.5d.tfrecords' % (name, shard, num_shards)
