with open (R'C:\Users\dkim4\OneDrive - Olin College of Engineering\Desktop\PythonWorkSpace\Advent of Code\day2input.txt','r') as t:
    input = t.readlines()

# A and X = rock
# B and Y = paper
# C and Z = scissors

#(1 for Rock, 2 for Paper, and 3 for Scissors)  AND 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
rock = 1
paper = 2
scissors = 3

win = 6
draw = 3
lose = 0

score1 = 0

for i in range(0,len(input)):
    
  

    if ((input[i])[0])==('A') and ((input[i])[2])==('Y'): #Elf plays rock, I play paper (Win)
        score1 += paper+win
    
    elif ((input[i])[0])==('A') and ((input[i])[2])==('Z'): #Elf plays rock, I play scissors (Lose)
        score1 += scissors+lose
    
    elif ((input[i])[0])==('B') and ((input[i])[2])==('X'): #Elf plays paper, I play rock (Lose)
        score1 += rock+lose
    
    elif ((input[i])[0])==('B') and ((input[i])[2])==('Z'): #Elf plays paper, I play scissors (Win)
        score1 += scissors+win
    
    elif ((input[i])[0])==('C') and ((input[i])[2])==('X'): #Elf plays scissors, I play rock (Win)
        score1 += rock+win

    elif ((input[i])[0])==('C') and ((input[i])[2])==('Y'): #Elf plays scissors, I play paper (lose)
        score1 += paper+lose
    
    elif ((input[i])[0])==('A') and ((input[i])[2])==('X'): #rock DRAW
        score1 += rock+draw

    elif ((input[i])[0])==('B') and ((input[i])[2])==('Y'): #paper DRAW
        score1 += paper+draw

    elif ((input[i])[0])==('C') and ((input[i])[2])==('Z'): #scissors DRAW
        score1 += scissors+draw


print(score1) # part 1 answer


#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

score2= 0

for i in range(0,len(input)):
    if ((input[i])[0])==('A') and ((input[i])[2])==('Y'): #Elf plays rock, need to draw, play rock
        score2 += rock+draw
    
    elif ((input[i])[0])==('A') and ((input[i])[2])==('Z'): #Elf plays rock, need to win, play paper
        score2 += paper+win
    
    elif ((input[i])[0])==('B') and ((input[i])[2])==('X'): #Elf plays paper, need to lose, play rock
        score2 += rock+lose
    
    elif ((input[i])[0])==('B') and ((input[i])[2])==('Z'): #Elf plays paper, need to win, play scissors
        score2 += scissors+win
    
    elif ((input[i])[0])==('C') and ((input[i])[2])==('X'): #Elf plays scissors, need to lose, play paper
        score2 += paper+lose

    elif ((input[i])[0])==('C') and ((input[i])[2])==('Y'): #Elf plays scissors, need to draw, play scissors
        score2 += scissors+draw
    
    elif ((input[i])[0])==('A') and ((input[i])[2])==('X'): #ELf plays rock, need to lose, play scissors
        score2 += scissors+lose

    elif ((input[i])[0])==('B') and ((input[i])[2])==('Y'): #ELf plays paper, need to draw, play paper
        score2 += paper+draw

    elif ((input[i])[0])==('C') and ((input[i])[2])==('Z'): #Elf plays scissors, need to win, play rock
        score2 += rock+win

print(score2) #part 2 answer


