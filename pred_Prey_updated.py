import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
random.seed(100000)

##--------------------------------------------------------------------------
## Island Class-----------------------------------------------------------------------------------
class Island (object):
    """Island
    a 3D grid where zero value indicates position not occupied.
    """
    ## Initialisation of an Island.
    def __init__(self, x,y,z, wolf_count=0, eagle_count=0,
                 rabbit_count=0, pigeon_count=0, grass_count=0, fruit_count=0):
        ''' Initialize grid to all 0's, then fill with animals.
        '''
        # Making the 3D-grid and its dimensions as Island attributes.
        # Construct the grid as a list of lists of lists;
        # first specify the z-dimension,
        # then the y-dimension and finally the x-dimension.
        self.grid_size_x = x
        self.grid_size_y = y
        self.grid_size_z = z 
        self.grid_3D = [[[0 for i in range(x)] for j in range(y)] for k in range(z)]

        # Place animals onto the Island using the init_animals method.
        self.init_envir(wolf_count, eagle_count, rabbit_count, pigeon_count,
                        grass_count, fruit_count)
        self.wolf_count, self.eagle_count = wolf_count, eagle_count
        self.rabbit_count, self.pigeon_count = rabbit_count, pigeon_count

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
            s+="z-level  {}\n".format(k)               # Print the z-level of the current layer.
            # Add a horizontal row to indicate the x-axis.            
            for n in range(self.grid_size_x): s+="{:<2s}".format(str(n)+"  ")
            s+="\n" # Build the 2D-levels in a new line. 
            for j in range(self.grid_size_y-1,-1,-1):  # Print the rows of the 2D layers.
                for i in range(self.grid_size_x+1):    # Each row has x columns
                    # Add a vertical column to indicate the y-axis level.
                    if i==self.grid_size_x: s+= "{:<2s}".format(str(j)+" ") 
                    else:
                        # print a '.' for an empty space.
                        # print the name of the animal for occupied position.
                        if not self.grid_3D[k][j][i]: s+= "{:<2s}".format('.' + "  ")
                        else: s+= "{:<2s}".format((str(self.grid_3D[k][j][i])) + "  ")
                s+="\n"                                # Start the next row in a new line.
            s+="\n"                                    # Separate every 2D-layer with a new line.
        return(s)
    

    ## --------------------------------------------------------------------------------
    def register(self,obj):
        ''' Register animal or plant with island, i.e. put it at the
        animal/plant's coordinates.
        '''
        x = obj.x
        y = obj.y
        z = obj.z
        self.grid_3D[z][y][x] = obj


    ## ------------------------------------------------------------------------------
    def remove(self,obj):
        ''' Remove animal or plant from island by making the animal's 
        position to be 0.
        '''
        x = obj.x
        y = obj.y
        z = obj.z
        self.grid_3D[z][y][x] = 0


    ## -----------------------------------------------------------------------------
    def occupant(self,x,y,z):
        '''Return the animal at location (x,y,z).
        '''
        if 0 <= x < self.grid_size_x and 0 <= y < self.grid_size_y \
                                     and 0 <= z < self.grid_size_z:
            return self.grid_3D[z][y][x]
        else:
            return -1  # outside island boundary      


    ## -----------------------------------------------------------------------------
    def init_envir(self,wolf_count, eagle_count, rabbit_count, pigeon_count,
                       grass_count, fruit_count):
        ''' Place the initial animals on the island.
        '''
        #start_time = time.time()
        # The while-loop continues until  unoccupied positions equalling to
        # wolf_count, eagle_count are found.
        # If the dimensions of the Island are insufficient to hold all the animals,
        # do not enter the loop; and inform the user.
        # Same while loop for all four animals.
        if wolf_count + rabbit_count + grass_count <= \
                   self.grid_size_x * self.grid_size_y and \
           wolf_count + rabbit_count + pigeon_count + eagle_count \
                      +  grass_count + fruit_count <= \
                   self.grid_size_x * self.grid_size_y * self.grid_size_z:
            #start_time=time.time()
        # The while-loop continues until  unoccupied positions equalling to
        # wolf_count, eagle_count are found.
        # Same while loop for all four animals.
        # The while-loop continues until  unoccupied positions equalling to
        # wolf_count, eagle_count are found.
            loc_set = set() # Used to avoid repeats.
            count = 0
            while count < wolf_count:
                # Wolves are restricted to layer_0.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = 0                                   
                if (x,y,z) not in loc_set:
                    new_wolf=Wolf(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_wolf)
          
            count = 0
            while count < rabbit_count:
                # Rabbits are restricted to layer_0.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = 0
                if (x,y,z) not in loc_set:
                    new_rabbit=Rabbit(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_rabbit)

            count = 0
            while count < eagle_count:
                # No position restrictions for eagles.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = random.randint(0,self.grid_size_z-1)
                if (x,y,z) not in loc_set:
                    new_eagle=Eagle(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_eagle)

            count = 0   
            while count < pigeon_count:
                # No position restrictions for pigeons.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = random.randint(0,self.grid_size_z-1)
                if not self.occupant(x,y,z):
                    new_pigeon=Pigeon(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_pigeon)
            
            count = 0
            while count < grass_count:
                # Grass are restricted to layer_0.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = 0                                   
                if (x,y,z) not in loc_set:
                    new_grass=Grass(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_grass)

            count = 0
            while count < fruit_count:
                # Fruits are restricted to layer_0 and 1.
                x = random.randint(0,self.grid_size_x-1)
                y = random.randint(0,self.grid_size_y-1)
                z = random.randint(0,1)                                   
                if (x,y,z) not in loc_set:
                    new_fruit=Fruit(self,x,y,z)
                    loc_set.add((x,y,z))
                    count += 1
                    self.register(new_fruit)
            #print("init_animal took {}s".format(time.time()-start_time))           
        else: print("Insufficient Island Dimensions")


    ## -----------------------------------------------------------------------------
    def clear_all_moved_flags(self):
        ''' Animals have a moved flag to indicated they moved this turn.
        Clear that so they can move at the next clock tick.
        '''
        # Loop through every cell in the 3D grid list.
        for z in range(self.grid_size_z):
            for y in range(self.grid_size_y):
                for x in range(self.grid_size_x):
                    if isinstance(self.grid_3D[z][y][x], Animal): 
                        self.grid_3D[z][y][x].clear_moved_flag()
                        
                        
    ##------------------------------------------------------------------------
    def get_locations(self):
        scatter_dict = {"W":[[],[],[],[],[]],"E":[[],[],[],[],[]],
                        "p":[[],[],[],[],[]],"r":[[],[],[],[],[]],
                        "g":[[],[],[],[],[]],"f":[[],[],[],[],[]]}
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                for z in range(self.grid_size_z):
                    instance = self.occupant(x,y,z)        
                    # Add the location statistics to a dictionary for animation.
                    # The dictionary is initialised such that the x,y,z locations
                    # can be added to the dictionary, as well as the life-time
                    # and number of offspring.
                    if isinstance(instance, Animal):
                        scatter_dict[instance.name][0].append(instance.x)
                        scatter_dict[instance.name][1].append(instance.y)
                        scatter_dict[instance.name][2].append(instance.z)
                        scatter_dict[instance.name][3].append(instance.life_time)
                        scatter_dict[instance.name][4].append(instance.offspring)
                    elif isinstance(instance, Plant):
                        scatter_dict[instance.name][0].append(instance.x)
                        scatter_dict[instance.name][1].append(instance.y)
                        scatter_dict[instance.name][2].append(instance.z)
                        scatter_dict[instance.name][3].append(instance.life_time)
                        scatter_dict[instance.name][4].append(instance.eaten)
        return scatter_dict
        
        
    ## -----------------------------------------------------------------------------
    def count_animal(self, add_stat=False):
        ''' Count the number of a specified type of animal on the island,
        and the statistics of the animals can be appended
        to the appropriate lists if add_stat=True.'''
        wolf_count, eagle_count, rabbit_count, pigeon_count = 0, 0, 0, 0
        # Loop through every position of the 3D_grid list. 
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                for z in range(self.grid_size_z):
                    animal = self.occupant(x,y,z) 
                    # If there is an animal corresponding to the type looking for,
                    # add count.            
                    if animal and not add_stat:
                        if isinstance(animal, Wolf):     wolf_count+=1
                        if isinstance(animal, Eagle):   eagle_count+=1
                        if isinstance(animal, Rabbit): rabbit_count+=1
                        if isinstance(animal, Pigeon): pigeon_count+=1
                    # If the add_stat condition is true,
                    # append the animal's data (i.e., life time and number of offspring)
                    # to the Island attributes.
                    # This will be used at the end of the simulation to
                    # gather the statistics of animals that are still alive.
                    elif animal and add_stat:
                        self.life_dict[animal.name].append(animal.life_time)
                        self.offspring_dict[animal.name].append(animal.offspring)
        # Update the Island attributes if add_stat=False.
        if not add_stat:
            self.wolf_count,    self.eagle_count =   wolf_count,  eagle_count
            self.rabbit_count, self.pigeon_count = rabbit_count, pigeon_count  


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


