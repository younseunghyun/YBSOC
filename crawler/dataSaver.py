import time
import pymongo

class dataSaver:

    def __init__(self):
        self.table_name = ''
        self.db_name ='crawler'

    def dataSaving(table_name,db_name, dataQueue):

        total =0
        
        def toFile(table_name,db_name,data,total):
            con = pymongo.MongoClient()
            collection = con[db_name][table_name]
            collection.insert(data)
            total +=1
            print(data['Date'],'dataSaver',dataQueue.qsize(),total)

            
        time.sleep(10)
        while True:
            try:
                # if dataQueue.empty():
                #     print('waiting')
                    
                #     if dataQueue.empty():
                #         break
                #     else:
                #         toFile(dataQueue.get())
                toFile(table_name, db_name, dataQueue.get(),total)
            except Exception as e:
                print(e)
                continue


