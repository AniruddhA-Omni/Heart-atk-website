import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('heart.csv')

X = df.iloc[:,0:13]
y = df.iloc[:,13]

#Data preparation
scaler = StandardScaler().fit(X)
standardX = scaler.transform(X)

#model training
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle = True)

model = LogisticRegression(C=0.472, class_weight='balanced', dual=False,
                   fit_intercept=True, intercept_scaling=1, l1_ratio=None,
                   max_iter=1000, multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=123, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)

X_train, X_test, y_train, y_test = train_test_split(standardX, y, random_state=0)

model.fit(X_train, y_train)

