
#Import necessary Libraries
import pandas as pd
import numpy as np

import string
import re
import os

import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import TextVectorization
from tensorflow import keras
from tensorflow.keras import layers

from params import *

my_df = pd.read_csv("Dataset/data.csv")
print("**********************")
my_df.head()