import random
import copy

class NQueen(object):
     # Below function fills the Array List with numbers 0 to n-1
    def FillBoard(self, store, n):
        
        i = 0
        while i < n:
            store.append(i)
            i += 1
        return  
 # This method calculates all the row conflicts for a queen placed in a particular cell.
    def RowConflict(self, a, n):
     
        Conflict = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i != j:
                    if a[i] == a[j]:
                        Conflict += 1
                j += 1
            i += 1
        return Conflict
    
    def printBoard(self,b,n):
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
    
    

    # This method calculates all the diagonal conflicts for a particular position of the board  
    def DiagonalConflict(self, a, n):
        Conflict = 0
        d = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i != j:
                    d = abs(i - j)
                    if (a[i] == a[j] + d) or (a[i] == a[j] - d):
                        Conflict += 1
                j += 1
            i += 1
        return Conflict

    # This method returns total number of Conflict for a particular queen position  
    def ConflictSum(self, a, n):
        Conflict = 0
        Conflict = self.RowConflict(a, n) + self.DiagonalConflict(a, n)
        return Conflict
    
    # Below function verifies whether the current state of the board is the solution
    def CheckSolution(self, a, n):
        if self.ConflictSum(a, n) == 0:
            return True
        return False
    
    # Below function generates a random state of the board
    def GenerateRandomBoard(self, a, n):
        i = 0
        while( i < n):
            a[i] =random.randint(0,n-1) + 0
            i += 1

    # Below method finds the solution for the n-queens problem with Min-Conflicts algorithm
    def FindMinConflict(self, b, n, iterations):
        store = []
        self.FillBoard(store, n)
        movesSum = 0
        optimalMoves = 0
        row = 0
        maxSteps = iterations
        # The maximum steps that can be allowed to find a solution with this algorithm
        while not self.CheckSolution(b, n):
            # Loops until it finds a solution
            randomSelection = random.randint(0,len(store)-1) + 0
            # Randomly selects a column from the available
            currentValue = b[store[randomSelection]]
            # This stores the current queue position in the randomly selected column
            randomValue = store[randomSelection]
            currentMin = self.FindColumnCollision(b, n, randomValue)
            # Sets the minimum variable to the current queue Conflict
            min_compare = currentMin
            while(not store):
                store.remove(randomSelection)    
            i = 0
            while i < n:
                if currentValue != i:
                    b[randomValue] = i
                    
                    col = self.FindColumnCollision(b, n, randomValue)
                    # Calculates the Conflict of the queen at particular position
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
                    break
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
        print("Total number of Moves: ", movesSum)
        print("Number of Moves in the solution set: ", optimalMoves)


    def noRestartFindMinConflict(self, b, n, iterations):
        store = []
        self.FillBoard(store, n)
        global succrate
        global failrate
        global movesSum 
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
            currentMin = self.FindColumnCollision(b, n, randomValue)
            # Sets the minimum variable to the current queue Conflict
            min_compare = currentMin
            while(not store):
                store.remove(randomSelection)
            i = 0
            while i < n:
                if currentValue != i:
                    b[randomValue] = i
                    col = self.FindColumnCollision(b, n, randomValue)
                    # Calculates the Conflict of the queen at particular position
                    if col < currentMin:
                        currentMin = col
                        row = i
                i += 1

            if min_compare == currentMin:
                # When there is no queen with minimum conflicts than the current position
                if maxSteps != 0:
                    # Checks if the maximum steps is reached
                    if len(store) > 0:
                        # checks whether there are columns available in the Array List
                        b[randomValue] = currentValue
                        # restores the queen back to the previous position
                        maxSteps -= 1
                        
                    else:
                        self.FillBoard(store, n)
                else:
                    break
            else:
                # When we find the the position in the column with minimum conflicts
           
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
                    print("x ", end="")
                j += 1
            print()
            i += 1
        print(" total moves ",movesSum)
        print("Number of Moves in the solution set: ", optimalMoves)

    def noRestartFindMinConflict(self, b, n, iterations):
        store = []
        self.FillBoard(store, n)
        movesSum = 0
        optimalMoves = 0
        global succstep, failstep,c
        
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
            currentMin = self.FindColumnCollision(b, n, randomValue)
            # Sets the minimum variable to the current queue Conflict
            min_compare = currentMin
            while(not store):
                store.remove(randomSelection)
            i = 0
            while i < n:
                if currentValue != i:
                    b[randomValue] = i
                    col = self.FindColumnCollision(b, n, randomValue)
                    # Calculates the Conflict of the queen at particular position
                    if col < currentMin:
                        currentMin = col
                        row = i
                i += 1

                self.printBoard(b,n)
                print("\n")
                c+=1
            if min_compare == currentMin:
                # When there is no queen with minimum conflicts than the current position
                if maxSteps != 0:
                    
                    # Checks if the maximum steps is reached
                    if len(store) > 0:
                        # checks whether there are columns available in the Array List
                        b[randomValue] = currentValue
                        # restores the queen back to the previous position
                        maxSteps -= 1
                    else:
                        self.FillBoard(store, n)
                else:
                    break
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
        print("Total number of Moves: ", movesSum)
        print("Number of Moves in the solution set: ", optimalMoves)
        
        if queens.CheckSolution(b,n):
            succstep+=movesSum
        else:
            failstep+=movesSum 
        



    # Below function returns the Conflict of a queen in a particular column of the board
     
    def FindColumnCollision(self, b, n, index):
        
        Conflict = 0
        global c
        t = 0
        i = 0
        while i < n:
            if i != index:
                t = abs(index - i)
                if b[i] == b[index]:
                    Conflict += 1
                elif b[index] == b[i] + t or b[index] == b[i] - t:
                    Conflict += 1
            i += 1
            
            
        return Conflict

movesSum = 0
optimalMoves = 0
succrate = 0
failrate = 0



print("Please select one from the below options:")
print("1. Min Conflict method without random restart")
print("2.exit")
choice = int(input("Please enter the choice:"))

if choice == 1:
    successrate=0
    failurerate=0
    c=0
    succstep=0
    failstep=0
    n = int(input("Please enter the value of n(no.of queens):"))

    if (n > 1 and n < 4) or n <= 1:
        print("*Please choose n value either greater than 3 or equals to 1 - Program Terminated")
        exit()
    a = [None] * n
    b = [None] * n
    queens = NQueen()
    queens.GenerateRandomBoard(a, n)
        # Randomly generate the board
    b = copy.deepcopy(a)
    print(" $$$$$$$$  Min Conflict Sideways Without Random Restart  $$$$$$$$")
    print("Enter the number of times to execute")
    notimes = int(input("Please enter the value:"))
    print("Please enter the maximum number of steps for iteration:")
    iterations = int(input("Please enter the value:"))
    while (notimes!=0):
        queens.noRestartFindMinConflict(b, n, iterations)
        
        movesSum += 1
        if queens.CheckSolution(b,n):
            
            print('Solution Found')
            successrate+=1
        else:
            print('No solution Found')
            failurerate+=1
        print(notimes)
        notimes = notimes - 1
        queens.GenerateRandomBoard(b,n)
    if(failstep == 0):
        print(" average success steps",succstep)
    else:
         print(" average failure steps",succstep/c)
        
    print('successrate- '+str(successrate))
    print('failurerate- '+str(failurerate))
    print('Success moves- '+str(succstep))
    print("moves",c)
 
if choice == 2:    
    exit()


