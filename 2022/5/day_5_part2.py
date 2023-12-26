with open (R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day5input.txt","r") as t:
    move = t.read().splitlines()

one = ['S','M','R','N','W','J','V','T']
two = ['B','W','D','J','Q','P','C','V']
three = ['B','J','F','H','D','R','P']
four = ['F','R','P','B','M','N','D']
five = ['H','V','R','P','T','B']
six = ['C','B','P','T']
seven = ['B','J','R','P','L']
eight = ['N','C','S','L','T','Z','B','W']
nine = ['L','S','G']

crates = [one,two,three,four,five,six,seven,eight,nine]

for x in move:

    nomove = x.removeprefix('move')
    nofrom = nomove.split('from')
    howmany = int(nofrom[0])
    noto = nofrom[1].split('to')

    From = int(noto[0])
    To = int(noto[1])

    groups = []
    for i in range (howmany):   #create a group of crates that are getting moved
        groups.append(crates[From-1].pop())
        
    
    newgroup = list(reversed(groups))
    crates[To-1] += (newgroup)  
    

for crate in crates:
    print(crate[-1]) #Part 2 answer








