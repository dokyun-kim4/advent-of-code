import numpy as np

with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day8input.txt","r") as t:
    input = t.read().splitlines()

length = len(input[0])
arr = np.zeros([length,length])

scenicscore = []

row = 0
for x in input:
    toadd = list(map(int,x))
    arr[row,:]= toadd
    row += 1


visiblecount = 0

for row in range(1,length-1):

    for col in range (1,length-1):
        
        left = arr[row,0:col]
        
        right = arr[row,col+1:length]

        top = arr[0:row,col]
        
        bot = arr[row+1:length,col]
      
        for lefttree in left:  #visibility from left
            if lefttree < arr[row,col]:
                leftvisible = True
            else:
                leftvisible = False
                break
        
        for righttree in right:  #visibility from right
            if righttree < arr[row,col]:
                rightvisible = True
            else:
                rightvisible = False
                break
        
        for toptree in top:  #visibility from top
            if toptree < arr[row,col]:
                topvisible = True
            else:
                topvisible = False
                break

        for bottree in bot:  #visibility from bot
            if bottree < arr[row,col]:
                botvisible = True
            else:
                botvisible = False
                break

        if leftvisible or rightvisible or topvisible or botvisible: # as long as it is visible from one side, we consider it visible
            visiblecount += 1


visiblecount += 99*4-4 #edges
print(visiblecount) #part 1 answer


