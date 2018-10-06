def count_animal(self, type=int, add_stat=False):
        ''' Count specified type of animal on the island,
        and statistics of the animals can be appended
        to the appropriate lists.'''
        print("in count")
        count = 0       
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                for z in range(self.grid_size_z):
                    animal = self.animal(x,y,z)             
                    if animal and isinstance(animal, type) and not add_stat:
                        count+=1
                    if animal and add_stat:
                        self.life_dict[animal.name].append(animal.life_time)
                        self.offspring_dict[animal.name].append(animal.offspring)
        if not add_stat:
            return count

                        

    def cal_stat(self, type):    
        #self.count_animal(add_stat=True) # append the data of animals that are still alive to 
                                         # the island attributes
        offspring_list = self.offspring_dict[type]
        offspring_list.sort()

        life_list = self.life_dict[type]
        life_list.sort()
        life_num = len(life_list)
        
        offspring_total = 0
        for elem in offspring_list:
            offspring_total += elem
        try:
            offspring_avg = offspring_total/len(offspring_list)
        except ZeroDivisionError:
            offspring_avg = 0
            
        life_total = 0
        for elem in life_list:
            life_total += elem
        try:
            life_avg = life_total/len(life_list)
        except ZeroDivisionError:
            life_avg = 0
        
        offspring_min = offspring_list[0]
        offspring_max = offspring_list[-1]
        life_min = life_list[0]
        life_max = life_list[-1]
        
        if len(offspring_list)%2==1:
            offspring_med = offspring_list[int((len(offspring_list)-1)/2)+1]
        else:
            offspring_med =(offspring_list[int(len(offspring_list)/2-0.5)] + \
                            offspring_list[int(len(offspring_list)/2+0.5)])/2
        
        if len(life_list)%2==1:
            life_med = life_list[int((len(life_list)-1)/2)+1]
        else:
            life_med =(life_list[int(len(life_list)/2-0.5)] + \
                       life_list[int(len(life_list)/2-0.5)])/2
                       
        return life_num, life_max, life_min, life_avg, life_med,\
               offspring_max, offspring_min, offspring_avg, offspring_med
