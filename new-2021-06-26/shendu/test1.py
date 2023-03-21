import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# w = np.array()
# x = np.array()
# b = 1
# for iter in range(100):
#     z = np.dot(w.T,x) + b
#
# res = datasets.load_iris()
# X = res.data
# y = res.target
# # print(X,y)
# cond = y !=2
# # print(cond)
# X = X[cond]
# y = y[cond]
# # print(X,y)
#
# result = train_test_split(X,y,test_size=0.2)
# lr = LogisticRegression()
# lr.fit(result[0],result[2])
# w = lr.coef_
# b = lr.intercept_
# print(w,b)
#
# proba_ = lr.predict_proba(result[1])
# print(proba_)

import numpy as np
import pandas as pd
coman = pd.read_csv('C:\\Users\\domek\\Desktop\\creditcard.csv')
# print(coman.info())
coman.replace([np.inf, -np.inf], np.nan,inplace=True)
coman = coman.fillna(0)
def regularit(df):
    newDataFrame = pd.DataFrame(index=df.index)
    columns = df.columns.tolist()
    for c in columns:
        if (c == 'ID'):
            newDataFrame[c] = df[c].tolist()
        else:
            d = df[c]
            MAX = d.max()
            MIN = d.min()
            newDataFrame[c] = ((d - MIN) / (MAX - MIN)).tolist()
    return newDataFrame
data = regularit(coman)
data.to_csv("C:\\Users\\domek\\Desktop\\a.csv",index=True,sep=',')
print(data)