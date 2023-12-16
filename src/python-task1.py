import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# read data
data = pd.read_excel("data/Census-Datensatz.xlsx")
# data.info()
print("Describe, result:\n", data.describe())
print("First 5 lines:\n", data.head())

X = data.drop(
    [
        "income",
        "education",
        "marital-status",
        "native-country",
        "occupation",
        "relationship",
        "workclass",
    ],
    axis=1,
)
y = data["income"]

print("First 5 lines, dropped attributes:\n", X.head())

# find unique values for non-int columns
# unique_vals = pd.DataFrame(columns=X.columns())
for col in X.columns:
    if X.dtypes[col] != "int64":
        unique_vals = X[col].drop_duplicates()
        print("column {}, unique values:\n".format(col), unique_vals)

# replace categoric and ordinal attributes with numeric values
# income
y.replace({"<=50k": 0, ">50k": 1}, inplace=True)
# race
X["race"].replace(
    {
        " White": 0,
        " Black": 1,
        " Asian-Pac-Islander": 2,
        " Amer-Indian-Eskimo": 3,
        " Other": 4,
    },
    inplace=True,
)
# sex
X["sex"].replace({" Male": 0, " Female": 1}, inplace=True)

print("First 5 lines, strings replaced:\n", X.head())

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# calculate mean in numpy

# print(len(X_train.columns))
print("columns: ", X_train.columns)
for col in X_train.columns:
    X_np_train = X_train[col].to_numpy()
    X_np_test = X_test[col].to_numpy()
    # print("col:", col, np_arr.dtype, np_arr.dtype.name)
    if X_np_train.dtype == "int64":
        # print(col, np_arr.mean())
        if X_np_train.mean() != X_np_test.mean():
            print(
                "means for {} differ: train: {}, test: {}".format(
                    col, X_np_train.mean(), X_np_test.mean()
                )
            )
        else:
            print(
                "means for {} are the same in train and test: {}".format(
                    col, X_np_train.mean()
                )
            )
