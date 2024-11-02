import math


def Area(r,v):
    return 2*math.pi*pow(r,2)+ 2*v/r

def FindH(r,v):
      return v/(math.pi*pow(r,2))

def FindMinArea(V):
    minArea = 1000000
    for i in range(100000):
        r = (i+1)/10000
        
        A = Area(r,V)
        H = FindH(r,V)
        if minArea > A:
            minArea = A
            minH = H
            minR = r
            
    print("|\t %.2f" % minR, "\t|\t %.2f" %minH ,"\t|\t ",V , "\t|\t %.2f" %(minH/minR)," \t|\t %.2f\t|"  % minArea )

#TODO
V = 500
minArea = 100000
minH = 0
minR = 0
print("|\t Rad. \t|\t Hei. \t|\t Vol. \t|\t H/R \t|\t AREA \t| ")


FindMinArea(100)

FindMinArea(200)

FindMinArea(300)

FindMinArea(400)

FindMinArea(500)


"""
for i in range(10000):
    r = (i+1)/1000
        
    A = Area(r,V)
    H = FindH(r,V)
    
            
    print("|\t %.2f" % r, "\t|\t %.2f" %H ,"\t|\t ",V , "\t|\t %.2f" %(H/r)," \t|\t %.2f\t|"  % A )
"""