## Plant-------------------------------------------------------------------------
class Plant(object):
    def __init__(self, island, x=0, y=0, z=0, s="P"):
        """ Initialise a plant class as food for Preys.
        """
        self.island = island
        self.name = s
        self.x, self.y, self.z = x, y, z
        self.life_time = 0
        self.eaten_time = 0
        self.eaten = False
    
    
    ##-----------------------------------------------------------------------
    def __str__(self):
        """ Prints the name of the Plant.
        """
        return self.name
    
    
    ## -----------------------------------------------------------------------------
    def position(self):
        ''' Return coordinates of the animal's current position.
        '''
        return self.x, self.y, self.z
        
        
    ##-----------------------------------------------------------------------
    def grow(self):
        """ When a Plant grows back, its eaten flage becomes False.
        """
        if self.eaten_time >= self.growth_time:
            assert self.eaten==True
            self.eaten = False
            self.eaten_time = 0
    
    
    ##-------------------------------------------------------------------------
    def clock_tick(self):
        ''' Grass updates life_time.
        '''
        self.life_time += 1
        if self.eaten: self.eaten_time += 1
        self.grow()
        #print('Tick {} {},{},{}; life:{}, eaten_time:{}'.format(self.name,
        #       self.x,self.y,self.z, self.life_time, self.eaten_time)) # Debug
        if self.life_time % (24*self.growth_time) == 0 and \
           random.randint(0,2)==1: self.eaten = True


