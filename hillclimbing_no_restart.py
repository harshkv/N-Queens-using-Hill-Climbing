import random
import time
import copy

class NQueen(object):
    def PrintBoard(self,OptimalSolution,n):
        i = 0
        while i < n:
            j = 0
            while j < n:
                if j == OptimalSolution[i]:
                    print(" Q ", end="")
                else:
                    print(" x ", end="")
                j += 1
            print()
            i += 1
# This class calculates the collisions or conflicts in a row that any two queens are getting in a particular position.

    def RowConflict(self, a, n):
        conflicts = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i != j:
                    if a[i] == a[j]:
                        conflicts += 1
                j += 1
            i += 1
        return conflicts

# This class calculates the number of collisions or conflicts diagonally that any particular queen is getting in the current cell

    def DiagonalConflict(self, a, n):
        conflicts = 0
        d = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i != j:
                    d = abs(i - j)
                    if (a[i] == a[j] + d) or (a[i] == a[j] - d):
                        conflicts += 1
                j += 1
            i += 1
        return conflicts


# This class sums up the row and diagonal conflict of a particular queen in a particular cell.

    def ConflictSum(self, a, n):
        conflicts = 0
        conflicts = self.RowConflict(a, n) + self.DiagonalConflict(a, n)
        return conflicts

#This function checks for the current state that whether it is a solution or not by checking whether the total number of conflicts is zero
    def CheckSolution(self, a, n):
        if self.ConflictSum(a, n) == 0:
            return True
        return False
    
# This function randomly generates the board
    def GenerateRandomBoard(self, a, n):

         i = 0
         while( i < n):
            a[i] =random.randint(0,n-1) + 0
            i += 1
# This class calls ConflictSum and takes the sum of conflicts from that function for the current state and exit the program whenever a better state is found
    def OptimalSolution(self, a, n):

        global movesSum
        conflicts = 0
        row = -1
        col = -1

        betterSol = False
        OptimalSolution = []
# Puts CurrentMin variable to the sume of conflicts of current state to initiate exit whenever a better state is found 
        CurrentMin = self.ConflictSum(a, n)
        OptimalSolution = copy.deepcopy(a)
# This code creates a new array and column Copys the current state to it so that many operations and checking can be done on this current state
        i = 0
        while i < n:
# This traverse through each column of the new array
            if betterSol:
# Break will be initiated if a better state than current state is found
                break
            m = OptimalSolution[i]
            j = 0
            while j < n:
# This array traversal is iterated over each row against the current column
                if j != m:
#The above condition makes sure that current position of the queen is not selected for further operations 
                    OptimalSolution[i] = j
                    self.PrintBoard(OptimalSolution,n)
                    movesSum +=1
                    
# This assigns the queen to the iterated places and then calculates the sum of conflict for that particular position of the queen
                    conflicts = self.ConflictSum(OptimalSolution, n)
                    if CurrentMin > conflicts:
# this checks for next better state and if it is found then the current values of array positions are stored 
                        col = i
                        row = j
                        CurrentMin = conflicts
                        betterSol = True
                        break
                OptimalSolution[i] = m
# The array is restored  to the board with current positions
                j += 1
            i += 1
        if col == -1 or row == -1:
#this checks for no further better state
            return False
        a[col] = row
        return True
#The OptimalSolutions returns the boolean value as true if the next state that is explored is better than the current state
        

# this function evaluates the solution for N queens with Minimum conflict algorithm
    def FindMinConflict(self, b, n, iterations):
