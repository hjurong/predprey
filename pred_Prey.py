import random
import time
import matplotlib.pyplot as plt
random.seed(100000)

## Island Class-----------------------------------------------------------------------------------
class Island (object):
    """Island
    a 3D grid where zero value indicates position not occupied.
    """
    ## Initialisation of an Island.
    def __init__(self, x,y,z, wolf_count=0, eagle_count=0,
                 rabbit_count=0, pigeon_count=0):
        ''' Initialize grid to all 0's, then place animals.
        '''
        # Making the 3D-grid and its dimensions as Island attributes.
        self.grid_size_x = x
        self.grid_size_y = y
        self.grid_size_z = z 
        self.grid_3D = []    
        # Construct the grid as a list of lists of lists;
        # first specify the z-dimension, 
        # then the y-dimension and finally the x-dimension.
        for k in range(z):                  
            self.grid_3D.append([])
            for j in range(y):
                self.grid_3D[k].append([0]*x)

        # Place animals onto the Island using the init_animals method.
        self.init_animals(wolf_count, eagle_count, rabbit_count, pigeon_count)

        # Add two attributes to Island for holding the data of the animals.
        # Dictionaries are used to make appending and extracting data simpler.
        self.life_dict = {"W":[], "E":[], "r":[], "p":[]}                          
        self.offspring_dict = {"W":[], "E":[], "r":[], "p":[]} 
        

    ## --------------------------------------------------------------------------------
    def size(self):
        ''' Return size of the island: three dimension.
        '''
        return self.grid_size_x,self.grid_size_y,self.grid_size_z         
    

    ## --------------------------------------------------------------------------------
    def __str__(self):
        ''' String representation for printing.
        (0,0,0) is at the lower left corner of the bottom layer.
        '''
        s = ""                                         # The 3D grid will be printed as a string.
        for k in range(self.grid_size_z-1,-1,-1):      # Print 3D grid as 2D layers.
            s+="z-level {}\n".format(k)                # Print the z-level of the current layer.
            for j in range(self.grid_size_y-1,-1,-1):  # Print the rows of the 2D layers.
                for i in range(self.grid_size_x):      # Each row has x columns
                    if not self.grid_3D[k][j][i]:
                        # print a '.' for an empty space
                        s+= "{:<2s}".format('.' + "  ")
                    else:
                        # print the name of the animal for occupied position
                        s+= "{:<2s}".format((str(self.grid_3D[k][j][i])) + "  ")
                s+="\n"                                # Start the next row in a new line.
            s+="\n"                                    # Separate every 2D-layer with a new line.
            
        return(s)
    

    ## --------------------------------------------------------------------------------
    def register(self,animal):
        ''' Register animal with island, i.e. put it at the
        animal's coordinates.
        '''
        x = animal.x
        y = animal.y
        z = animal.z
        self.grid_3D[z][y][x] = animal


    ## ------------------------------------------------------------------------------
    def remove(self,animal):
        ''' Remove animal from island by making the animal's position to be 0.
        '''
        x = animal.x
        y = animal.y
        z = animal.z
        self.grid_3D[z][y][x] = 0


    ## -----------------------------------------------------------------------------
    def animal(self,x,y,z):
        '''Return the animal at location (x,y,z).
        '''
        if 0 <= x < self.grid_size_x and 0 <= y < self.grid_size_y \
                                     and 0 <= z < self.grid_size_z:
            return self.grid_3D[z][y][x]
        else:
            return -1  # outside island boundary      


    ## -----------------------------------------------------------------------------
    def init_animals(self,wolf_count, eagle_count, 
                     rabbit_count, pigeon_count):
        ''' Place the initial animals on the island.
        '''
        start_time=time.time()
        if wolf_count + rabbit_count <= \
                   self.grid_size_x * self.grid_size_y and \
           wolf_count + rabbit_count + pigeon_count + eagle_count <= \
                   self.grid_size_x * self.grid_size_y * self.grid_size_z:
            count = 0
            loop_count = 0
        # The while-loop continues until  unoccupied positions equalling to
        # wolf_count, eagle_count are found.
        # If the dimensions of the Island are insufficient to hold all the animals,
        # break; and inform the user.
        # Same while loop for all four animals.
            while count < wolf_count:
                loop_count += 1
                # Wolves are restricted to layer_0.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = 0                                   
                if not self.animal(x,y,z):
                    new_wolf=Wolf(self,x,y,z)
                    count += 1
                    self.register(new_wolf)
                    if loop_count > self.grid_size_x * self.grid_size_y:
                        pass
                #print("Insufficient Island Dimensions")
                #break 
                
            count = 0
            loop_count = 0
            while count < rabbit_count:
                loop_count += 1
                # Rabbits are restricted to layer_0.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = 0
                if not self.animal(x,y,z):
                    new_rabbit=Rabbit(self,x,y,z)
                    count += 1
                    self.register(new_rabbit)
                    if loop_count > self.grid_size_x * self.grid_size_y:
                        pass
                #print("Insufficient Island Dimensions")
                #break 
            
            count = 0
            loop_count = 0
            while count < eagle_count:
                loop_count += 1
                # No position restrictions for eagles.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = random.randint(0,self.grid_size_z-1)
                if not self.animal(x,y,z):
                    new_eagle=Eagle(self,x,y,z)
                    count += 1
                    self.register(new_eagle)            
                    if loop_count > self.grid_size_x * self.grid_size_y * self.grid_size_z:
                #print("Insufficient Island Dimensions")
                #break
                        pass
        
            count = 0   
            loop_count = 0
            while count < pigeon_count:
                loop_count += 1
                # No position restrictions for pigeons.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = random.randint(0,self.grid_size_z-1)
                if not self.animal(x,y,z):
                    new_pigeon=Pigeon(self,x,y,z)
                    count += 1
                    self.register(new_pigeon)             
                    if loop_count > self.grid_size_x * self.grid_size_y * self.grid_size_z:
                #print("Insufficient Island Dimensions")
                #break
                        pass
            print(time.time() - start_time)

    ## -----------------------------------------------------------------------------
    def clear_all_moved_flags(self):
        ''' Animals have a moved flag to indicated they moved this turn.
        Clear that so they can move at the next clock tick.
        '''
        # Loop through every cell in the 3D grid list.
        for z in range(self.grid_size_z):
            for y in range(self.grid_size_y):
                for x in range(self.grid_size_x):
                    if self.grid_3D[z][y][x]:
                        self.grid_3D[z][y][x].clear_moved_flag()
    

    ## -----------------------------------------------------------------------------
    def count_animal(self, add_stat=False):
        ''' Count the number of a specified type of animal on the island,
        and the statistics of the animals can be appended
        to the appropriate lists if add_stat=True.'''
        wolf_count = 0 
        eagle_count = 0
        rabbit_count = 0
        pigeon_count = 0    
        # Loop through every position of the 3D_grid list. 
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                for z in range(self.grid_size_z):
                    animal = self.animal(x,y,z) 
                    # If there is an animal corresponding to the type looking for,
                    # add count.            
                    if animal and not add_stat:
                        if isinstance(animal,Wolf):
                            wolf_count+=1
                        if isinstance(animal,Eagle):
                            eagle_count+=1
                        if isinstance(animal,Rabbit):
                            rabbit_count+=1
                        if isinstance(animal,Pigeon):
                            pigeon_count+=1
                    # If the add_stat condition is true,
                    # append the animal's data (i.e., life time and number of offspring)
                    # to the Island attributes.
                    # This will be used at the end of the simulation to
                    # gather the statistics of animals that are still alive.
                    if animal and add_stat:
                        self.life_dict[animal.name].append(animal.life_time)
                        self.offspring_dict[animal.name].append(animal.offspring)
        if not add_stat:
            return wolf_count,eagle_count,rabbit_count,pigeon_count


    ## -----------------------------------------------------------------------------
    def cal_stat(self, type):    
        """ Calculates all the required statistics for a type of animal and
        return the result as a tuple."""

        # Get the data (i.e., the life_time and offspring lists 
        # of a subclass of Animal.) from the Island attributes.
        # Sort those lists for extracting maximum and minimum and median calculations.
        offspring_list = self.offspring_dict[type]
        offspring_list.sort()                     
        life_list = self.life_dict[type]
        life_list.sort()
        life_num = len(life_list)

        # If a type of animal is initialised to be zero (i.e., none in the simulation),
        # IndexError will arise when trying to calculated its statistics.
        # This is not desirable for testing.
        # Use try-except to prevent the program from crashing if this occurs.
        try:
            offspring_min, offspring_max = offspring_list[0], offspring_list[-1]
            life_min, life_max = life_list[0], life_list[-1]

            # Calculate the average for the number of offspring and life_time.
            offspring_avg = sum(offspring_list)/len(offspring_list)
            life_avg = sum(life_list)/len(life_list)

        # Calculate the median for the number of offspring and life_time.
        # Need to consider two cases:
        # 1. If the length of the list is an odd number,
        #    the median is the middle number of that list
        #    (Python indexing starts at 0).
        # 2. If the length of the list is an even number,
        #    the median is the average between the two middle numbers.
            if len(offspring_list)%2==1:
                offspring_med = offspring_list[int((len(offspring_list)-1)/2)]
            else:
                offspring_med =(offspring_list[int(len(offspring_list)/2-1)] +
                                offspring_list[int(len(offspring_list)/2)])/2
        
            if len(life_list)%2==1:
                life_med = life_list[int((len(life_list)-1)/2)]
            else:
                life_med =(life_list[int(len(life_list)/2-1)] +
                           life_list[int(len(life_list)/2)])/2 

        # If a type of animal is not initialised, make all its statistics 0. 
        except IndexError:
            life_num = "\nThis type of animal has not been initialised."
            life_min, life_max, life_avg, life_med = 0, 0 ,0 ,0
            offspring_min, offspring_max, offspring_avg, offspring_med = 0, 0, 0, 0

        # Return the result as a tuple.               
        return life_num, life_max, life_min, life_avg, life_med,\
               offspring_min, offspring_max, offspring_avg, offspring_med