##----------------------------------------------------------------------------
class Grass(Plant):
    def __init__(self, island, x=0, y=0, z=0, s="g"):
        """ Grass is a subclass of Plant; it can be eaten by Rabbit.
        """
        Plant.__init__(self, island, x, y, z, s)
        self.growth_time = self.regrowth
    
    
##---------------------------------------------------------------------------
class Fruit(Plant):
    def __init__(self, island, x=0, y=0, z=0, s="f"):
        """ Fruit is a subclass of Plant; it can be eaten by Prey.
        """
        Plant.__init__(self, island, x, y, z, s)
        self.growth_time = self.regrowth
        

##--------------------------------------------------------------------------
## Animal Class---------------------------------------------------------------------------------------------------
class Animal (object):
    def __init__(self, island, x=0, y=0, z=0, s="A", s_range=2):
        """ Initialize an Animal class, with their positions and names.
        """
        # Storing the information as class attributes.
        self.island = island
        self.name = s
        self.x, self.y, self.z = x, y, z
        self.moved = False
        self.life_time, self.offspring = 0, 0
        self.check_grid_list = [(i,j,k) for i in range(-1,2)
                   for j in range(-1,2) for k in range(-1,2) 
                                        if (i,j,k)!=(0,0,0)]
        assert len(self.check_grid_list)==26, "Error in chech grid list"
        self.search_set = set((i,j,k) for i in range(-s_range, s_range+1)
                                      for j in range(-s_range, s_range+1)
                                      for k in range(-s_range, s_range+1) 
                                      if (i,j,k)!=(0,0,0)).difference(
                          set(self.check_grid_list))
        assert len(self.search_set)==98, "Error in search_set"
        

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
    def check_grid(self, type_looking_for=int):
        ''' Look randomly at all possible locations from the animal's location
        and return a location that is presently occupied by an object
        of the specified type. Return 0 if no such location exists
        '''
        # Generate a set of neighbour offset tuples.
        # Animals can only search positions that are in this list.
        # An animal can inspect a maximum of 26 positions.
        #start = time.time()
        offset = self.check_grid_list
        assert len(offset)==26, "Error in offset list."
        # Randomly look through positions with offset to current position included in offset
        # by shuffling the list.
        # Every time this loop is entered, the offset list would have a different order.
        result = 0
        random.shuffle(offset)
        for index in range(len(offset)):         
            x = self.x + offset[index][0]  # neighbouring x,y,z coordinates
            y = self.y + offset[index][1]
            if isinstance(self, Eagle) or isinstance(self, Pigeon):  
                # Eagle or pigeon have no restrictions on their positions.              
                z = self.z + offset[index][2]                
            else:
                # Wolf and rabbit are restricted to layer_0.
                z = self.z
            # If a position is found, return its coordinates and exit loop.
            if 0 <= x < self.island.grid_size_x and \
               0 <= y < self.island.grid_size_y and \
               0 <= z < self.island.grid_size_z and \
               isinstance(self.island.occupant(x,y,z), type_looking_for):      
                   result=(x,y,z)
                   break
        # If an object of the specified type cannot be found, result=0.
        #print("check_grid took {}".format(time.time()-start))
        return result


    ## searching for a particular animal two grids away-----------------------
    def search(self, type_search=int, s_range=2):
        if s_range==2:
            search_set = self.search_set # only search 2 grids away.
            for elem in search_set:
                x = self.x + elem[0]  # neighbouring x,y,z coordinates
                y = self.y + elem[1]
                z = self.z + elem[2]
                # If the position is outside the 3D grid, choose another one.
                if not 0 <= x < self.island.grid_size_x or \
                   not 0 <= y < self.island.grid_size_y or \
                   not 0 <= z < self.island.grid_size_z: continue
                # If a position is found, return its coordinates and exit loop.
                if isinstance(self.island.occupant(x,y,z), type_search):
                    return (x,y,z), self.island.occupant(x,y,z).name
                    break
                
        elif s_range==1:
            search_list = self.check_grid_list
            return_dict = {} # To hold all valid positions.
            for elem in search_list:
                x = self.x + elem[0]  # neighbouring x,y,z coordinates.
                y = self.y + elem[1]
                z = self.z + elem[2]
                # If the position is outside the 3D grid, choose another one.
                if not 0 <= x < self.island.grid_size_x or \
                   not 0 <= y < self.island.grid_size_y or \
                   not 0 <= z < self.island.grid_size_z: continue
                # If a position is found, append to return_list.
                if isinstance(self.island.occupant(x,y,z), type_search):
                    return_dict[(x,y,z)]=self.island.occupant(x,y,z).name
            return return_dict
    
    
    ##-------------------------------------------------------------------------    
    def get_position(self,coordinate=(0,0,0),other_type=None):
        assert isinstance(coordinate, tuple), "Error in get_position"
        position_set = set()
        for elem in self.check_grid_list:
            x = elem[0] + coordinate[0]
            y = elem[1] + coordinate[1]
            z = elem[2] + coordinate[2]
            if 0 <= x < self.island.grid_size_x and \
               0 <= y < self.island.grid_size_y and \
               0 <= z < self.island.grid_size_z:
                   if other_type is None:
                       if isinstance(self, Wolf) or isinstance(self, Rabbit):
                           assert coordinate[2]==0, "Error in get_position"
                           position_set.add((x, y, coordinate[2]))
                       elif isinstance(self, Eagle) or isinstance(self, Pigeon):
                           position_set.add((x, y, z))
                   else: 
                       if other_type=="W" or other_type=="r":
                           assert coordinate[2]==0, "Error in get_position"
                           position_set.add((x, y, coordinate[2]))
                       else:
                           position_set.add((x, y, z))
        return position_set
        
    
    ## Secondary and more strategic move method-------------------------
    def move_towards(self, search_type=int):
        """ Search for prey or predator at two grids away.
        If one present, move according to type. 
        """
        # This is done using sets. In particular, the reachable positions
        # of an animal is stored in a set. The predator will move to one of the
        # common positions assessible by both animals.
        # Those positions are found using set intersections.
        if self.search(type_search=search_type, s_range=2) and not self.moved:
            position, name = self.search(type_search=search_type, s_range=2)
            move_range = self.get_position(coordinate=(self.x,self.y,self.z)) \
                       & self.get_position(coordinate=position, other_type=name)
            for val in move_range:
                assert abs(self.x-val[0])<=1 and abs(self.y-val[1])<=1 \
                   and abs(self.z-val[2])<=1, "Error in move"
                if isinstance(self.island.occupant(val[0],val[1],val[2]), int):                   
                    #print('Move_towards, {} to {}; from {},{},{} to {},{},{}'.format(
                    #       self.name,name,self.x,self.y,self.z,
                    #       val[0],val[1],val[2]))       #debug
                    self.island.remove(self)   # Remove instance from current spot.
                    self.x = val[0]            # New x,y,z coordinates.
                    self.y = val[1]
                    self.z = val[2]
                    self.island.register(self) # Register instance at new coordinates.
                    self.moved=True
                    break
    
    
    ##--------------------------------------------------------------------
    def move_away(self, search_type=int):
        """ A Prey looks for nearby (i.e. a grid away) Predators and move
        away from them.
        """
        # This is also done with sets, similar to the move_towards method.
        # However, the position choices are created by the differece of sets.
        location_dict = self.search(type_search=search_type, s_range=1)
        if location_dict and not self.moved:
            move_range = self.get_position(coordinate=(self.x, self.y, self.z))
            for location, name in location_dict.items():
                move_range = move_range.difference(self.get_position(
                                         coordinate=location, other_type=name))
            if move_range:
                for val in move_range:
                    assert abs(self.x-val[0])<=1 and \
                           abs(self.y-val[1])<=1 and \
                           abs(self.z-val[2])<=1, "Error in move"
                    if isinstance(self.island.occupant(val[0],val[1],val[2]), int):                   
                        #print('Move_away, {} from {}; from {},{},{} to {},{},{}'.format(
                        #       self.name, name, self.x,self.y,self.z,
                        #       val[0],val[1],val[2]))       #debug
                        self.island.remove(self)   # Remove instance from current spot.
                        self.x = val[0]            # New x,y,z coordinates.
                        self.y = val[1]
                        self.z = val[2]
                        self.island.register(self) # Register instance at new coordinates.
                        self.moved=True
                        break

    
    ## -----------------------------------------------------------------------------
    def move(self):
        ''' Move to an open, neighbouring position
        '''
        # An animal is only allowed to move once per clock tick. 
        # Look for an empty cell, i.e., cell occupied by 0.
        location = self.check_grid(int)
        if location and not self.moved:
            assert abs(self.x-location[0])<=1 and abs(self.y-location[1])<=1 \
               and abs(self.z-location[2])<=1, "Error in move"
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
                #new_animal.move_clock = self.move_clock
                self.island.register(new_animal)    
                self.offspring += 1
                #print('{} Breeding {},{},{}'.format(
                #       str(self.name),self.x,self.y,self.z)) # debug


