import sys

if len(sys.argv) < 2:
	print("Specify tmd5 file")
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

with open("points.txt","w") as ofs:
	for c in pts:
		ofs.write("{} {}\n".format(c[0],c[1]))