## Animal Class---------------------------------------------------------------------------------------------------
class Animal (object):
    def __init__(self, island, x=0, y=0, z=0, s="A"):
        """ Initialize the animals as a subclass of Island;
        and their positions and names.
        """
        # Storing the information as class attributes.
        self.island = island
        self.name = s
        self.x = x
        self.y = y
        self.z = z
        self.moved=False


    ## -----------------------------------------------------------------------------
    def __str__(self):
        """ Prints the name of the animal.
        """
        return self.name
    

    ## -----------------------------------------------------------------------------
    def position(self):
        ''' Return coordinates of the animal's current position.
        '''
        return self.x, self.y, self.z


    ## -----------------------------------------------------------------------------
    def check_grid(self,type_looking_for=int):
        ''' Look randomly at all possible locations from the animal's location
        and return a location that is presently occupied by an object
        of the specified type. Return 0 if no such location exists
        '''
        # Generate a list of neighbour offset tuples.
        # Animals can only search positions that are in this list.
        #start = time.time()
        offset = [] 
        for k in range(-1,2,1):
            for j in range(-1,2,1):
                for i in range(-1,2,1):
                    offset_tup = (i,j,k)
                    # Do not include the zero offset.
                    if offset_tup != (0,0,0):
                        offset.append(offset_tup)
        # An animal can inspect a maximum of 26 positions.
        assert len(offset)==26, "Error in offset list."
        result = 0
        # Randomly look through positions with offset to current position included in offset
        # by shuffling the list.
        # Every time this loop is entered, the offset list would have 
        # a different order.
        random.shuffle(offset)
        for index in range(len(offset)):         
            # Eagle or pigeon have no restrictions on their positions.
            if isinstance(self, Eagle) or isinstance(self, Pigeon):
                x = self.x + offset[index][0]  # neighbouring x,y,z coordinates
                y = self.y + offset[index][1]
                z = self.z + offset[index][2]
                # If the position is outside the 3D grid, choose another one.
                if not 0 <= x < self.island.grid_size_x or \
                   not 0 <= y < self.island.grid_size_y or \
                   not 0 <= z < self.island.grid_size_z:
                    continue
                # If a position is found, return its coordinates and exit loop.
                elif type(self.island.animal(x,y,z))==type_looking_for:
                    result=(x,y,z)
                    break

            # Wolf and rabbit are restricted to layer_0.
            else:
                x = self.x + offset[index][0]  # neighbouring x,y,z coordinates
                y = self.y + offset[index][1]
                z = self.z
                # If position is outside Island, continue loop.
                # If a position is found, exit loop and return its coordinates.
                if not 0 <= x < self.island.grid_size_x or \
                   not 0 <= y < self.island.grid_size_y or \
                   not 0 <= z < self.island.grid_size_z:
                    continue
                elif type(self.island.animal(x,y,z))==type_looking_for:
                    result=(x,y,z)         
                    break
        # If an object of the specified type cannot be found, result=0.
        #print ("check_grid took {}s".format(time.time()-start))
        return result


    ## -----------------------------------------------------------------------------
    def move(self):
        ''' Move to an open, neighbouring position
        '''
        # An animal is only allowed to move once per clock tick.
        if not self.moved:
            # Look for an empty cell, i.e., cell occupied by 0.
            location = self.check_grid(int)
            if location:
                #print('Move, {}, from {},{},{} to {},{},{}'.format(
                #       self.name,self.x,self.y,self.z,
                #       location[0],location[1],location[2]))         #debug
                
                self.island.remove(self)   # Remove instance from current spot.
                self.x = location[0]       # New x,y,z coordinates.
                self.y = location[1]
                self.z = location[2]
                self.island.register(self) # Register instance at new coordinates.
                self.moved=True            # Change the moved flag.


    ## -----------------------------------------------------------------------------
    def clear_moved_flag(self):
        """ Change the animal's moved attribute to False.
        """
        self.moved=False


    ## -----------------------------------------------------------------------------
    def breed(self):
        ''' Breed a new Animal at an empty neighbouring location.
        If no empty position available, wait.
        '''
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                # Register the new animal at the empty position.
                # Increase the instance's offspring count.
                # Reset breed_clock.
                self.breed_clock = self.breed_time            
                the_class = self.__class__
                new_animal = the_class(
                           self.island,x=location[0],y=location[1],z=location[2])
                self.island.register(new_animal)    
                self.offspring += 1

                #print('{} Breeding {},{},{}'.format(
                #       str(self.name),self.x,self.y,self.z)) # debug


