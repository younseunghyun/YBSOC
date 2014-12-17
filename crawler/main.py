__author__ = 'jack'
from multiprocessing import Process, Queue, Pool
from urlCrawler import blogUrl
from contextGather import blogContextGather
import time

def qq(q):
    while True:
        try:
            if q.empty():
                time.sleep(5)
                if q.empty():
                    break
                else:
                    blogContextGather(q.get())
            blogContextGather(q.get())
        except Exception as e:
            print(e)
            continue
if __name__ == '__main__':
    keyword='부산'
    ini_date='2013,1,1'
    e_date='2014,10,7'
    thread_number = 10
    q = Queue()

    print('keyword : %s ini_date : %s end_date : %s thread_number : %s' %(keyword,ini_date,e_date,thread_number))
    for s in range(1,thread_number+1):
        Process(target=qq, args=(q,)).start()
    Process(target=blogUrl, args=(keyword,ini_date,e_date,q,)).start()
    






