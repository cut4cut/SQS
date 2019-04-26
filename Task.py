import threading
import time

class Task(threading.Thread):
    
    __states_dic = {
        0: 'Wait',
        1: 'InProccesing',
        2: 'Solved',
    }
    
    __kind_dic = {
        0: 0,
        1: 1,
        2: 2,
        3: 3
    }
    
    def __init__(self, kind_id, interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.__interval = interval
        self.__kind = self.__kind_dic[kind_id]
        self.__state = self.__states_dic[0]
    
    def set_state(self, state_id):
        try:
            self.__state = self.__states_dic[state_id]
        except KeyError as e:
            ValueError('Undefined unit: {}'.format(e.args[0]))
            
    def check_state(self):
        return self.__state
    
    def check_kind(self):
        return self.__kind
    
    def run(self):
        self.set_state(1)
        time.sleep(self.__interval)
        self.set_state(2)