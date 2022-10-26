import os

import numpy as np
import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, f1_score
from imblearn.over_sampling import SMOTE


#  读取csv每行的内容
from torch.utils.data import Dataset

for dirname, _, filenames in os.walk('creditcard.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# 显示所有列
pd.set_option('display.max_columns', None)

#
df = pd.read_csv('creditcard.csv')
print(df.head())

## Lest start with Basic EDA
# Check for distinct value count for target variable
# 特征向量
df.Class.value_counts().plot.bar(logy=True)
#
# As visible , target variable is highly imbalanced

# Check for row level duplicates
print("original shape of dataframe :-", df.shape)
print("shape of dataframe after duplicate removal :-", df.drop_duplicates().shape)
# We have duplicates , so lets remove it
df = df.drop_duplicates()


def model_fit(model, x_train, y_train, x_test, y_test, model_name):
    model_cur = model.fit(x_train, y_train)
    predictions = model_cur.predict(x_test)
    model_evaluation(y_test, predictions, model_name)


def model_evaluation(y_test, predictions, model_name):
    print('roc_auc score for ' + model_name + ' is ' + str(roc_auc_score(y_test, predictions)))
    print('f1 score for ' + model_name + ' is ' + str(f1_score(y_test, predictions)))


# Lest draw the heat map to check for correlations
sns.heatmap(df.corr())

# Let's divide the target and predictor variables first and then scale the values
x = df.drop('Class', axis=1)
y = df['Class']
scaler = StandardScaler()
x_new = scaler.fit_transform(x)
x = pd.DataFrame(x_new, columns=x.columns)
# Splitting the data into train and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=42)

models = {'Logisitc regression': LogisticRegression(),
          'Decision tree classifier': DecisionTreeClassifier(),
          'Random forest Classifier': RandomForestClassifier()}


# Creating custom functions to evaulate different models before and after applying SMOTE
for model_name, model in models.items():
    model_fit(model, x_train, y_train, x_test, y_test, model_name)

    # Now we will try the model with SMOTE methodlogy to compare improvements in auc_roc score
sm = SMOTE(random_state=6)
X_train_new, y_train_new = sm.fit_resample(x_train, y_train)

for model_name, model in models.items():
    model_fit(model, X_train_new, y_train_new, x_test, y_test, model_name)


class Data(Dataset):
    def __init__(self):
        contains = pandas.read_csv("./creditcard.csv")
        #   2维 矩阵  [::]
        self.np_data = np.array(contains).astype(dtype=np.float32)[::,1:-1:]
        # self.np_data = (self.np_data-np.min(self.np_data))/(np.max(self.np_data)-np.min(self.np_data))
        self.np_res = np.array(contains).astype(dtype=np.float32)[::,-1::]
        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(self.np_data, self.np_res, test_size=0.1, random_state=0)
        sm = SMOTE()
        # print(len(self.x_train))
        self.x_train, self.y_train = sm.fit_resample(self.x_train, self.y_train)
        # print(len(self.x_train))
        # print(self.y_train.sum())

class MyDataSet(Data):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return len(self.x_train)

    def __getitem__(self, item):
        return (torch.tensor(self.x_train[item]),torch.tensor(np.array([self.y_train[item]])))