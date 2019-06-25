import numpy as np


class particle:

    def __init__(self,position):

        self.position = position


    def set_Position(self,position):
        self.position = position

    def get_Position(self):
        return self.position

    def set_Pbest(self,Pbest):
        self.Pbest = Pbest

    def get_Pbest(self):
        return self.Pbest

    def set_Position_index(self,index,point):
       self.position.__setitem__(index,point)

    def set_Pbest_index(self,index,point):
        self.Pbest.__setitem__(index,point)

    def set_fitness(self,fitness):
        self.fitness = fitness

    def compare_positions(self,position_a,position_b):

        if 1/self.get_distance(position_b) > 1/self.get_distance(position_a):
            return True

        return False

    def calculate_fitness(self):

        self.fitness = 1/self.get_distance(self.position)
        self.set_fitness(self.fitness)

        return self.fitness


    def get_distance(self,points):

        self.distance = 0.0

        for r in range(0,len(points)):

            if r == len(points) -1:

                initx = points[r][0]
                inity = points[r][1]

                destx = points[0][0]
                desty = points[0][1]

            else:

                initx = points[r][0]
                inity = points[r][1]
                destx = points[r+1][0]
                desty = points[r+1][1]

            euclidean_distance = self.euclidean(destx,initx,desty,inity)
            self.distance = self.distance + euclidean_distance

        return self.distance

    def euclidean(self,x2,x1,y2,y1):

        distance = np.power(x2-x1,2) + np.power(y2-y1,2)
        e_distance = np.sqrt(distance)

        return e_distance



