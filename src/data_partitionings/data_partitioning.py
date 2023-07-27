import pandas as pd

class DataPartitioning():


    @classmethod
    def basic_split_data_frame(cls, dataframe):
        # Standard split function for dataset
        
        n = len(dataframe)
        train_df = dataframe[0:int(n*0.7)]
        val_df = dataframe[int(n*0.7):int(n*0.9)]
        test_df = dataframe[int(n*0.9):]

        return train_df, val_df, test_df
    

    
