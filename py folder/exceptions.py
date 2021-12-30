myint = int(raw_input())
reallist = []
for i in range(myint):
    mylist = map(str,raw_input().split())
    reallist.append(mylist)
    try:
        print int(reallist[i][0])/int(reallist[i][1])
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e   