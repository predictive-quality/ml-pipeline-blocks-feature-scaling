# Sklearn preprocessing - Feature scaling
The sklearn.preprocessing package provides several common utility functions and transformer classes to change raw feature vectors into a representation that is more suitable for the downstream estimators.

In general, learning algorithms benefit from standardization of the data set. If some outliers are present in the set, robust scalers or transformers are more appropriate. The behaviors of the different scalers, transformers, and normalizers on a dataset containing marginal outliers is highlighted in [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/modules/preprocessing.html).


## Installation

Clone the repository and install all requirements using `pip install -r requirements.txt` .


## Usage

You can run the code in two ways.
1. Use command line flags as arguments `python main.py --input_path= --output_path=...`
2. Use a flagfile.txt which includes the arguments `python main.py --flagfile=example/flagfile.txt`

## Input Flags/Arguments

#### --input_path
Path where input files like dataframes,scaler.pckl for feature scaling where stored.
Could be local filepath or s3 storage path.

#### --output_path
Path where transformed dataframes and the sacler will be stored.

#### --stage
 - fit: fit_transform a dataframe and create a new scaler.
 - transform: use a given scaler and transform a dataframe.
 - inverse: inverse scale a dataframe with a given scaler.

#### --filename_list
List of filenames with dataframes in feather format to scaler or inverse scale.

#### --method
Define on of the following Scaler/Transfrom which should be used for scaling.

 - [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer)
 - [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler)
 - [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler)
 - [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler)
 - [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler)
 - [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer)
 - [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer)

#### --scaler_obj
Filename of the scaler that should be used.

#### --config

It is possible to supply config parameter when no scaler is supplied and a new scaler will be created fit_transform. \
[sklearn.preprocessing](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing)

## Example

First move to the repository directory.
We run e.g. fit and transform for a train dataset with `python main.py --flagfile=ff_fit.txt` \
After that we want to transform a test dataset with the fitted scaler from the train dataset. `python main.py --flagfile=ff_transform.txt`

## Data Set

The data set was recorded with the help of the Festo Polymer GmbH. The features (`x.csv`) are either parameters explicitly set on the injection molding machine or recorded sensor values. The target value (`y.csv`) is a crucial length measured on the parts. We measured with a high precision coordinate-measuring machine at the Laboratory for Machine Tools (WZL) at RWTH Aachen University.