from Classifier import Classifier
from sklearn.svm import SVC


#This is a subclass that extends the abstract class Classifier.
class SVMClassifier(Classifier):

	#The abstract method from the base class is implemeted here to return multinomial naive bayes classifier
	def buildClassifier(self, X_features, Y_train):
		clf = SVC(kernel='linear', C=0.003).fit(X_features, Y_train)
		return clf

	def get_name(self):
		print "Classifier: SVMClassifier"