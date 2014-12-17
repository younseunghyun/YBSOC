def keywordList(key_list):
        print(key_list)
        key_list_cnt=0
        if len(key_list)>7:
            if len(key_list)%7 ==0:
                key_list_cnt = int(len(key_list)/7)
            else:
                key_list_cnt = int(len(key_list)/7)+1
        else:
            key_list_cnt=1

        #storing query
        query_list=list()
        for cnt in range(key_list_cnt):
            query=''
            for keyword in key_list:
                query+=keyword +' | '
                query = query[:-3]
            query_list.append(query)

        return query_list
