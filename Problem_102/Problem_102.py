# Project Euler Problem 102


# Adapted from geeks for geeks
def isIntersection(p1, q1, p2, q2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
    
    def onSegment(p, q, r):
        if (q[0] <= min(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= min(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        
        return False

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    # General Case
    if (o1 != o2 and o3 != o4): return True

    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)): return True

    # p1, q1 and q2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)): return True

    # p2, q2 and p1 are colinear and p1 lies on segment p2q2 
    if (o3 == 0 and onSegment(p2, p1, q2)): return True

    # p2, q2 and q1 are colinear and q1 lies on segment p2q2 
    if (o4 == 0 and onSegment(p2, q1, q2)): return True

    return False

# triangles = open('p102_triangles.txt', 'r').readlines()
# triangles = [l.split(',') for l in triangles]
# triangles = [map(int, t) for t in l for l in triangles]

p1 = (1,1)
q1 = (10,1)
p2 = (1,2)
q2 = (10,2)

print(isIntersection(p1,q1,p2,q1))
