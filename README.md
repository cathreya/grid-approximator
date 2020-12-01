### Grid Approximator

Given a Treemaker tmd5 file approximates a grid. Work in progress.

To run:
```bash
# Extract points from the tmd5 file
python points_from_tmd.py <filename>.tmd5 <outfilename>.txt
# Compile and run the approximator
g++ grid_approx.cpp -o approx 
./approx <outfilename>.txt # This will print out a grid size
# visualize the point with the output grid
python visualize <grid size> # Output is stored as an image file "test.png"
```
![Sample](test.png)


Issues
- Primitive cost function. Regularizes based on the grid size.
- Might end up mapping multiple points to the same grid intersecton.
- Doesn't account for the actual circle packing yet.
