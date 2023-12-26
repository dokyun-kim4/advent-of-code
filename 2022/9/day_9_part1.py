import numpy as np


with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day9input.txt","r") as t:
    input = t.read().splitlines()

#starting coordinates
xloc = 0
yloc = 0

tailtravel = [] #store coordinates of locations where the tail went to

tailtravel.append([xloc,yloc])

# if [0,0] in tailtravel:
#     print("yes")

# print(tailtravel)


for x in input:

    split = x.split(" ")
    dir = split[0]   #which way
    dis = int(split[1]) #how far
    print(dir)
    print(dis)

    if dir == "R":  #right
        for i in range (1,dis):
            whereishead = [xloc+1,yloc]
            xloc = whereishead[0]
            print(whereishead)
            if whereishead in tailtravel:
                pass
            else:
                tailtravel.append(whereishead)
        
                
    elif dir == "L":  #left
        for i in range (1,dis):
            whereishead = [xloc-1,yloc]
            xloc = whereishead[0]
            print(whereishead)
            
            if whereishead in tailtravel:
                pass
            else:
                tailtravel.append(whereishead)
        

    elif dir == "U":  #up
        for i in range (1,dis):
            whereishead = [xloc,yloc+1]
            yloc = whereishead[1]
            print(whereishead)
            if whereishead in tailtravel:
                pass
            else:
                tailtravel.append(whereishead)
        
           

    elif dir == "D":  #down
        for i in range (1,dis):
            whereishead = [xloc,yloc-1]
            yloc = whereishead[1]
            print(whereishead)
            if whereishead in tailtravel:
                pass
            else:
                tailtravel.append(whereishead)
        


print(len(tailtravel))


