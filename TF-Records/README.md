# Setting up TensorFlow TF-Records

In this video and scripts, we take directories of images with category labels (e.g. cows, pigs, sheep, ... etc) and output tf record files used in [Tensorflow slims's transfer learning](https://github.com/tensorflow/models/tree/master/research/slim). 

1. Add your images, stored in directories named with the image category, to the DATA directory

2. Run `DivideData.py`: This file will divide the available data according to the train/test split defined on line 8 (defaults to 20%) and save them into a train/validate directory, as expected by TensorFlow's build_image_data.py. Speaking of which... 

3. Download/checkout [build_image_data.py](https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_image_data.py) and add to your project. 
Make the alterations described below. 

4. Run build_image_data.py. 


**_build_image_data.py alterations:_**

1. Download/checkout: [build_image_data.py](https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_image_data.py)

2. Change the following lines:
    * Line 78 to: `tf.app.flags.DEFINE_string('train_directory', 'DATA/train/', ` ...
    * Line 80 to: `tf.app.flags.DEFINE_string('validation_directory', 'DATA/validate/', ...`
    * Line 88 to: `tf.app.flags.DEFINE_string('output_directory', 'C:\\Users\\melissa\\Desktop\\youtubetutorials\\TensorflowRecords\\tmp\\',` ... **NOTE**: the output file needs an absolute path, please update to point to your TensorflowRecords directory
    * Line 106: `tf.app.flags.DEFINE_string('labels_file', 'DATA/labels.txt', 'Labels file')`
    * Line 258: `output_filename = '%s-%.5d-of-%.5d.tfrecords' % (name, shard, num_shards)`