##----------------------------------------------------------------------------
## Prey Class--------------------------------------------------------------------
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
        self.starve_clock-= 1
        self.life_time += 1
        #print('Tick Prey {},{},{} breed:{} life:{}'.format(
        #       self.x,self.y,self.z,self.breed_clock,self.life_time)) # debug
        if self.starve_clock <= 0 or self.life_time >= self.life_max:
            self.island.remove(self)
            self.island.life_dict[self.name].append(self.life_time)
            self.island.offspring_dict[self.name].append(self.offspring)            
            #print('Death, {} at {},{},{}, life={}'.format(
            #       self.name,self.x,self.y,self.z,self.life_time)) # Debug
        
    def feed(self, plant_type):
        ''' Prey looks at the offset locations for Plant.
        If found, it moves to that location and updates its starve clock.
        The Plant's eaten attribute is updated.
        '''
        # Eating involves moving; it can only be performed once per clock tick.
        if not self.moved:
            plant = self.check_grid(plant_type)
            if plant and not self.island.occupant(plant[0],
                                                  plant[1],plant[2]).eaten:
                assert self.island.occupant(plant[0],plant[1],plant[2]).eaten==False
                #print('Eating: {} at {},{},{} {} at {},{},{}'.format(
                #       str(self.name),self.x,self.y,self.z,
                #       self.island.occupant(location[0],location[1],location[2]),
                #       location[0],location[1],location[2])) # debug
                self.island.occupant(plant[0],plant[1],plant[2]).eaten=True
                self.starve_clock=self.starve_time
                #self.moved=True
    
    ## ---------------------------------------------------------------------
    def reposition(self):
        """ Move away from predators that are nearby. 
        """
        self.move_away(search_type=Predator) or \
        self.move_towards(search_type=Plant)

