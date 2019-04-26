import numpy as np
import threading
import time

class MainFlow(threading.Thread):
    
    def __init__(self, queue, interval, mainFlow_count_arr):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.__state = False
        self.count_arr = mainFlow_count_arr
        self.queue = queue
        
    def stop(self):
        self.__state = True

    def make_count_mainFlow_arr(subFlow_count_arr):
        # Each row consict counts of each subFlow per time_step
        self.count_mainFlow = subFlow_count_arr.T
        return subFlow_count_arr.T

    def make_count_subFlow_arr(N, demision, mu, sigma):
        # For creating a martix of random vectors we need first vector of same demision
        temp_arr = np.arange(demision)
        for i in range(N):
            # 1D array of random numbers
            s = np.random.normal(mu, sigma, (100, 1))
            # 1D array of count random numbers for each bean
            count = np.histogram(s, demision)[0]
            # Add new vector to matrix as temp_arr
            temp_arr = np.vstack((temp_arr, count))
        temp_arr = np.delete(temp_arr, 0, 0)
        return temp_arr
    
    def run(self):
        iter_count = 0
        for i in mainFlow_count_arr:
            print('The time step is {0}'.format(iter_count))
            print('The time is {0}'.format(time.ctime()))
            
            if(self.__state):
                print('End of work Main Flow simulation') 
                break
            
            i_temp = np.copy(i)

            while True:
                choose = np.random.randint(4)

                for j in range(4):
                    if(i_temp[j] != 0):
                        #choose_make_dic[j]
                        #print(i_temp[j], j)
                        self.queue.append(Task(j,2))
                        i_temp[j] = i_temp[j] - 1

                if not np.any(i_temp):
                    #print(i_temp)
                    break
            iter_count = iter_count + 1
            time.sleep(self.interval)  