numbers = [0,1,2,3,4,5,6,7,8,9]
count =0
for x in numbers:
    for y in numbers:
        for z in numbers:
            print(str(x)+str(y) +str(z))
            print("count: " + str(count))
            count +=1