##--------------------------------------------------------------------------
## Predator Class-----------------------------------------------------------------------------------
class Predator(Animal):
    def __init__(self, island, x=0,y=0,z=0,s="Pred"):
        """Initialise the Predator class as a subclass of Animal.
        """        
        Animal.__init__(self,island,x,y,z,s)


    ## Update clocks--------------------------------------------------------
    def clock_tick(self):
        ''' Predator updates breeding, starving and life_time
        '''
        self.breed_clock -= 1
        self.starve_clock-= 1
        self.life_time += 1
        #print('Tick Predator {},{},{} breed:{} starve: {} life:{}'.format(
        #       self.x,self.y,self.z,
        #       self.breed_clock,self.starve_clock,self.life_time)) # Debug
        
        # If the predator's starve clock is 0, remove it from Island, 
        # register its data to Island's offspring_dict and life_dict.
        if self.starve_clock <= 0 or self.life_time >= self.life_max:
            self.island.remove(self)
            self.island.life_dict[self.name].append(self.life_time)
            self.island.offspring_dict[self.name].append(self.offspring)            
            #print('Death, {} at {},{},{}, life={}'.format(
            #       self.name,self.x,self.y,self.z,self.life_time)) # Debug
            
            
     ## Hunt prey method-------------------------------------------------------
    def hunt(self, prey_type):
        ''' Predator looks at the offset locations for Prey.
        If found, it moves to that location and updates its starve clock.
        The Prey is removed.
        Register the data of the eaten prey to offspring_dict and life_dict.
        '''
        # Eating involves moving; it can only be performed once per clock tick.
        if not self.moved:
            location = self.check_grid(prey_type)
            if location:
                #print('Eating: {} at {},{},{} {} at {},{},{}'.format(
                #       str(self.name),self.x,self.y,self.z,
                #       self.island.occupant(location[0],location[1],location[2]),
                #       location[0],location[1],location[2])) # debug
                
                # Add the statistics of the Prey animal to appropriate Island attributes.
                # Life-time:
                self.island.life_dict[str(self.island.occupant(
                        location[0],location[1],location[2]))].append(
                            self.island.occupant(
                                location[0],location[1],location[2]).life_time)                 
                # Number of offspring:
                self.island.offspring_dict[str(self.island.occupant(
                        location[0],location[1],location[2]))].append(
                            self.island.occupant(
                                location[0],location[1],location[2]).offspring) 

                # Remove the eaten animal and move the Predator instance to its position.
                self.island.remove(self.island.occupant(location[0],location[1],location[2]))
                self.island.remove(self)
                self.x=location[0]
                self.y=location[1]
                self.z=location[2]
                self.island.register(self)
                self.starve_clock=self.starve_time
                self.moved=True


