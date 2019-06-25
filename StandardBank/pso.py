import random
from Particle import particle

class PSO:

    noIterations = 2000

    def __init__(self, Particles):
        self.Particles = Particles #initializing the particles variable which stores paths

    def startPso(self):

        counter = 0
        #iterating until the number of iterations is reached
        while counter < self.noIterations:

            for r in range(0,len(self.Particles)):

                currentParticle = self.Particles[r]  #getting a particle from the list and assigning it to current particle
                self.Particles[r].calculate_fitness() #claculating the fitness function of each particle
                self.Particles[r].set_Pbest(currentParticle.get_Position()) #initializing the pbest of each particle as the current path

            self.gbest = self.calculate_gbest(self.Particles) #calulating the gbest of the particle

            for i in range(0,len(self.Particles)):
                new_position = self.update_position(self.Particles[i],self.gbest) #updatingn the position of the path using crossover as the velocity
                self.Particles[i].set_Position(new_position.get_Position()) #setting the newly updated position

            for r in range(0,len(self.Particles)):
                pbest = self.Particles[r].get_Pbest() #getting the pbest from each particle
                position = self.Particles[r].get_Position() #getting each particles positions
                #if statement to compare the pbest and position to see which one is better
                if self.Particles[r].compare_positions(pbest,position):
                    self.Particles[r].set_Pbest(position) #setting the pbest as position if the position is the better than pbest
                #if staatement to cmompare the gbest and position to which one is better
                if self.Particles[r].compare_positions(self.gbest.get_Position(),self.Particles[r].get_Pbest()):
                    self.gbest.set_Position(self.Particles[r].get_Pbest()) #setting the gbest as the pbest if the pbest is better than the gbest

            counter = counter +1 #incrementing the counter

        return self.gbest


    def calculate_gbest(self,particles):

        current_gbest = particles[0] #the initializing the first particle as the gbest

        #gbest to find the best particle out of all particles
        for r in range(0,len(particles)):
            #if statement to compare the fitness of each particle to find the best particle
            if particles[r].calculate_fitness() > current_gbest.calculate_fitness():

                current_gbest = particles[r] #assigning the best found particle to current gbest

        #returining gbest
        return current_gbest

    def update_position(self,pbest,gbest):

      size = len(pbest.get_Pbest()) -1 #getting the size of pbest
      index = random.randint(0,size) #getting  a random index in within the range 0 and size

      new_tour = [] #new_particle[]
      default_point = [-1,-1] #initializing the default as point with coordinates(-1,-1)

      #for loop to initialize the variable new tour with default point (-1,-1)

      for i in range(0,len(pbest.get_Pbest())):
          new_tour.append(default_point) #adding the point (-1,-1) to the point

      new_particle = particle(new_tour) #creating a particle which has (-1,-1) as its coordiantes initially (initializing a new particles)
      counter =0

      #for loop to extract the coordinates from the pbest and adding them in the new particle
      for i in range(index,len(pbest.get_Pbest())):
          if i > index:
             new_particle.set_Position_index(counter,pbest.get_Pbest()[i]) #setting the coordinates in pbest in the new particle
             counter = counter +1 #incrementing counter


      missing_points = [] #missing points to store the points that were not added from pbest

      #for loop to populate missing point with points from gbest
      for i in range(0,len(gbest.get_Position())):

          exists = 0 #control variable to determine whether to add the point in the missinglist varibale
          point = gbest.get_Position()[i] #getting the current point

          for r in range(0,len(new_particle.get_Position())):
              #if statement to set the control variable to 1 if the point already exists
              if point == new_particle.get_Position()[r]:
                  exists = 1

          #if exists is equals to 0 then add the point to the missing points list
          if exists == 0:
              missing_points.append(point)

      counter2 = 0

      #for loop to add the points from missing points list to the new particle.
      for i in range(0,len(new_particle.get_Position())):

          if new_particle.get_Position()[i] == default_point:
              new_particle.set_Position_index(i,missing_points[counter2])
              counter2 = counter2 + 1


      return new_particle