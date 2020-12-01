import numpy as np
def extract(input_file):
	with open(input_file,'r') as ifs:
		a = ifs.read()

	b = a.split("\n\n")

	pts = []
	for i in range(1,len(b)):
		c = b[i].split("\n")
		pts.append([float(c[0]),float(c[1])])


	c = b[0].split("\n")
	pts.append([float(c[2]),float(c[3])])

	return np.array(pts)