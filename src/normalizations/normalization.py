

class Normalization():
    
    @classmethod
    def basic_normalization(cls, train_df, val_df, test_df):

        train_mean = train_df.mean()
        train_std = train_df.std()
        train_df_normalized = (train_df - train_mean) / train_std
        val_df_normalized = (val_df - train_mean) / train_std
        test_df_normalized = (test_df - train_mean) / train_std

        return train_df_normalized, val_df_normalized, test_df_normalized