## Prey Class-----------------------------------------------------------------------------------
class Prey(Animal):
    def __init__(self, island, x=0,y=0,z=0,s="Prey"):
        """Initialise the Prey class as a subclass of Animal.
        Prey will inherit all methods from its parent class.
        """
        Animal.__init__(self,island,x,y,z,s)
           

    ## -----------------------------------------------------------------------------
    def clock_tick(self):
        '''Prey updates its local breed clock and life_time
        '''
        self.breed_clock -= 1
        self.life_time += 1
        #print('Tick Prey {},{},{} breed:{} life:{}'.format(
        #       self.x,self.y,self.z,self.breed_clock,self.life_time)) # debug


## Predator Class-----------------------------------------------------------------------------------
class Predator(Animal):
    def __init__(self, island, x=0,y=0,z=0,s="Pred"):
        """Initialise the Predator class as a subclass of Animal.
        """        
        Animal.__init__(self,island,x,y,z,s)


    ## -----------------------------------------------------------------------------
    def clock_tick(self):
        ''' Predator updates breeding, starving and life_time
        '''
        self.breed_clock -= 1
        self.starve_clock -= 1
        self.life_time += 1
        #print('Tick Predator {},{},{} breed:{} starve: {} life:{}'.format(
        #       self.x,self.y,self.z,
        #       self.breed_clock,self.starve_clock,self.life_time)) # Debug
        
        # If the predator's starve clock is 0, remove it from Island, 
        # register its data to Island's offspring_dict and life_dict.
        if self.starve_clock <= 0:
            self.island.remove(self)
            self.island.life_dict[self.name].append(self.life_time)
            self.island.offspring_dict[self.name].append(self.offspring)            
            #print('Death, {} at {},{},{}, life={}'.format(
            #       self.name,self.x,self.y,self.z,self.life_time)) # Debug
            
            
     ## -----------------------------------------------------------------------------
    def eat(self, prey_type):
        ''' Predator looks at the offset locations for Prey.
        If found, it moves to that location and updates its starve clock.
        The Prey is removed.
        Register the data of the eaten prey to offspring_dict and life_dict.
        '''
        # Eating involves moving; it can be performed once per clock tick.
        if not self.moved:
            location = self.check_grid(prey_type)
            if location:
                #print('Eating: {} at {},{},{} {} at {},{},{}'.format(
                #       str(self.name),self.x,self.y,self.z,
                #       self.island.animal(location[0],location[1],location[2]),
                #       location[0],location[1],location[2])) # debug
                
                # Add the statistics of the Prey animal to appropriate Island attributes.
                # Life-time:
                self.island.life_dict[str(self.island.animal(
                        location[0],location[1],location[2]))].append(
                            self.island.animal(
                                location[0],location[1],location[2]).life_time)                 
                # Number of offspring:
                self.island.offspring_dict[str(self.island.animal(
                        location[0],location[1],location[2]))].append(
                            self.island.animal(
                                location[0],location[1],location[2]).offspring) 

                # Remove the eaten animal and move the Predator instance to its position.
                self.island.remove(self.island.animal(location[0],location[1],location[2]))
                self.island.remove(self)
                self.x=location[0]
                self.y=location[1]
                self.z=location[2]
                self.island.register(self)
                self.starve_clock=self.starve_time
                self.moved=True   

        
