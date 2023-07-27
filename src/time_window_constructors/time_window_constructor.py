import tensorflow as tf
import numpy as np


class TimeWindowConstructor():


    def __init__(self, dataframe=None, sequence_length=None):
        
        self.dataframe = dataframe
        if dataframe is None:
            raise ValueError("needed dataframe instance")

        self.sequence_length = sequence_length


    
    def array_to_dataset(self, data):
    
        data = np.array(data, dtype=np.float32)
        ds = tf.keras.utils.timeseries_dataset_from_array(
            data = data,
            targets = None,
            sequence_length = self.sequence_length,
            shuffle = True,
            batch_size = None)

        return ds

    def split_features_labels(self, features):
        pass