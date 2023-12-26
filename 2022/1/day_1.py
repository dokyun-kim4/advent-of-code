with open(R'C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day1input.txt','r') as t:
    numbers = t.readlines()
        
class SpaceError(Exception):
    pass


sums = []
i = 0
total = 0

while True:
    try:
        if not numbers[i].isspace():
            total += int(numbers[i])
            i+=1
        elif numbers[i].isspace():
            raise SpaceError

    except SpaceError:
        sums.append(total)
        total = 0
        i += 1
    if i == len(numbers)-1:
            break

length = len(sums)
    
print(max(sums))   #answer to part 1 

sums.sort()
print(sums[length-1]+sums[length-2]+sums[length-3]) #answer to part 2


