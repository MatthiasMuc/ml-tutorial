import pandas as pd
import numpy as np
import matplotlib as mpl

# from sklearn.model_selection import train_test_split


def prepare_data(data):
    data.drop(
        [
            "education",
            "marital-status",
            "native-country",
            "occupation",
            "relationship",
            "workclass",
        ],
        axis=1,
    )
    return


# read data
data = pd.read_excel("data/Census-Datensatz.xlsx")

prepare_data(data)

# just for me
print(data.corr())

print(pd.plotting.scatter_matrix(data))