##--------------------------------------------------------------------------        
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
        self.life_max = self.max_life - random.randint(0,2)
        #self.move_clock, self.life_time, self.offspring = 0, 0, 0
        

    ## Eat based on eat----------------------------------------------------
    def eat(self):
        ''' Eagles can eat pigeons and rabbits.
        '''
        self.hunt(prey_type = Prey)

    def reposition(self):
        """ Move towards preys and away from wolves that are two grids away. 
        """
        self.move_towards(search_type=Prey) or self.move_away(search_type=Wolf)
        

##--------------------------------------------------------------------------        
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
        self.life_max = self.max_life - random.randint(0,2)
        #self.move_clock, self.life_time, self.offspring = 0, 0, 0
        

    ## Eat method based on the eat method------------------------------------------------------------------------------
    def eat(self):
        ''' Wolves can eat rabbits, eagles and pigeons.
        '''
        self.hunt(prey_type=Prey) or self.hunt(prey_type=Eagle)
    
    
    ## Secondary move method------------------------------------------------
    def reposition(self):
        """ Move towards preys that are two grids away. 
        """
        self.move_towards(search_type=Prey) or self.move_towards(search_type=Eagle)


##-------------------------------------------------------------------------
## Rabbit class--------------------------------------------------------------------------------------------
class Rabbit (Prey):
    def __init__(self, island, x=0, y=0, z=0, s="r"):
        """Initialise the Rabbit class as a subclass of Prey.
        Rabbit inherits from Prey.
        Add life_time, offspring breed_clock attributes to every instance.
        """         
        Prey.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.starve_clock= self.starve_time
        self.life_max = self.max_life - random.randint(0,2)
        #self.move_clock, self.life_time, self.offspring = 0, 0, 0

    def eat(self):
        self.feed(plant_type=Plant)
