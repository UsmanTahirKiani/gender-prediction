import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder, MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
import pickle

df = pd.read_csv("data1.csv")

# print(bankdata.head())
# mlb = MultiLabelBinarizer()
# mhv = mlb.fit_transform(fbrdata['name'].apply(lambda x: set(x.split(' '))))
# df_out = pd.DataFrame(mhv,columns=mlb.classes_)
# enc = OneHotEncoder(sparse=False)
# ohe_vars = ['name'] # specify the list of columns here
# ohv = enc.fit_transform(fbrdata.loc[:,ohe_vars])
# ohe_col_names = ['%s_%s'%(var,cat) for var,cats in zip(ohe_vars, enc.categories_) for cat in cats]
# df_out.assign(**dict(zip(ohe_col_names,ohv.T)))

splitted = df['name'].str.split()
df['first_name'] = splitted.str[0]
df['feature'] = df['first_name']+" "+df['province'].astype(str)
df['feature'] = df['feature'].apply(lambda x: str(x).lower())
df = df[['feature','gender']]
df = df[[len(e)>1 for e in df.feature]]
#df = df.drop_duplicates()
#df.to_csv('data2.csv')
Xfeatures = df["feature"]

cv = CountVectorizer()
X = cv.fit_transform(Xfeatures)
# print(cv.get_feature_names())

y = df["gender"]

# print(fbrdata.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=42)

clf = MultinomialNB()
clf.fit(X_train,y_train)
print(clf.score(X_train,y_train))

sample_name = ["Usman"]
vect = cv.transform(sample_name).toarray()
print(clf.predict(vect))

filename = 'finalized_model1.pkl'
pickle.dump(clf, open(filename, 'wb'))
vectorizer_file = 'vectorizer1.pkl'
pickle.dump(cv, open(vectorizer_file,'wb'))

# svclassifier = SVC(kernel='linear')
# svclassifier.fit(X_train, y_train)

# y_pred = svclassifier.predict(X_test)
#
# print(y_pred)
# print(confusion_matrix(y_test,y_pred))
# print(classification_report(y_test,y_pred))
#