from Featurizer import Featurizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


#This is a subclass that extends the abstract class Featurizer.
class TfIdfFeaturizer(Featurizer):

	#The abstract method from the base class is implemeted here to return count features
	def getFeatureRepresentation(self, X_train, X_val):
		
		stopwords=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 
				'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 
						'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 
							'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 
								'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 
									'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 
										'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he',
											 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
											 	 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 	
											 	 	'further', 'was', 'here', 'than']
		tfidf = TfidfVectorizer(stop_words=stopwords)
		#print(X_train[0])

		X_train_counts = tfidf.fit_transform(X_train)
		X_val_counts = tfidf.transform(X_val)
		return X_train_counts, X_val_counts

	def get_name(self):
		print "Featurizer: Tf-IDFfeaturizer"