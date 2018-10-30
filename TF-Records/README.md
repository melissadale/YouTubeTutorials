# Setting up TensorFlow TF-Records

In this video, 
 * 



**_build_image_data.py alterations:_**

1. download/checkout: [build_image_data.py](https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_image_data.py)
2. change the following lines:
    * Line 78: `tf.app.flags.DEFINE_string('train_directory', 'DATA/train/', ` ...
    * Line 80: `tf.app.flags.DEFINE_string('validation_directory', 'DATA/validate/', ...`
    * Line 88: `C:\\Users\\dalemeli\\Desktop\\youtubetutorials\\TensorflowRecords\\tmp\\`
    * Line 106: `tf.app.flags.DEFINE_string('labels_file', 'DATA/labels.txt', 'Labels file')`
    * Line 258: `output_filename = '%s-%.5d-of-%.5d.tfrecords' % (name, shard, num_shards)
`