##--------------------------------------------------------------------------
## Pigeon class--------------------------------------------------------------------------------------------
class Pigeon (Prey):
    def __init__(self, island, x=0, y=0, z=0, s="p"):
        """Initialise the Rabbit class as a subclass of Prey.
        Pigeon inherits from Prey.
        Add life_time, offspring breed_clock attributes to every instance.
        """          
        Prey.__init__(self,island,x,y,z,s)
        self.breed_clock = self.breed_time
        self.starve_clock= self.starve_time
        self.life_max = self.max_life - random.randint(0,2)
        #self.move_clock, self.life_time, self.offspring = 0, 0, 0

    def eat(self):
        self.feed(plant_type=Fruit)
##--------------------------------------------------------------------------    
## Animation function----------------------------------------------------------
def animation(data, ax, plot=None,x=0,y=0,z=0):
    assert isinstance(data,dict)
    if plot:
        #plot.remove()
        ax.cla() # Clear the axis for re-drawing.
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim((0, x))
        ax.set_ylim((0, y))
        ax.set_zlim((0, z))
        ax.set_autoscale_on(False)
    # Iterate through the stat-dictionary to update all animals.
    # The annotation for each animal shows its name, life-time and number of offspring.
    colour_dict = {"W":"b", "E":"y", "p":"r", "r":"c", "g":"g", "f":"m"}
    indicators  = {"g":{True:"k", False:"g"}, "f":{True:"k", False:"m"}}
    size_dict   = {"W":700, "E":650, "p":600, "r":600, "g":45, "f":45}
    for name, stats in data.items():
        if name in ["W","E","p","r"]:
            for i in range(len(stats[0])):
                plot = ax.scatter(stats[0][i], stats[1][i], stats[2][i], 
                          marker="${} ({},{})$".format(name,stats[3][i],
                          stats[4][i]), color=colour_dict[name], s=size_dict[name])
        elif name in ["g","f"]:
            for i in range(len(stats[0])):
                plot = ax.scatter(stats[0][i], stats[1][i], stats[2][i],
                          marker=".", color=indicators[name][stats[4][i]], 
                          s=size_dict[name])
    try:
        plt.pause(0.01) # Pause the plot for it to update.
    except: pass
    return plot


## Statistics printing function------------------------------------------------
def print_stat(island=None, animal_list=[]):
    """ Add the data of the animals that are still alive 
    to appropriate Island attributes.
    Loop through every animal and print associated results."""
    island.count_animal(add_stat=True)
    for elem in animal_list:
        stat_list = island.cal_stat(type=elem)
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
    #print("\nlife", island.life_dict,"\noffspring",island.offspring_dict)  # Debug
    #print(island)


## Function for plotting animal statistics-----------------------------------------------------
def stat_plot(W_list=[], E_list=[], p_list=[], r_list=[]):
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1)
    ax.plot(p_list,"r",label="Pigeon",linewidth=2)
    ax.plot(r_list,"g",label="Rabbit",linewidth=2)
    ax.plot(E_list,"y",label="Eagle",linewidth=2)
    ax.plot(W_list,"b",label="Wolf",linewidth=2)
    ax.legend(bbox_to_anchor=(0.75, 0.7), loc=3, borderaxespad=0.)
    ax.set_ylabel(r"$Number$ $of$ $Alive$ $Animals$", fontsize = 15)
    ax.set_xlabel(r"$Clock$ $Tick$", fontsize=15)
    ax.set_title(r"$Population$ $Fluctuation$", fontsize=20)
    plt.show()