## Eagle class---------------------------------------------------------------------------------------------------
class Eagle (Predator):
    def __init__(self, island, x=0, y=0, z=0, s="E"):
        """Initialise the Eagle class as a subclass of Predator.
        Methods of the Predator class will be inherited.
        Add life_time, offspring breed_clock and starve_clock 
        attributes to every instance.
        """          
        Predator.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.starve_clock = self.starve_time
        self.life_time = 0
        self.offspring = 0
        

    ## --------------------------------------------------------------------------------
    def hunt(self):
        ''' Eagles can eat pigeons and rabbits.
        '''
        self.eat(prey_type = Pigeon) or self.eat(prey_type = Rabbit)


## Wolf class------------------------------------------------------------------------------------------------
class Wolf (Predator):
    def __init__(self, island, x=0, y=0, z=0, s="W"):
        """Initialise the Wolf class as a subclass of Predator.
        Wolf inherits methods from Predator.
        Add life_time, offspring, breed_clock and starve_clock 
        attributes to every instance.
        """         
        Predator.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.starve_clock = self.starve_time
        self.life_time = 0
        self.offspring = 0
        

    ## ------------------------------------------------------------------------------
    def hunt(self):
        ''' Wolves can eat rabbits, eagles and pigeons.
        '''
        self.eat(prey_type = Rabbit) or self.eat(prey_type = Pigeon) \
        or self.eat(prey_type = Eagle)
    

