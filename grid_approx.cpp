#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>

double regularization_param = 0.005;

struct Point{
	double x,y;
};

double dist(double x1, double y1,double x2,double y2){
	return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
}

int get_grid(double x, int grid){
	return floor(grid*x);
}

double cost(int grid, std::vector<Point>& pt){

	double sum_sq_error = 0;
	for(int i=0;i<(int)pt.size();i++){
		int before_x = get_grid(pt[i].x, grid);
		int before_y = get_grid(pt[i].y, grid);
		int after_x = before_x + 1;
		int after_y = before_y + 1;
		double min_dist = dist(pt[i].x, pt[i].y, (double)before_x/grid, (double)before_y/grid);
		min_dist = std::min(min_dist, dist(pt[i].x, pt[i].y, (double)before_x/grid, (double)after_y/grid));
		min_dist = std::min(min_dist, dist(pt[i].x, pt[i].y, (double)after_x/grid, (double)after_y/grid));
		min_dist = std::min(min_dist, dist(pt[i].x, pt[i].y, (double)after_x/grid, (double)before_y/grid));
		sum_sq_error += min_dist;
	}

	return sum_sq_error + regularization_param * grid;
}

int main(int argc, char* argv[]){
	if(argc < 2){
		std::cout<<"USAGE ./"<<argv[0]<<" input-filename"<<std::endl;
		return 1;
	}

	std::vector<Point> pt;
	std::ifstream ifs(argv[1]);

	Point p;
	while(ifs>>p.x>>p.y){
		pt.push_back(p);
	}

	double mincost = 1e9;
	int arg_min = 0;

	for(int grid = 2; grid < 256; grid ++){
		double ncost = cost(grid, pt);
		if(ncost < mincost){
			mincost = ncost;
			arg_min = grid;
		}
	}

	std::cout<<"Use a "<<arg_min<<" grid. Cost: "<<mincost<<std::endl;



	return 0;
}