##-------------------------------------------------------------------------
## Main Program for simulation------------------------------------------------------------------------------------------------
def main(eagle_breed_time =13, eagle_starve_time=13, initial_eagles=13,
         wolf_breed_time  =15,  wolf_starve_time=12, initial_wolves=10,
         eagle_max_life   =45, wolf_max_life    =40,
         pigeon_breed_time=8,   pigeon_max_life =28, initial_pigeons=30,
         rabbit_breed_time=6,   rabbit_max_life =32, initial_rabbits=32,
         rabbit_starve_time=10, pigeon_starve_time=12,
         initial_grass=90, initial_fruit=100, grass_regrowth=8,
         fruit_regrowth=7,
         x=30, y=30, z=3, ticks=800, stop=True,
         print_statistics=False, plot_statistics=True, anim=True):
    ''' Main simulation. Sets defaults, runs event loop,
    plots data at the end, creates 3D-scatter-animation and
    print statistics if enabled.
    '''
    ## Initialization of class attributes.------------------------------------
    Eagle.breed_time, Eagle.starve_time= eagle_breed_time, eagle_starve_time
    Wolf.breed_time, Wolf.starve_time =  wolf_breed_time, wolf_starve_time
    Eagle.max_life, Wolf.max_life    =  eagle_max_life, wolf_max_life 
    Pigeon.breed_time, Pigeon.max_life = pigeon_breed_time, pigeon_max_life
    Rabbit.breed_time, Rabbit.max_life = rabbit_breed_time, rabbit_max_life
    Rabbit.starve_time, Pigeon.starve_time = rabbit_starve_time, pigeon_starve_time
    Grass.regrowth, Fruit.regrowth = grass_regrowth, fruit_regrowth
    
    ## Create lists to hold statistics for graphing---------------------------
    # If plotting is enabled.    
    if plot_statistics:    
        pigeon_list, rabbit_list, eagle_list, wolf_list = [], [], [], []
    
    ## Initialise an Island, called land--------------------------------------
    land = Island(x,y,z, initial_wolves, initial_eagles, initial_rabbits,
                  initial_pigeons, initial_grass, initial_fruit)
    island_size = land.size()
    #print(land)

    ## Create a figure-object on which the animation will occur----------------
    if anim:    
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, projection='3d') # Animation in 3D axes
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_xlim((0, x))
        ax1.set_ylim((0, y))
        ax1.set_zlim((0, z))
        ax1.set_autoscale_on(False)
        plt.ion()
        plt.show()
        W = None # Create an artist on which the scatter points are drawn. 

    ## Simulation Loop-----------------------------------------------------------------------------
    # Simulate using a for loop. 
    # Every clock tick, look at every position of the Island,
    # do tasks if there is an animal there.
    # Every time entering the for-loop, clear the moved flags of all animals.
    # If one of the populations become zero, exit the loop.
    for i in range(ticks):
        if anim:
            W = animation(land.get_locations(), ax1, plot=W, x=x, y=y, z=z)
        land.clear_all_moved_flags()
        #print(land)  # debug
        for x in range(island_size[0]):
            for y in range(island_size[1]):
                for z in range(island_size[2]):
                    instance = land.occupant(x,y,z)
                    # Execute actions according to the type of instance.
                    if isinstance(instance, Plant): instance.clock_tick()
                    if isinstance(instance, Animal) and not instance.moved:
                        instance.eat()  or instance.reposition() or \
                        instance.move() or instance.breed() or \
                        instance.clock_tick()
        
        # Record population data for plotting.
        # Append the counts to a list only if plotting is enabled.
        land.count_animal() 
        if plot_statistics:
            pigeon_list.append(land.pigeon_count)
            rabbit_list.append(land.rabbit_count)
            eagle_list.append(land.eagle_count)
            wolf_list.append(land.wolf_count)
        # Exit the simulation if one population becomes 0.
        if stop and (land.rabbit_count == 0 or land.pigeon_count == 0):
            print('Lost the Prey population. Quiting.')
            break
        if stop and (land.wolf_count == 0 or land.eagle_count == 0):
            print('Lost the Predator population. Quitting.')
            break
        #print(land)
        
        # Print out every 10th cycle, see what's going on.
        # Print the island, hold at the end of each cycle to get a look.
        if not i%50 and i!=0:
            print("ticks: {:>11}".format(i))
            print("pigeon_count: {:>4} \nrabbit_count: {:>4} "
                  "\nwolf_count: {:>6} \neagle_count {:>6}\n".format(
                   land.pigeon_count, land.rabbit_count, 
                   land.wolf_count, land.eagle_count))

        
    ## Statistics analysis and printing-----------------------------------------
    if print_statistics:
        print_stat(island=land,animal_list=["W","E","p","r"])
    
    
    ## Closing the 3D animation after existing the loop.--------------------
    if anim:
        plt.ioff()
        plt.pause(3) # Pause the plot at the end for inspection.
        plt.close()  # Close the plot.
    
    ## Plotting population fluctuation over the simulation.-----------------
    if plot_statistics:
        stat_plot(W_list=wolf_list, E_list=eagle_list, 
                  p_list=pigeon_list, r_list=rabbit_list)


##--------------------------------------------------------------------------
## Calling the main program-----------------------------------------------------
start = time.time() # To determine the efficiency of the program.
main()
print("total took {}s".format(time.time()-start)) # Efficiency test.