## Rabbit class--------------------------------------------------------------------------------------------
class Rabbit (Prey):
    def __init__(self, island, x=0, y=0, z=0, s="r"):
        """Initialise the Rabbit class as a subclass of Prey.
        Rabbit inherits from Prey.
        Add life_time, offspring breed_clock attributes to every instance.
        """         
        Prey.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.life_time = 0
        self.offspring = 0
    
        
## Pigeon class--------------------------------------------------------------------------------------------
class Pigeon (Prey):
    def __init__(self, island, x=0, y=0, z=0, s="p"):
        """Initialise the Rabbit class as a subclass of Prey.
        Pigeon inherits from Prey.
        Add life_time, offspring breed_clock attributes to every instance.
        """          
        Prey.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.life_time = 0
        self.offspring = 0
    

## Main Program for simulation------------------------------------------------------------------------------------------------
def main(eagle_breed_time=10, eagle_starve_time=4, initial_eagles=12,
         wolf_breed_time=12,  wolf_starve_time=3, initial_wolves=7,
         pigeon_breed_time=3, initial_pigeons=300,
         rabbit_breed_time=2, initial_rabbits=350,
         x=20, y=20, z=3, ticks=200, stop=True):
    ''' Main simulation. Sets defaults, runs event loop, plots data at the end.
    '''
    # Initialization of class attributes.
    Eagle.breed_time = eagle_breed_time
    Eagle.starve_time = eagle_starve_time  
    Wolf.breed_time = wolf_breed_time
    Wolf.starve_time = wolf_starve_time  
    Pigeon.breed_time = pigeon_breed_time
    Rabbit.breed_time = rabbit_breed_time
    
    # For graphing
    pigeon_list=[]
    rabbit_list=[]
    eagle_list=[]
    wolf_list=[]
    
    # Initialise an Island.
    land = Island(x,y,z,initial_wolves,initial_eagles,
                        initial_rabbits, initial_pigeons)
    island_size = land.size()
    #print(land)

    ## Simulation Loop-----------------------------------------------------------------------------
    # Simulate using a for loop. 
    # Every clock tick, look at every position of the Island,
    # do tasks if there is an animal there.
    # Every time entering the for-loop, clear the moved flags of all animals.
    # If one of the populations become zero, exit the loop.
    start = time.time()
    for i in range(ticks):
        #start = time.time() # To determine the efficiency of the program
        land.clear_all_moved_flags()
        #print(land) # debug
        for x in range(island_size[0]):
            for y in range(island_size[1]):
                for z in range(island_size[2]):
                    animal = land.animal(x,y,z)
                    if animal and not animal.moved:
                        if isinstance(animal,Predator):
                            animal.hunt()
                        animal.move()
                        animal.breed()
                        animal.clock_tick()
        
        # Record population data for plotting.
        animal_count_tup = land.count_animal()
        rabbit_count = animal_count_tup[2]
        pigeon_count = animal_count_tup[3]
        wolf_count = animal_count_tup[0]
        eagle_count = animal_count_tup[1]
        pigeon_list.append(pigeon_count)
        rabbit_list.append(rabbit_count)
        eagle_list.append(eagle_count)
        wolf_list.append(wolf_count)


        if stop and (rabbit_count == 0 or pigeon_count == 0 or eagle_count==0):
            print('Lost the Prey population. Quiting.')
            break
        if stop and (wolf_count == 0 or eagle_count == 0):
            print('Lost the Predator population. Quitting.')
            break
        #print(land)
        
        # Print out every 10th cycle, see what's going on.
        # Print the island, hold at the end of each cycle to get a look.
        if not i%1000 and i!=0:
            print("ticks: {:>11}".format(i))
            print("pigeon_count: {:>4} \nrabbit_count: {:>4} "
                  "\nwolf_count: {:>6} \neagle_count {:>6}\n".format(
                   pigeon_count, rabbit_count, wolf_count, eagle_count))
        #print('*'*20)
        #print(land)
        #ans = input("Return to continue")
    print("tick {} took {}s".format(i,time.time()-start))

    ## Statistics analysis and printing--------------------------------------------------------
    # Add the data of the animals that are still alive to appropriate Island attributes.
    # Loop through every animal and print associated results.
    land.count_animal(add_stat=True)
    for elem in []:#["W","E","r","p"]:
        stat_list = land.cal_stat(type=elem)
        print("\nSimulation statistics for {}".format(elem))
        print("Number of {} {:<25} {}".format(
               elem,"lived during simulation:", stat_list[0]))
        print("{:<37} {:<5}".format("Max life_time:",stat_list[1]))
        print("{:<37} {:<5}".format("Min life_time:",stat_list[2]))
        print("{:<37} {:<5.3f}".format("Average life_time:",stat_list[3]))
        print("{:<37} {:<6.3f}".format("Median life_time:",stat_list[4]))
        print("{:<37} {:<5}".format("Min number of offspring:",stat_list[5]))
        print("{:<37} {:<5}".format("Max number of offspring:",stat_list[6]))
        print("{:<37} {:<5.3f}".format("Average number of offspring:",stat_list[7]))
        print("{:<37} {:<6.3f}\n".format("Median number of offspring:",stat_list[8]))

    #print("\nlife", land.life_dict,"\noffspring",land.offspring_dict)  # Debug
    #print(land)
    
    #-----------------------------------------------------------------------------    
    ## Plotting population fluctuation over the simulation.
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1)
    ax.plot(pigeon_list,"y",label="Pigeon",linewidth=2)
    ax.plot(rabbit_list,"r",label="Rabbit",linewidth=2)
    ax.plot(eagle_list,"g",label="Eagle",linewidth=2)
    ax.plot(wolf_list,"b",label="Wolf",linewidth=2)
    ax.legend(bbox_to_anchor=(0.75, 0.7), loc=3, borderaxespad=0.)
    ax.set_ylabel(r"$Number$ $of$ $Alive$ $Animals$", fontsize = 15)
    ax.set_xlabel(r"$Clock$ $Tick$", fontsize=15)
    ax.set_title(r"$Population$ $Fluctuation$", fontsize=20)
    #plt.show()

main()