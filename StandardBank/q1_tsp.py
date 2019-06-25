# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 11:29:11 2017

@author: A210032
"""

""" 
Interview coding question

Standard Bank Data Services, Data Science team.

Instructions
    1: Implement the 3 functions below as described in their comments.
    2: Feel free to define any other functions that you like to make the code
       easier to read, but do not import any other packages.
    3: The function shortest_round_trip requires a solution to the well known 
       travelling salesperson problem which is known to be np-hard.  Implement
       any solution that produces an approximation to the shortest path or 
       an exhaustive search.
    4: Email your solution to james.taylor@standardbank.co.za
    5: Feel free to ask clarifying questions, but not too many...
    6: In your next interview, we will run this file and discuss the solutions
       implemented and the way that the code is written.
    7: Bonus
        Implement the solution using a graph data structure.
        To show the robustness of you solution show how well your solution work
        on the Existing points found  in the Points List however also generate 
        random a larger graph
        7.1 Implement Dijkstra Algorithm to find the shortest path 


"""

# the required imports.  Don't add any others
import numpy as np
import scipy as sp
from pso import PSO
import matplotlib.pyplot as plt
from random import randint
from random import shuffle
from Particle import particle

# the data points on the map.  Each pair is an x-y coordinate.  The distance 
# between any two points is the Euclidian distance, i.e. 
# d = sqrt((x2-x1)**2+(y2-y1)**2)
# one can travel from any point to any other
points = [[22,32],
        [40,14],
        [99,75],
        [35,20],
        [89,97],
        [83,90],
        [66,81],
        [75,97],
        [88,19],
        [100,8],
        [26,4],
        [54,57],
        [75,75],
        [15,10],
        [52,95],
        [88,26],
        [91,90],
        [44,83],
        [85,11],
        [9,92],
        [58,40],
        [86,55],
        [63,47],
        [94,59],
        [90,81],
        [28,64],
        [71,54],
        [28,35],
        [67,29],
        [75,77]]


0

def get_nearest_point(x, y):
    """
    Returns the index of the point on the map that is closest to the provided
    point.  The provided point may not coincide with any points on the map.
    
    Returns:
        an int giving the index of the nearest point
    """
    
    # place implementation here.

    distance_list = [] #list to store the nearest point

    for r in range(0, len(points)):
        x2 = points[r][0] #getting the x value
        y2 = points[r][1] #getting the y value

        distance = np.power(x2 - x, 2) + np.power(y2 - y, 2) #calculating the euclidean distance
        distance = np.sqrt(distance)
        distance_list.append(distance) #adding the distance to the list

    min_distance = min(distance_list) #getting the nearest distance
    index = distance_list.index(min_distance) #index of the nearest point

    return index


def get_nearest_points(x, y, n_points):
    """ 
    Given a point (x, y) returns a list of the n_points that are closest to it.
    """
    
    # place implementation here

    distance_list = [] #list to store the distances
    nearest_points = [] #list to strtire the nearest points
    points_copy = points.copy() #copy of the points variable

    for i in range(0,len(points)):

        x2  = points[i][0] #getting x value
        y2 = points[i][1] #getting y value

        distance = np.power(x2-x,2) + np.power(y2-y,2) #calculating the eculidean distance
        distance = np.sqrt(distance)
        distance_list.append(distance) #adding the distance to the distance list

    for r in range(0,n_points):

        min_distance = min(distance_list) #getting the minimum distgance
        index = distance_list.index(min_distance) #getting the index of the nearest disatcne
        nearest_point = points_copy[index] #getting the nearest point
        nearest_points.append(nearest_point) #adding the nearest point in the nearest points list


        distance_list.__delitem__(index) #deleting the current nearest distance to get the nearest distancne in the next loop
        points_copy.__delitem__(index) #deleting the current point in the points list to gte the next nearest point

    return nearest_points

def get_farthest_points(x,y, n_poits):
    """
    Given a point (x, y) returns a list of the n_points that are farthest to it.
    """
    points_copy = points.copy()
    farthest_points = []
    distance_list = []
    #for loop to add all the distances calculated from the point x,y to the points in the list
    for r in range(0,len(points)):

        x2 = points[r][0] #getting the x value
        y2 = points[r][1] #getting the y value

        distance = np.power(x2-x,2) + np.power(y2-y,2) #calculating the euclidean distance
        distance = np.sqrt(distance)
        distance_list.append(distance) #adding the distances in the list

    for i in range(0,n_poits):

        max_distance = max(distance_list) #getting the maximum distance in list
        index = distance_list.index(max_distance) #getting the index of the least distance
        farthest_point = points_copy[index] #getting the furthest point from the point list
        farthest_points.append(farthest_point) #adding the furthest point in the list that stores the furthest point

        distance_list.__delitem__(index) #deleting the previous furthest point form the distance list to find the new furthest distance
        points_copy.__delitem__(index) #deleting the previous furthest poit  from the point list to find the new furthest point



    return farthest_points

def generate_random_points(num_points,limit_coord=100 ):
    """
    This function returns a random list of points
    returns:
        a list of points on a 2D plane
    """
    return [ [randint(0, limit_coord),randint(0, limit_coord)] for i in range(num_points)] #returning a list of random distance
    
def shortest_round_trip():
    """ Returns a list of indices that should be visited to start at the point
    at index 0 and end at the same point while visiting each other point at 
    least once.
    """
    # replace this implementation
    particles_list = []
    shortest_path = []

    for i in range(0, 20):
        shuffle(points) #partitioning the points list
        p = particle(points) #instatiating the Particle object
        particles_list.append(p) #adding the points in the particle list

    min = 1000 #initializing the current mininmum disstance
    bit = 0 #bit (integer) to be used as a variable to find the optimal solution(path)

    #if statement to fidn the new best solution(path)

    for i in range(0,10):

      pso = PSO(particles_list)  # instatiating the PSO object
      gbest = pso.startPso()  # statring the PSO algorithm

      if min >= gbest.get_distance(gbest.get_Position()):
         min = gbest.get_distance(gbest.get_Position()) #assigning the new and best solution or path to the min variable
         shortest_path = gbest.get_Position() #assising the new  and best solution or path to the shortest_position variable
         print(str(min))
         print(shortest_path)


    optimal_particle = [] #list to store the indices of the shortest path

    for r in range(0,len(shortest_path)):
        p = shortest_path[r]   #assising the current point in the shortest path to p

        for i in range(0,len(points)):
            #if statement to store the index in the optimal_particle list
            if p == points[i]:
                optimal_particle.append(i)


    optimal_particle.append(optimal_particle[0]) #adding the first point as the last point in the list

    return optimal_particle

    
if __name__ == "__main__":
    print("Nearest point: \n\n")
    plt.figure("Nearest point")    
    (x, y) = (50,50)    
    plt.plot(x,y,'xb')
    for point in points:
        plt.plot(point[0], point[1],'k.')
    nearest = get_nearest_point(x, y)
    plt.plot(points[nearest][0],points[nearest][1],'or')
    
    
    print("Nearest points: \n\n")
    plt.figure("Nearest points")    
    (x, y) = (50,50)    
    plt.plot(x,y,'xb')
    for point in points:
        plt.plot(point[0], point[1],'k.')
    nearest_list = get_nearest_points(x, y, 3)

    for nearest in range(0, len(nearest_list)):
        plt.plot(nearest_list[nearest][0], nearest_list[nearest][1], 'or')

    print("Farthest points: \n\n")
    plt.figure("Farthest points")    
    (x, y) = (50,50)    
    plt.plot(x,y,'xb')
    for point in points:
        plt.plot(point[0], point[1],'k.')
    farthest_list = get_farthest_points(x, y, 3)

    for fearthest in range(0, len(farthest_list)):
        plt.plot(farthest_list[fearthest][0], farthest_list[fearthest][1], 'or')
    
    
    print("Shortest trip: \n\n")
    plt.figure("Shortest trip")  
    trip = shortest_round_trip()

    for point in points:
        plt.plot(point[0], point[1],'k.')    

    dist = 0.0

    for i in range(len(trip)-1):
        x1 = points[trip[i]][0]
        y1 = points[trip[i]][1]
        x2 = points[trip[i+1]][0]
        y2 = points[trip[i+1]][1]
        dist += np.sqrt((x2-x1)**2 + (y2-y1)**2)
        plt.plot([x1, x2], [y1, y2],'r')
        
    
    print("distance of naive trip: 1653.39776561")
    print("distance of this trip: " + str(dist))
    ranp = generate_random_points(10)
    print("Random points",generate_random_points(10) )
    for point in ranp:
        plt.plot(point[0], point[1],'y.')
    
        


    plt.show()