# This array will sstore the This array list is for storing the columns from which a random column will be selected
        columnCopy = []
        self.FillBoard(columnCopy, n)

        randomCount = 0
        movesSum = 0
        OptimalMoves = 0
        row = 0
        maxSteps = iterations
        # The maximum steps that can be allowed to find a solution with this algorithm
        while not self.CheckSolution(b, n):
            # Loops until it finds a solution, 
            randomSelection = random.randint(0,len(columnCopy)-1) + 0
            # Randomly selects a column from the available
            currentValue = b[columnCopy[randomSelection]]
            # This stores the current queue position in the randomly selected column
            randomValue = columnCopy[randomSelection]
            CurrentMin = self.FindColumnCollisions(b, n, randomValue)
            # Sets the minimum variable to the current queue conflicts
            min_compare = CurrentMin
    
            while(not columnCopy):
                columnCopy.remove(randomSelection)
            i = 0
            while i < n:
                if currentValue != i:
                    b[randomValue] = i
                    col = self.FindColumnCollisions(b, n, randomValue)
                    # Calculates the conflicts of the queen at particular position
                    if col < CurrentMin:
                        CurrentMin = col
                        row = i
                i += 1
            if min_compare == CurrentMin:
                # When there is no queen with minimum conflicts than the current position
                if maxSteps != 0:
                    # Checks if the maximum steps is reached
                    if len(columnCopy) >= 0:
                        # checks whether there are columns available in the Array List
                        b[randomValue] = currentValue
                        # recolumnCopys the queen back to the previous position
                        maxSteps -= 1
                    else:
                        self.FillBoard(columnCopy, n)
                else:
                    # If the max steps is reached then, the board is regenerated and initiated the max steps variable
                    randomCount += 1
                    OptimalMoves = 0
                    self.FillBoard(columnCopy, n)
                    maxSteps = iterations
            else:
                # When we find the the position in the column with minimum conflicts
                OptimalMoves += 1
                b[randomValue] = row
                min_compare = CurrentMin
                columnCopy.clear()
                maxSteps -= 1
                self.FillBoard(columnCopy, n)
        print()
        i = 0
        while i < n:
            j = 0
            while j < n:
                if j == b[i]:
                    print(" Q ", end="")
                else:
                    print(" x ", end="")
                j += 1
                
            print()
            i += 1
    
        print("Number of Moves in the solution set: ", OptimalMoves)



 # Below function returns the conflicts of a queen in a particular column of the board
    @classmethod
    def FindColumnCollisions(self, b, n, index):
        conflicts = 0
        t = 0
        i = 0
        while i < n:
            if i != index:
                t = abs(index - i)
                if b[i] == b[index]:
                    conflicts += 1
                elif b[index] == b[i] + t or b[index] == b[i] - t:
                    conflicts += 1
            i += 1
        return conflicts

# Below function fills the Array List with numbers 0 to n-1
    @classmethod
    def FillBoard(self, columnCopy, n):
        i = 0
        while i < n:
            columnCopy.append(i)
            i += 1
        return

succrate = 0
failrate = 0
iteracheck = 3
totalRestart = 0
movesSum = 0

print("Please select one from the below options:")
print("1. Solve n queens with Hill Climbing without restart ")
print("2. exit")
choice = int(input("Please enter the choice:"))
if choice == 1:
    
    n = int(input("Please enter the value of n(no. of queens):"))
    if (n > 1 and n < 4) or n <= 1:
        print("*Please choose n value either greater than 3 or equals to 1 - Program Terminated")
        exit()
    if choice < 1 or choice > 7:
        print("*Program terminated - Wrong option selected")
        exit()
    iteracheck = int(input("Please enter the number of times the reporting needs to be done"))
    while (iteracheck != 0):
        a = [None] * n
        b = [None] * n
        OptimalMoves = 0
        queens = NQueen()
        queens.GenerateRandomBoard(a, n)
 # Randomly generate the board
        b = copy.deepcopy(a)
        print("**********Steepest Ascent without Random Restart*********")
        
        while not queens.CheckSolution(a, n):
#run till a the optimal solution is found \
            if queens.OptimalSolution(a, n):
#check for better state                       
                movesSum += 1
                OptimalMoves += 1
                break 
        
        if queens.CheckSolution(a, n) == True:
            print("Solution found")
            succrate += 1
        else:
            print("Solution not found")
            failrate += 1
#Total number of moves
        print("Total moves count ",movesSum-1)
#Total number of moves in the solution        
        print("Total moves count in solution set ",OptimalMoves)

        i = 0
        while i < n:
            j = 0
            while j < n:
                if j == a[i]:
                    print(" Q ", end="")
                else:
                    print(" x ", end="")
                j += 1
            print()
            i += 1
        iteracheck -= 1
    else:
        print("success rate =",succrate/(succrate+failrate)*100)
        print("failure rate =",failrate/(succrate+failrate)*100)
    
if choice == 2:
    exit()
 
