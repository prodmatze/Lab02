list1 = [x for x in range(1, 21)]
list2 = [x for x in range(1, 21)]
def listenzeug():

    for i in range(len(list1)):
        list2[i] = list1[i] * list1[i]
    print("This is List Nr. 1:")
    print(list1)
    print("########")
    print("This is the squared List:")
    print(list2)
def isListEven():
    evenList = []
    for i in range(len(list2)):
        if list1[i]%2 == 0:
            evenList.append(list1[i])
    print("##########")
    print ("This is the List with even Numbers:")
    print (evenList)

listenzeug()
isListEven()




