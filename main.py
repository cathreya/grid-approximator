from grid_approx import search
from points_from_tmd import extract
from visualize import plot
from sys import argv,exit

def main():
	if(len(argv) < 2):
		print("Provide input tmd5")
		exit(1)

	inf = argv[1]
	outf = "test.png"

	pts = extract(inf)
	grid, error = search(pts)
	print("Use a {} grid. Cost: {}".format(grid,error))

	plot(grid, pts, outf)

if __name__ == "__main__":
	main()