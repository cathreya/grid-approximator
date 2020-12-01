import matplotlib.pyplot as plt
import numpy as np
import sys

grid = int(sys.argv[1])

with open("points.txt","r") as ifs:
    a = ifs.read()

fig, ax = plt.subplots()
a = a.split("\n")
x = [float(i.split()[0]) for i in a ]
y = [float(i.split()[1]) for i in a ]

print(x,y)

colors = ['k']*len(x)
ax.scatter(x, y, c=colors, alpha=0.5)
ax.set_xlim((0,1))
ax.set_ylim((0,1))
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))
plt.xticks(np.arange(0, 1, 1/grid))
plt.yticks(np.arange(0, 1, 1/grid))
ax.grid(b=True, which='major', color='k', linestyle='--')
plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
fig.savefig('test.png', dpi=600)
plt.close(fig)