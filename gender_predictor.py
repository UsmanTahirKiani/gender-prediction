import pickle
# from sklearn.feature_extraction.text import CountVectorizer

loaded_model = pickle.load(open('finalized_model1.pkl', 'rb'))
cv = pickle.load(open('vectorizer1.pkl', 'rb'))
# cv = CountVectorizer()

sample_name = ["naseem punjab"]
vect = cv.transform(sample_name).toarray()
print(loaded_model.predict(vect))
