import sys
import os



counteasy = 0
counttough = 0
countreg = 0
countimp = 0 

try:
    with open(str(sys.argv[1]), "r") as input:
        linesA = input.readlines()
    with open(str(sys.argv[2]), "r") as input:
    	linesB = input.readlines()
except IOError:
    print "Error: File not found"
else:
	linesA = str(linesA).strip('\r\n').split(',')
	linesB = str(linesB).strip('\r\n').split(',')

	for i in range(len(linesA)):
		if linesA[i] == "0" and linesB[i] == "0":
			counttough += 1
		elif linesA[i] == "1" and linesB[i] == "1":
			counteasy += 1
		elif linesA[i] == "0" and linesB[i] == "1":
			countimp += 1
		elif linesA[i] == "1" and linesB[i] == "0":
			countreg += 1

	print("Easy inputs = ", counteasy)
	print("tough inputs  = ", counttough)
	print("improvement count = ", countimp)
	print("regression count = ", countreg)