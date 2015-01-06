__author__ = 'jack'
from multiprocessing import Process, Queue, Pool
from urlCrawler import blogUrl
from dataSaver import dataSaver
from multiThreadCrawler import multithreadCrawler
from contextGather import blogContextGather


if __name__ =='__main__':

    crawler = multithreadCrawler()
    crawler.ini_date = '2014,9,1'
    crawler.e_date = '2015,12,31'
    crawler.thread_number = 100
    crawler.contextGather = blogContextGather
    crawler.urlGather = blogUrl
    crawler.dataSaver = dataSaver.dataSaving
    crawler.table_name='crawler'
    crawler.db_name='bukchon9_12'
    crawler.keyword = '북촌 한옥마을'
    print(crawler)  
    crawler.run()





    





