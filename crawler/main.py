__author__ = 'jack'
from multiprocessing import Process, Queue, Pool
from urlCrawler import blogUrl
from contextGather import blogContextGather
import time
from multiThreadCrawler import multithreadCrawler

if __name__ == "__main__":
    crawler = multithreadCrawler()
    crawler.keyword ='부산'
    crawler.ini_date = '2013,1,1'
    crawler.e_date = '2014,10,7'
    crawler.thread_number = 10
    crawler.contextGather = blogContextGather
    crawler.urlGather = blogUrl
    print(crawler)
    crawler.run()




    





