from matplotlib import pyplot as plt
import random

def midpt(p1,p2):
  return (p1[0]+p2[0])/2,(p1[1]+p2[1])/2

pts = [[0,0],[15,40],[30,0]]

x,y = [2],[2]

for i in range(1000000):
  r = random.randint(0,2)
  newP = midpt(pts[r],[x[-1],y[-1]])
  x.append(newP[0])
  y.append(newP[1])

plt.scatter(x, y, label= "stars", color= "orange", 
            marker= ".", s=30)
  

  
# function to show the plot
plt.show()
