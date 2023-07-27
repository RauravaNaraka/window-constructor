from time_window_constructors.time_window_constructor import TimeWindowConstructor
import pandas as pd
from data_partitionings.data_partitioning import DataPartitioning   
from normalizations.normalization import Normalization

if __name__ == "__main__":

    dataframe = pd.read_csv("data/example.csv")

    train_df, val_df, test_df = DataPartitioning.basic_split_data_frame(dataframe = dataframe)

    train_df_normalized, val_df_normalized, test_df_normalized = Normalization.basic_normalization(train_df, val_df, test_df)


