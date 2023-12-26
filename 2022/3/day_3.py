with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day3input.txt","r") as t:
    input = t.readlines()


priorities = 0


for x in input:
    cutoff = int(len(x)/2)
    strend = len(x)
    str1=(x[0:cutoff])
    str2=(x[cutoff:strend])
    commonletter = list(set(str1)&set(str2))
    unicode = ord((commonletter[0]))
    if unicode > 96 and unicode < 123:
        priorities += unicode-96
    else:
        priorities += unicode-38
    
    
print(priorities) # part 1 answer

badge = 0
counter = 0
with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day3input.txt","r") as p:
    while True:    
        groupsofthree=([next(p).rstrip() for y in range(0,3)])


        str1=groupsofthree[0]
        str2=groupsofthree[1]
        str3=groupsofthree[2]
        
        commonletter = list(set(str1)&set(str2)&set(str3)) #find the common letter between 3 strings
        unicode = ord(str(commonletter[0]))

        if unicode > 96 and unicode < 123:
            badge += unicode-96
        else:
            badge += unicode-38

        counter +=3
        if counter == 300:
            break
        

print(badge) #part 2 answer

