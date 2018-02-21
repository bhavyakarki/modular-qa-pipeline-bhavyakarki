from Classifier import Classifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler  

#This is a subclass that extends the abstract class Classifier.
class NNClassifier(Classifier):

	#The abstract method from the base class is implemeted here to return multinomial naive bayes classifier
	def buildClassifier(self, X_features, Y_train):
		# scaling data bec MLP is sensitive to feature scaling

		clf = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(50, 40, 30), random_state=0)

		clf = clf.fit(X_features, Y_train)
		return clf

	def get_name(self):
		print "Classifier: MLPClassifier"