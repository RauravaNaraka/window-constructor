import tensorflow as tf
import numpy as np


class TimeWindowConstructor():
    def __init__(self, sequence_length):
        self._sequence_length = sequence_length

    def array_to_dataset(self, data):
        ds = tf.keras.utils.timeseries_dataset_from_array(
            data = data,
            sequence_length = self._sequence_length,
            batch_size = None)

        return ds
