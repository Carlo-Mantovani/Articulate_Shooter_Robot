from Point import Point

class Tri:   
    def __init__(self, vertices = [[]]):
        self.vertices = [[]]
    
        
    def getVertices(self):
        return self.vertices    

    def readTriObject(self):
        f = open("tri/sheep.tri")
        line = f.readline()
        i = 0
        while line:
            pointList = line.split()
            if len(pointList) == 10:
                
                vertex1 = Point(float(pointList[0]), float(pointList[1]), float(pointList[2]))
                vertex2 = Point(float(pointList[3]), float(pointList[4]), float(pointList[5]))
                vertex3 = Point(float(pointList[6]), float(pointList[7]), float(pointList[8]))
                color = pointList[9]
                self.vertices.append([vertex1, vertex2, vertex3, color])
                
                i = i + 1
            line = f.readline()
        