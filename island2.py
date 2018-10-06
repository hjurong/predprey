import random

class Island (object):
    """Island
       n X n grid where zero value indicates not occupied."""
    def __init__(self, n, prey_count=0, predator_count=0):
        '''Initialize grid to all 0's, then fill with animals
        '''
        #print(n,prey_count,predator_count)
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0]*n    # row is a list of n zeros
            self.grid.append(row)
        #self.init_animals(prey_count,predator_count)

    def size(self):
        '''Return size of the island: one dimension.
        '''
        return self.grid_size

    def register(self,animal):
        '''Register animal with island, i.e. put it at the 
        animal's coordinates
        '''
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def __str__(self):
        '''String representation for printing.
           (0,0) will be in the lower left corner.
        '''
        s = ""
        for j in range(self.grid_size-1,-1,-1):  # print row size-1 first
            for i in range(self.grid_size):      # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    s+= "{:<2s}".format('.' + "  ")
                else:
                    s+= "{:<2s}".format((str(self.grid[i][j])) + "  ")
            s+="\n"
        return s

    ## -----------------------------------------------------------------------------
    def init_animals(self,wolf_count, eagle_count, rabbit_count, pigeon_count):
        ''' Place the initial animals on the island.
        '''
        start_time = time.time()
        # The while-loop continues until  unoccupied positions equalling to
        # wolf_count, eagle_count are found.
        # If the dimensions of the Island are insufficient to hold all the animals,
        # do not enter the loop; and inform the user.
        # Same while loop for all four animals.
        if wolf_count + rabbit_count <= \
                   self.grid_size_x * self.grid_size_y and \
           wolf_count + rabbit_count + pigeon_count + eagle_count <= \
                   self.grid_size_x * self.grid_size_y * self.grid_size_z:
            location_dict = {"ground":[(i,j,0) for i in range(self.grid_size_x)
                                               for j in range(self.grid_size_y)],
                             "sky":[(i,j,k) for i in range(self.grid_size_x)
                                            for j in range(self.grid_size_y)
                                            for k in range(1,self.grid_size_z)]}
            for i in range(wolf_count):
                # Wolves are restricted to layer_0.
                location = location_dict["ground"][
                           random.randint(0,len(location_dict["ground"])-1)]
                new_wolf=Wolf(self,location[0],location[1],location[2])
                self.register(new_wolf)
                location_dict["ground"].remove(location)
            
            for i in range(rabbit_count):
                # Rabbits are restricted to layer_0.
                location = location_dict["ground"][
                           random.randint(0,len(location_dict["ground"])-1)]
                new_rabbit=Rabbit(self,location[0],location[1],location[2])
                self.register(new_rabbit)
                location_dict["ground"].remove(location)
            
            for i in range(eagle_count):
                # No position restrictions for eagles.
                if random.randint(0,1)==0 and location_dict["ground"]:
                    location = location_dict["ground"][
                               random.randint(0,len(location_dict["ground"])-1)]
                    location_dict["ground"].remove(location)
                elif location_dict["sky"]:
                    location = location_dict["sky"][
                               random.randint(0,len(location_dict["sky"])-1)]
                    location_dict["sky"].remove(location)
                new_eagle=Eagle(self,location[0],location[1],location[2])
                self.register(new_eagle)
      
            for i in range(pigeon_count):
                # No position restrictions for pigeons.
                if random.randint(0,1)==0 and location_dict["ground"]:
                    location = location_dict["ground"][
                               random.randint(0,len(location_dict["ground"])-1)]
                    location_dict["ground"].remove(location)
                elif location_dict["sky"]:
                    location = location_dict["sky"][
                               random.randint(0,len(location_dict["sky"])-1)]
                    location_dict["sky"].remove(location)
                new_pigeon=Pigeon(self,location[0],location[1],location[2])
                self.register(new_pigeon)
                
            print(time.time()- start_time)      
            
        else: print("Insufficient Island Dimensions")
    
##-----------------------------------------------------------------
class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        '''Initialize the animal's and their positions
        '''
        self.island = island
        self.name = s
        self.x = x
        self.y = y
            
    def __str__(self):
        return self.name
