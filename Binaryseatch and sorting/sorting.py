'''naive approach - bubble sort
eficiency : o(n^2)
space: 0(1) because we dont use any new data structure or list'''

list =[8,3,5,4,2,10]
lengthofy = len(list)-1
for x in range(len(list)):
    for y in range(lengthofy):
        if list[y]>list[y+1]:
            list[y],list[y+1]=list[y+1],list[y]

    lengthofy -= 1 #because every round pushes the largest element to the end. so we do not need to check it that is why it is one less check every round with len -1



# print(list)