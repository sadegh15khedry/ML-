import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

def split_data(df, feature_column, label_column, test_size=.2, random_state=50):
    # x = df.drop(columns= [feature_column])
    # y = df.drop(columns= [label_column])
    return train_test_split(df[feature_column], df[label_column], test_size=test_size, random_state=random_state)
   

def categorical_encode(df, columns):
    label_encoder = LabelEncoder()
    for column in columns:
        df[column] = label_encoder.fit_transform(df[column])
    
    return df

def normalize_data(df, method, normalization_columns):
    
    if method == 'max_abs':
        for column in normalization_columns:
            df[column] = df[column] / df[column].abs().max()
    elif method == 'min_max':
        for column in normalization_columns: 
            df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())     
    elif method == 'z_score':
        for column in normalization_columns: 
            df[column] = (df[column] - df[column].mean()) / df[column].std()
    elif method == 'robust':
        for column in normalization_columns:
            df[column] = (df[column] - df[column].median()) / (df[column].quantile(0.75) - df[column].quantile(0.25))
    elif method == 'log':
        for column in normalization_columns:
            df[column] = np.log1p(df[column])  # log1p is used to avoid log(0)
    elif method == 'l2':
        df = df.apply(lambda x: x / np.sqrt(np.sum(np.square(x))), axis=1)
    
    return df