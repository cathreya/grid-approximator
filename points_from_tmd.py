import sys

if len(sys.argv) < 3:
	print("Specify tmd5 file and output file")
	sys.exit()


with open(sys.argv[1],'r') as ifs:
	a = ifs.read()

b = a.split("\n\n")

pts = []
for i in range(1,len(b)):
	c = b[i].split("\n")
	pts.append((c[0],c[1]))


c = b[0].split("\n")
pts.append((c[2],c[3]))

with open(sys.argv[2],"w") as ofs:
	for c in pts:
		ofs.write("{} {}\n".format(c[0],c[1]))

