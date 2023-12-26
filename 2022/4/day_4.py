with open(R"C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day4input.txt","r")as t:
    input = t.read().splitlines() #gets rid of the \n

dupcounter = 0
for x in input:
    
    split1 = x.split(',')
    split1_1 = split1[0].split('-')
    split1_2 = split1[1].split('-')
    elf1start = int(split1_1[0])
    elf1end = int(split1_1[1])
    elf2start = int(split1_2[0])
    elf2end = int(split1_2[1])


    if (elf2end >= elf1end and elf2start <=elf1start) or (elf1end >= elf2end and elf1start <=elf2start):
        dupcounter += 1

print(dupcounter) #part 1 answer


dupcounter = 0
for x in input:
    
    split1 = x.split(',')
    split1_1 = split1[0].split('-')
    split1_2 = split1[1].split('-')

    elf1start = int(split1_1[0])
    elf1end = int(split1_1[1])
    elf2start = int(split1_2[0])
    elf2end = int(split1_2[1])

    set1 = set(range(elf1start,elf1end+1))
    set2 = set(range(elf2start,elf2end+1))
    
    if set1.intersection(set2) != set():
        dupcounter+=1


print(dupcounter) #part 2 answer