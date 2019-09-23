import random
import copy

class NQueen(object):
    # Below function verifies whether the current state of the board is the solution(I.e with zero conflicts)
    def CheckSolution(self, a, n):
        if self.ConflictSum(a, n) == 0:
            return True
        return False


    # This method calculates all the diagonal conflicts for a particular position of the queen
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


    # This method calculates the conflicts for the current state of the board and quits whenever finds a better state.
    def OptimalSolution(self, a, n):
        conflicts = 0
        row = -1
        col = -1
        bettersol = False
        optimalSol = []
        # Sets min variable to the conflicts of current board so that if finds better than this it will quit.
        currentMin = self.ConflictSum(a, n)
        optimalSol = copy.deepcopy(a)
        # Create a duplicate array for handling different operations
        i = 0
        while i < n:
            # This iteration is for each column
            if bettersol:
                # If it finds and better state than the current, it will quit
                break
            m = optimalSol[i]
            j = 0
            while j < n:
                # This iteration is for each row in the selected column
                if j != m:
                    # This condition ensures that, current queen position is not taken into consideration.
                    optimalSol[i] = j
                    conflicts = self.ConflictSum(optimalSol, n)
                    if currentMin > conflicts:
                        # If a better state is found, that particular column and row values are stored
                        col = i
                        row = j
                        currentMin = conflicts
                        bettersol = True
                        break
                optimalSol[i] = m
                # Restoring the array to the current board position
                j += 1

            i += 1
        if col == -1 or row == -1:
            # If there is no better state found
            print("local maxima at " ,conflicts ," calling random regenerate")
            return False
        a[col] = row
        return True
        # Returns true to the main function if there is any better state found


    # This method returns total number of conflicts for a particular queen position
    def ConflictSum(self, a, n):
        conflicts = 0
        conflicts = self.RowConflict(a, n) + self.DiagonalConflict(a, n)
        return conflicts    
    
    # Below function generates a random state of the board
    def GenerateRandomBoard(self, a, n):
        i = 0
        while( i < n):
            a[i] =random.randint(0,n-1) + 0
            i += 1


    # This method calculates all the row conflicts for a queen placed in a particular cell.
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
    
restartsSum = 0
movesSum = 0
optimalMoves = 0

print("Please select one from the below options:")
print("1. Hill Climbing and Random Restart")
print("2.exit ")
      
choice = int(input("enter your choice"))
        # Randomly generate the board
if choice == 1:
    n = int(input("Please enter the value of n:"))
    if (n > 1 and n < 4) or n <= 1:
        print("*Please choose n value either greater than 3 or equals to 1 - Program Terminated")
        exit()
    a = [None] * n
    b = [None] * n
    queens = NQueen()
    queens.GenerateRandomBoard(a, n)
    b = copy.deepcopy(a)
    
    print("$$$$$$$$$$    Hill Climbing with Random Restart  $$$$$$$$$$$$$$$")
    while not queens.CheckSolution(a, n):
                # Executes until a solution is found
        if queens.OptimalSolution(a, n):
                    # If a better state for a board is found
            movesSum += 1
            optimalMoves += 1
            continue 
        else:
                    # If a better state is not found
            optimalMoves = 0
            queens.GenerateRandomBoard(a, n)
                    # Board is generated Randomly
            restartsSum += 1
    print("The Number of restarts: ",restartsSum)
    print("Total number of moves: ",movesSum-1)
    # Gives the total number of moves from starting point
    print("Number of moves in the solution set: ",optimalMoves)
    # Gives number of steps in the solution set.
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
    if(restartsSum == 0):
         print("Average steps",movesSum)
    else:
        print("Average steps",movesSum/restartsSum)
  
if choice == 2:
    exit()
