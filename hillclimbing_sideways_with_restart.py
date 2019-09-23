import random
import copy

class NQueen(object):
#generates the board randomly for random restarts
    def GenerateRamdomBoard(self, a, n):
        i = 0
        while( i < n):
            a[i] =random.randint(0,n-1) + 0
            i += 1
 
    def FillBoard(self, store, n):
        i = 0
        while i < n:
            store.append(i)
            i += 1
        return
     
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

    # This method returns total number of conflicts for a particular queen position    
    def ConflictSum(self, a, n):
        conflicts = 0
        conflicts = self.RowConflict(a, n) + self.DiagonalConflict(a, n)
        return conflicts


    def CheckSolution(self, a, n):
        if self.ConflictSum(a, n) == 0:
            return True
        return False

     
    def FindMinConflict(self, b, n, iterations):
        store = []
        self.FillBoard(store, n)
        restartsSum = 0
        movesSum = 0
        optimalMoves = 0
        row = 0
        maxSteps = iterations
        # The maximum steps that can be allowed to find a solution with this algorithm
        while not self.CheckSolution(b, n):
            # Loops until it finds a solution, 
            randomSelection = random.randint(0,len(store)-1) + 0
            # Randomly selects a column from the available
            currentValue = b[store[randomSelection]]
            # This stores the current queue position in the randomly selected column
            randomValue = store[randomSelection]
            currentMin = self.FindColumnCollisions(b, n, randomValue)
            # Sets the minimum variable to the current queue conflicts
            min_compare = currentMin
            while(not store):
                store.remove(randomSelection)
            i = 0
            while i < n:
                if currentValue != i:
                    b[randomValue] = i
                    col = self.FindColumnCollisions(b, n, randomValue)
                    # Calculates the conflicts  of the queen at particular position
                    if col < currentMin:
                        currentMin = col
                        row = i
                i += 1
            if min_compare == currentMin:
                # When there is no queen with minimum conflicts than the current position
                if maxSteps != 0:
                    # Checks if the maximum steps is reached
                    if len(store) >= 0:
                        # checks whether there are columns available in the Array List
                        b[randomValue] = currentValue
                        # restores the queen back to the previous position
                        maxSteps -= 1
                    else:
                        self.FillBoard(store, n)
                else:
                    # If the max steps is reached then, the board is regenerated and initiated the max steps variable
                    restartsSum += 1
                    optimalMoves = 0
                    self.GenerateRamdomBoard(b, n)
                    self.FillBoard(store, n)
                    maxSteps = iterations
            else:
                # When we find the the position in the column with minimum conflicts
                movesSum += 1
                optimalMoves += 1
                b[randomValue] = row
                min_compare = currentMin
                store.clear()
                maxSteps -= 1
                self.FillBoard(store, n)
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
        print("Total number of Random Restarts: ",restartsSum)
        print("Total number of Moves: ", movesSum)
        print("Number of Moves in the solution set: ", optimalMoves)
     
    # Below function returns the conflicts of a queen in a particular column of the board
     
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



print("Please select one from the below options:")
print("1. Sideways Hill Climbing With Random Restart ")
print("2.exit ")

choice = int(input("enter your choice"))
if choice == 1:
    n = int(input("Please enter the value of n(no. of queens):"))
    a = [None] * n
    b = [None] * n
    queens = NQueen()
    queens.GenerateRamdomBoard(a, n)
    b = copy.deepcopy(a)  
    iterations = 0
    print()
    print(" $$$$$$$  Sideways Hill Climbing With Random Restart $$$$$$$$ ")
    iterations= int(input("Please enter the  number of steps for iteration:"))
    queens.FindMinConflict(b, n, iterations)


if choice  == 2:
    exit()
