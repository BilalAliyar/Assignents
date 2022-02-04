import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

#Read dataset
data = pd.read_excel("iris.xls")
data.isnull().sum()

y = data["Classification"]
X = data.drop(["Classification"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.25)


nmclf = RandomForestClassifier(n_estimators=50)

model = nmclf.fit(X_train, y_train)

pickle.dump(nmclf, open('model.pkl', 'wb'))