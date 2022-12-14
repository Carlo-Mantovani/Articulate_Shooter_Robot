from Point import Point, prodVetorial

class TriModel:   
    def __init__(self, color) -> None:
        self.vertices = [[]]
        self.positions = []
        self.min = Point(0,0,0)
        self.max = Point(0,0,0)
        self.normal = Point(0,0,0)
        self.color = color
        
    def getVertices(self):
        return self.vertices    

    def readTriObject(self, file):
        f = open(file)
        line = f.readline()
        i = 0
        while line:
            pointList = line.split()
            if len(pointList) == 10:
                
                vertex1 = Point(float(pointList[0]), float(pointList[1]), float(pointList[2]))
                vertex2 = Point(float(pointList[3]), float(pointList[4]), float(pointList[5]))
                vertex3 = Point(float(pointList[6]), float(pointList[7]), float(pointList[8]))
                
                normal = normalCalc(vertex1,vertex2,vertex3)
                self.vertices.append([vertex1, vertex2, vertex3, normal])

                i = i + 1

                for j in range (3):
                    if (self.vertices[i][j].x < self.min.x):
                        self.min.x = self.vertices[i][j].x
                    if (self.vertices[i][j].y < self.min.y):
                        self.min.y = self.vertices[i][j].y
                    if (self.vertices[i][j].z < self.min.z): 
                        self.min.z = self.vertices[i][j].z
                    if (self.vertices[i][j].x > self.max.x):
                        self.max.x = self.vertices[i][j].x
                    if (self.vertices[i][j].y > self.max.y):
                        self.max.y = self.vertices[i][j].y
                    if (self.vertices[i][j].z > self.max.z):
                        self.max.z = self.vertices[i][j].z

            line = f.readline()

def normalCalc(p1, p2, p3):
    vet1 = p2 + (p1*-1)
    vet2 = p3 + (p2*-1)
    vet = prodVetorial(vet1, vet2)
    return vet      