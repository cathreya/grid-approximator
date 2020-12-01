import numpy as np
from math import floor
from sys import argv, exit

regularization_param = 0.01

def get_grid(x, grid):
	return floor(grid*x)


def cost(grid, pt):
	global regularization_param
	sum_sq_error = 0
	for i in range(len(pt)):
		before_x = get_grid(pt[i][0], grid)
		before_y = get_grid(pt[i][1], grid)
		after_x = before_x + 1
		after_y = before_y + 1
		min_dist = np.linalg.norm(pt[i] - np.array([before_x/grid, before_y/grid]))
		min_dist = min(min_dist, np.linalg.norm(pt[i] - np.array([after_x/grid, before_y/grid])))
		min_dist = min(min_dist, np.linalg.norm(pt[i] - np.array([after_x/grid, after_y/grid])))
		min_dist = min(min_dist, np.linalg.norm(pt[i] - np.array([before_x/grid, after_y/grid])))
		sum_sq_error += min_dist

	return sum_sq_error + regularization_param * grid


def search(pt):
	mincost = 1e9
	arg_min = 0
	for grid in range(2,257):
		ncost = cost(grid,pt)
		if ncost < mincost:
			mincost = ncost
			arg_min = grid

	return arg_min,mincost


