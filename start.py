# Names: 
# Leonardo Lindo
# Jordan Seay
# Nam Tran
#


import random
def inarow_Nsouth( ch, r_start, c_start, A, N ):
     #for the 3-in-a-row-east function:

    NR = len(A)   # number of rows is len(A)

    if r_start +N -1>= NR or c_start > len(A[0]):   
        return False    # out of bounds in rows
    # other out-of-bounds checks...
    else:

        for i in range(N):                  # loop i as needed
            if A[r_start+i][c_start] != ch:   # check for mismatches
                return False                # mismatch found - return False
        return True                         # loop found no mismatches - return 
def inarow_Neast( ch, r_start, c_start, A, N ): 
        #for the 3-in-a-row-east function:

    NR = len(A)   # number of rows is len(A)

    if r_start >= NR or c_start +N -1 > len(A[0]):   
        return False    # out of bounds in rows
   
    # other out-of-bounds checks...
    else:

        for i in range(N):                  # loop i as needed
            if A[r_start][c_start+i] != ch:   # check for mismatches
                return False                # mismatch found - return False
        return True                         # loop found no mismatches - return 
    
def inarow_Nsoutheast( ch, r_start, c_start, A, N ): 
     #for the 3-in-a-row-east function:

    NR = len(A)   # number of rows is len(A)

    #NC = 4
    if r_start + N - 1 >= NR or c_start + N -1 > len(A[0]):   
        return False    # out of bounds in rows
   
    # other out-of-bounds checks...
    else:

        for i in range(N):                  # loop i as needed
            if A[r_start+i][c_start+i] != ch:   # check for mismatches
                return False                # mismatch found - return False
        return True                         # loop found no mismatches - return 
   

def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    #for the 3-in-a-row-east function:

    NR = len(A)   # number of rows is len(A)

    #NC = 4
    if r_start -N + 1 >= NR or c_start + N -1 > len(A[0]):   
        return False    # out of bounds in rows
   
    # other out-of-bounds checks...
    else:

        for i in range(N):                  # loop i as needed
            if A[r_start-i][c_start+i] != ch:   # check for mismatches
                return False                # mismatch found - return False
        return True                         # loop found no mismatches - return 
 

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [[' ']*W for row in range(H)]

    def __repr__(self):
        W = self.width
        H = self.height
        s = ''
        for r in range(H):
            s += '|'
            for c in range(W):
                 s += self.data[r][c] + '|'
            s += '\n'
        s += (2*W+1)*'-'
        s += '\n'
        for c in range (W):
            s += ' ' + str(c)
        return s    
        
    def addMove(self, col, ox):
        H = self.height
        for row in range(H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox
    def clear(self):

        self.data = [[' ']*self.width for row in range(self.height)]

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'    

    def allowsMove(self, c):
        if c<0 or c>self.width-1:
            return False
        elif self.data[0][c] == 'X' or self.data[0][c] == 'O':
            return False
        else: 
            return True     
    def isFull(self):
        for i in range(self.width):
            for I in range(self.height):
                if self.data[0][I] == ' ':
                    return False
        return True 
    def delMove(self, c):
        for i in range(self.height):
                if self.data[i][c] != ' ':
                    self.data [i][c] = ' '
                    return
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W):

                if inarow_Neast( ox, row, col, D, 4 ) ==True:
                    return True
                elif inarow_Nsouth( ox, row, col, D, 4 ) ==True:
                    return True
                elif inarow_Nsoutheast( ox, row, col, D, 4 ) ==True:
                    return True
                elif inarow_Nnortheast( ox, row, col, D, 4 ) ==True:
                    return True    
        return False    
    def colsToWin(self,ox):
        H = self.height
        W = self.width
        D = self.data
        y=[]

        for col in range(W):
            if self.allowsMove(col)==True:
                self.addMove(col, ox)
                if self.winsFor(ox)==True:
                    y.append(col)
                self.delMove(col)
        return y


    def aiMove( self, ox ):
        if self.colsToWin(ox) != []:
            return random.choice(self.colsToWin(ox))
        if ox=="X" and self.colsToWin(ox) == []:
            A = random.choice(self.colsToWin('O'))
            # if A==[]:
            #     A = random.choice(range(self.width))
            #     return A   
            # else: return A   
            return A
        if ox=="O" and self.colsToWin(ox) == []:
            A = self.colsToWin('X')
            if A==[]:
                A = range(self.width)
                return random.choice(A)   
            else: return random.choice(A)  
        else:    
            while True:
                i = random.choice(range(self.width))
                if self.allowsMove(i) == True:
                    return i
                    break


    def hostGame(self):
        print("Welcome to Conect Four!")
        print()
        print(self)
        print()
        while True:
            print()
            P = int(input("X's choice: "))
            while self.allowsMove(P) == False:
                P = int(input("Invalid column chosen. Choose another column: ")) 
            self.addMove(P,'X')


            if self.winsFor('X') == True:
                print(self)
                print()
                print("X wins!!!!")
                break    
            if self.isFull == True:
                print("It's a Tie")
            print(self)
            print()
            

            # Q = self.aiMove("O")
            # while self.allowsMove(Q) == False:
            #     Q = int(input("Invalid column chosen. Choose a column: "))     
            self.addMove(int(self.aiMove("O")), "O")
            if self.winsFor('O') == True: 
                print(self)
                print()
                print('O Wins!!!!')
                break
            if self.isFull == True:
                print("It's a Tie")    
            print(self)

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s


    def oppCh(self):
        """
        This method should return the other kind of checker or playing 
        piece, i.e., the piece being played by self's opponent. 
        In particular, if self is playing 'X', this method returns 'O'
        and vice-versa. 
        """
        if self.ox == "X":
            return "O"
        else:
            return "X"
    
    def scoreBoard(self, b):
        """
        This method should return a single float value representing 
        the score of the input b, which you may assume will be an 
        object of type Board. This should return 100.0 if the board b
        is a win for self. It should return 50.0 if it is neither a 
        win nor a loss for self, and it should return 0.0 if it is 
        a loss for self (i.e., the opponent won).
        """
        if b.winsFor(self.ox) == True and b.winsFor(self.oppCh()) == False:
            return 100.0
        elif b.winsFor(self.ox) == False and b.winsFor(self.oppCh()) == False:
            return 50.0
        elif b.winsFor(self.ox) == False and b.winsFor(self.oppCh()) == True:
            print("WOW")
            return 0.0



    def tiebreakMove(self, scores):
        """
        This method takes in scores, which will be a nonempty list
        of floating-point numbers. If there is only one highest 
        score in that scores list, this method should return its 
        COLUMN number, not the actual score! Note that the column 
        number is the same as the index into the list scores. If 
        there is more than one highest score because of a tie, this 
        method should return the COLUMN number of the highest score 
        appropriate to the player's tiebreaking type. 
        """
        max_num = max(scores)
        max_list = []
        for i in range(len(scores)):
            if scores[i] == max_num:
                max_list.append(i)
        if self.tbt == "LEFT":
            return max_list[0]
        elif self.tbt == "RIGHT":
            return max_list[-1]
        elif self.tbt == "RANDOM":
            return random.choice(max_list)
        

    def scoresFor(self, b):
        """
        This method is the heart of the Player class! Its job is to 
        return a list of scores, with the cth score representing the 
        "goodness" of the input board after the player moves to column c.
        And, "goodness" is measured by what happens in the game after 
        self.ply moves.
        """
        

