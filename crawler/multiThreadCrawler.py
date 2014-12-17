__author__ = 'jack'
from multiprocessing import Process, Queue, Pool
import time
from dataSaver import dataSaver

class multithreadCrawler:
    
    stack = Queue()
    output = Queue()
    
    def __init__(self):
        self.keyword = None
        self.ini_date = None
        self.e_date = None
        self.thread_number = 1
        self.contextGather = None
        self.urlGather = None
        self.dataSaver = None
        

    def __repr__(self):
        return 'keyword : %s ini_date : %s end_date : %s thread_number : %s contextGather : %s urlGather : %s dataSaver : %s' %(self.keyword,self.ini_date,self.e_date,self.thread_number, self.contextGather, self.urlGather, self.dataSaver)



    def worker(self, inputQueue,outputQueue):
        while True:
            try:
                if inputQueue.empty():
                    time.sleep(5)
                    if inputQueue.empty():
                        break
                    else:
                        outputQueue.put(self.contextGather(inputQueue.get()))
                outputQueue.put(self.contextGather(inputQueue.get()))
                #print(outputQueue.qsize())
            except Exception as e:
                print(e)
                continue

    def run(self):
        for s in range(1,self.thread_number+1):
            Process(target=self.worker, args=(self.stack,self.output,)).start()
        Process(target=self.urlGather, args=(self.keyword,self.ini_date,self.e_date,self.stack,)).start()
        Process(target=self.dataSaving, args=(self.output,)).start()

    
    
    
    

    
    

    



