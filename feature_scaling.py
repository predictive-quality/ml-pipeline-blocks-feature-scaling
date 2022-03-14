# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from sklearn.preprocessing import Normalizer,MinMaxScaler,MaxAbsScaler,StandardScaler,RobustScaler,QuantileTransformer,PowerTransformer
import pandas as pd
import os
from absl import logging

def scale(dataframe,method,scaler,config):
    """Scale features with choosen method

    Args:
        input_path (sring): Path to find features
        output_path (string): Path to save scaled features and the scaler 
        filename_scaled (list): Filenames of features which will get scaled
        method (string): Defines method of scaling process.
        scaler (obj): sklearn scaler object which was load in main.py
    """   

    already_fitted = False

    if scaler != None:
        already_fitted = True

    elif method == 'Normalizer':
        scaler = Normalizer()

    elif method == 'MinMaxScaler':
        scaler = MinMaxScaler()

    elif method == 'MaxAbsScaler':
        scaler = MaxAbsScaler()
    
    elif method == 'StandardScaler':
        scaler = StandardScaler()

    elif method == 'RobustScaler':
        scaler = RobustScaler()

    elif method == 'QuantileTransformer':
        scaler = QuantileTransformer()

    elif method == 'PowerTransformer':
        scaler = PowerTransformer()
    else:
        raise Exception('Scaler method: {} is invalid!'.format(method))
        
    if config != None:
        scaler.set_params(**config)


    dataframe_head = dataframe.columns.values
    if already_fitted == False:
        dataframe_scaled = scaler.fit_transform(dataframe)
    else:
        dataframe_scaled = scaler.transform(dataframe)
    dataframe_scaled = pd.DataFrame(dataframe_scaled,columns=dataframe_head)
    logging.info('File got scaled with method {}'.format(scaler))
    
    return scaler, dataframe_scaled

def inverse_scale(dataframe,scaler):
    """Inverse Scale Dataframes.

    Args:
        input_path (sring): Path to find scaled features and their scaler
        output_path (string): Path to save inverse scaled features
        filename_scaled (list): Filenames of scaled features
        scaler (obj): sklearn scaler object which was load in main.py
    """


    scaler_str = str(scaler)
    if scaler_str == 'Normalizer()':
        logging.warning('Normalizer has no function for inverse scaling!')
    else:
        dataframe_head = dataframe.columns.values
        dataframe_inverse_scaled = scaler.inverse_transform(dataframe)        
        dataframe_inverse_scaled = pd.DataFrame(dataframe_inverse_scaled,columns=dataframe_head)
        logging.info('File got inverse scaled with method {}'.format(scaler))
    
    return dataframe_inverse_scaled