__author__ = 'jack'
from multiprocessing import Process, Queue, Pool
import time


class multithreadCrawler():
    
    stack = Queue()
    output = Queue()
    
    def worker(inputQueue,outputQueue):
        while True:
            try:
                if inputQueue.empty():
                    time.sleep(5)
                    if inputQueue.empty():
                        break
                    else:
                        contextGather(inputQueue.get())
                outputQueue.put(contextGather(inputQueue.get()))
            except Exception    as e:
                print(e)
                continue

    def run():
        for s in range(1,thread_number+1):
            Process(target=worker, args=(stack,)).start()
        Process(target=urlGather, args=(keyword,ini_date,e_date,stack,)).start()


    def __repr__():
        print('keyword : %s ini_date : %s end_date : %s thread_number : %s' %(keyword,ini_date,e_date,thread_number))

    def __init__(self):
        self.keywrod = ''
        self.ini_date = ''
        self.e_date = ''
        self.thread_number = 1
        self.contextGather = ''
        self.urlGather = ''
        self.dataSaver = ''
    
    @configCheck    
    @property
    def keywrod(self):
        return self._keywrod
    @keywrod.setter
    def keywrod(self, value):
        self._keywrod = value
    
    @configCheck    
    @property
    def ini_date(self):
        return self._ini_date
    @ini_date.setter
    def ini_date(self, value):
        self._ini_date = value
    
    @configCheck    
    @property
    def e_date(self):
        return self._e_date
    @e_date.setter
    def e_date(self, value):
        self._e_date = value
    
    @configCheck        
    @property
    def thread_number(self):
        return self._thread_number
    @thread_number.setter
    def thread_number(self, value):
        self._thread_number = value
    
    
    @property
    def contextGather(self):
        return self._contextGather
    @contextGather.setter
    def contextGather(self, value):
        self._contextGather = value
    
      
    @property
    def urlGather(self):
        return self._urlGather
    @urlGather.setter
    def urlGather(self, value):
        self._urlGather = value


    

    def configCheck(self):
            print('keyword : %s ini_date : %s end_date : %s thread_number : %s' %(self.keyword,self.ini_date,self.e_date,self.thread_number))





