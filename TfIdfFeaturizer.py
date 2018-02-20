from Featurizer import Featurizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


#This is a subclass that extends the abstract class Featurizer.
class TfIdfFeaturizer(Featurizer):

	#The abstract method from the base class is implemeted here to return count features
	def getFeatureRepresentation(self, X_train, X_val):
		tfidf = TfidfVectorizer()
		#print(X_train[0])
		X_train_counts = tfidf.fit_transform(X_train)
		X_val_counts = tfidf.transform(X_val)
		return X_train_counts, X_val_counts

	def get_name(self):
		print "Featurizer: Tf-IDFfeaturizer"