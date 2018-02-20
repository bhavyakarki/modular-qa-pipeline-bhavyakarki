from sklearn.feature_extraction.text import HashingVectorizer
from Featurizer import Featurizer



#This is a subclass that extends the abstract class Featurizer.
class HashVectorizer(Featurizer):

	#The abstract method from the base class is implemeted here to return count features
	def getFeatureRepresentation(self, X_train, X_val):
		hash_vect = HashingVectorizer()
		X_train_counts = hash_vect.fit_transform(X_train)
		X_val_counts = hash_vect.transform(X_val)
		return X_train_counts, X_val_counts

	def get_name(self):
		print "Featurizer: Hashvectorizer"