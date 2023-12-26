with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day7input.txt","r") as t:
    input = t.read().splitlines()

files = {}

print(input[0].split(" "))


for x in input:
    if x.split(" ")[1] == "cd" and x.split(" ")[2] != "/": # if the $cd command is present, everything under this will be stored in this directory
        currentdir = x.split(" ")[2]  #get name of current directory
        files[currentdir] = 0
        

    elif x.split(" ")[0] == "dir":
            dir = x.split(" ")[1]
            files[dir] = 0
        
    elif x.split(" "):
        pass




           





