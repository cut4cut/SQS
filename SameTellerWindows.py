import threading
import time

class SameTellerWindows(threading.Thread):
    
    __power_by_service_dic = {
        0: 2,
        1: 1,
        2: 4,
        3: 2
    }
    
    __counter_dic = {
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.daemon = True
        self.__state = True
        self.queue = queue
                
    def stop(self):
        self.__state = False
        print(self.__state)
        
    def run(self):
        while self.__state:
            
            for i in self.queue:
                if (i.check_state() == 'Solved'):
                    self.__counter_dic[i.check_kind()] = self.__counter_dic[i.check_kind()] - 1
                    print('TaskKind:{0} isReady -> Solved'.format(i.check_kind()))
                    self.queue.remove(i)
                
                if (i.check_state() == 'Wait'):
                    if(self.__counter_dic[i.check_kind()] < self.__power_by_service_dic[i.check_kind()]):
                        self.__counter_dic[i.check_kind()] = self.__counter_dic[i.check_kind()] + 1
                        print('TaskKind:{0} Wait -> InProccesing'.format(i.check_kind()))
                        # может поменять строчки местами?
                        i.set_state(1)
                        i.start()
                        
        print('End of work Teller Windows simulation')    