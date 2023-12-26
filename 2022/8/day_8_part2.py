import numpy as np

with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day8input.txt","r") as t:
    input = t.read().splitlines()

length = len(input[0])
arr = np.zeros([length,length])

scenicscores = []

row = 0
for x in input:
    toadd = list(map(int,x))
    arr[row,:]= toadd
    row += 1



for row in range(1,length-1):

    for col in range (1,length-1):
        
        left = list(reversed(arr[row,0:col])) # all trees in the left
        
        right = arr[row,col+1:length] # all trees in the right
        
        top = list(reversed(arr[0:row,col])) # all trees in the top
        
        bot = arr[row+1:length,col] # all trees in the bottom
        
        leftscore = 0
        rightscore = 0
        topscore = 0
        botscore = 0

        for lefttree in left:  #visibility from left
            
            if lefttree < arr[row,col]:
                leftvisible = True
                leftscore += 1
            else:
                leftvisible = False
                leftscore += 1
                break
        
        for righttree in right:  #visibility from right
            
            if righttree < arr[row,col]:
                rightvisible = True
                rightscore += 1
            else:
                rightvisible = False
                rightscore += 1
                break
        
        for toptree in top:  #visibility from top
            
            if toptree < arr[row,col]:
                topvisible = True
                topscore += 1
            else:
                topvisible = False
                topscore += 1
                break

        for bottree in bot:  #visibility from bot
            
            if bottree < arr[row,col]:
                botvisible = True
                botscore += 1
            else:
                botvisible = False
                botscore +=1
                break

        
        
        scenicscore = leftscore*rightscore*topscore*botscore
        scenicscores.append(scenicscore)


print(max(scenicscores)) #part 2 answer


