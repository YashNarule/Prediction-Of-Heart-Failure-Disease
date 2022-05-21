import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import warnings
import pickle
warnings.filterwarnings("ignore")

heart_data = pd.read_csv('D:\\special\\.dist\\project\\Untitled spreadsheet - Sheet1 (2).csv')

X = heart_data.drop(columns='Result', axis=1)
Y = heart_data['Result']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y, random_state=2)



RandomForestClassifierModel = RandomForestClassifier(criterion = 'gini',n_estimators=100,max_depth=5,random_state=33) #criterion can be also : entropy 
RandomForestClassifierModel.fit(X_train, Y_train)

pickle.dump(RandomForestClassifierModel,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

