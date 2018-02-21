import abc
from abc import abstractmethod
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score

class Evaluator:
	__metaclass__ = abc.ABCMeta
	@classmethod
	def __init__(self): #constructor for the abstract class
		pass

	#This is a class method that gets accuracy of the model
	@classmethod
	def getAccuracy(self, Y_true, Y_pred):
		accuracy = accuracy_score(Y_true, Y_pred)
		
		print "************************************"
		for i in range(len(Y_true)):
			if Y_pred[i] == Y_true[i]:
				print 1
			else:
				print 0
		return accuracy
	
	#This is a class method that gets precision, recall and f-measure of the model	
	@classmethod
	def getPRF(self, Y_true, Y_pred):
		prf = precision_recall_fscore_support(Y_true, Y_pred, average='macro')
		precision = prf[0]
		recall = prf[1]
		f_measure = prf[2]
		return precision, recall, f_measure

