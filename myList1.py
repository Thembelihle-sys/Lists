myList1 =  [1, 2, 3]

for v in range (len(myList1)):
    myList1.insert(1, myList1[v])
    print(myList1)

    myList3= [i for i in range(-1,2)]
    print(myList3)

    t = [[3-i for i in range (3)] for j in range (3)]
    S = 0
    for i in range(3):
        S+= t [i][i]
        print(S)
    list = [[0, 1 ,2 , 3] for i in range (2)]
print(list[2][0])
    