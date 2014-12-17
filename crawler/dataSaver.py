import time
class dataSaver:

    def dataSaving(dataQueue):

        def toFile(data):
            print(data['Source'])
            open('./'+data['Source']+'.txt','w').write(str(data))

        while True:
            print('hehehe')
            try:
                if dataQueue.empty():
                    time.sleep(10)
                    if dataQueue.empty():
                        break
                    else:
                        toFile(dataQueue.get())
                toFile(dataQueue.get())
            except Exception as e:
                print(e)
                continue


