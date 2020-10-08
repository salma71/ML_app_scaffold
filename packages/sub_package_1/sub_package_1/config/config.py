import pathlib

import sub_package_1

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(sub_package_1.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "" # add test data name with extension
TRAINING_DATA_FILE = ""  # add train data name with extension
TARGET = "" # add your target variable


# variables
FEATURES = ["", ""] # add your variables in a string format seperated by commas

# add variables to be dropped afterwards
DROP_FEATURES = ""

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = [""]

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = ["",""]

TEMPORAL_VARS = "" # add temporal vars if not delete it

# variables to log transform
NUMERICALS_LOG_VARS = ["", ""]

# categorical variables to encode
CATEGORICAL_VARS = ["",""]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]


PIPELINE_NAME = "" # add your pipeline name
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
