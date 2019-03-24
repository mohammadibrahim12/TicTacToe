
def checkwin (string1, string2, string3, count):
    #gets passed in game lists containing player moves, checks if there is a winner or a tie then returns appropiate message and True, otherwise return False

    if string1[2] == string2[2] == string3[2] == "X" or string1[8] == string2[8] == string3[8] == "X" or string1[14] == string2[14] == string3[14] == "X":
        return ["PLAYER 2(X) WON", True]
    elif string1[2] == string2[2] == string3[2] == "O" or string1[8] == string2[8] == string3[8] == "O" or string1[14] == string2[14] == string3[14] == "O":
        return ["PLAYER 1(O) WON", True]
    elif string1[2] == string1[8] == string1[14] == "X" or string2[2] == string2[8] == string2[14] == "X" or string3[2] == string3[8] == string3[14] == "X":
        return ["PLAYER 2(X) WON", True]
    elif string1[2] == string1[8] == string1[14] == "O" or string2[2] == string2[8] == string2[14] == "O" or string3[2] == string3[8] == string3[14] == "O":
        return ["PLAYER 1(O) WON", True]
    elif string1[2] == string2[8] == string3[14] == "X" or string1[14] == string2[8] == string3[2] == "X":
        return ["PLAYER 2(X) WON", True]
    elif string1[2] == string2[8] == string3[14] == "O" or string1[14] == string2[8] == string3[2] == "O":
        return ["PLAYER 1(O) WON", True]
    elif count < 9:
        return ["", False]
    else:
        return ['ITS A TIE', True]


def replacer(string, location, xoro):
    #Replaces numbers in the game board lists with X or O according to player and returns true, if user enters an invalid choice returns false and prints message
    #location variable represents where in the list the X or O needs to be placed, can be one of index 2, 8 , or 14 of the list 
   if string[location] == "X" or string [location] == "O":
       print ("Slot taken, pick again.")
       return False
   elif xoro == 1:
       string[location] = "O"
       return True
   else:
       string[location] = "X"
       return True


def print_game (list1, list2, list3):
    #prints the game, uses the passed in updated lists of the game board, along with pre determined vertical and horizontal lines to build board

    verticals = "     |     |     "
    horizontal = "----- ----- -----"

    #passed in lists must be converted to strings in order to print correctly 
    string1 = "".join(list1)
    string2 = "".join(list2)
    string3 = "".join(list3)

    #passed in lists containing user choices along with vertical and horizontal strings are organized in list to be printed
    listgame =  ["\n", verticals, string1, verticals, horizontal, verticals, string2, verticals, horizontal, verticals, string3, verticals, "\n"]
   
    #game board is printed, going through each variable in list
    for x in listgame:
        print(x)

def postion(pos, player):
    #Based on player, calls replacer function to replace game lists with the appropriate X or O based on the user input (1-9) 
    if player == 1: 
        if pos == 1:
            return replacer(gamelist1, 2, 1)
        elif pos == 2:
            return replacer(gamelist1, 8, 1)
        elif pos == 3:
            return replacer(gamelist1, 14, 1)
        elif pos == 4:
            return replacer(gamelist2, 2, 1)
        elif pos == 5:
            return replacer(gamelist2, 8, 1)
        elif pos == 6:
            return replacer(gamelist2, 14, 1)
        elif pos == 7:
            return replacer(gamelist3, 2, 1)
        elif pos == 8:
            return replacer(gamelist3, 8, 1)
        elif pos == 9:
            return replacer(gamelist3, 14, 1)
        else:
            return False 
    else:
        if pos == 1:
            return replacer(gamelist1, 2, 2)
        elif pos == 2:
            return replacer(gamelist1, 8, 2)
        elif pos == 3:
            return replacer(gamelist1, 14, 2)
        elif pos == 4:
            return replacer(gamelist2, 2, 2)
        elif pos == 5:
            return replacer(gamelist2, 8, 2)
        elif pos == 6:
            return replacer(gamelist2, 14, 2)
        elif pos == 7:
            return replacer(gamelist3, 2, 2)
        elif pos == 8:
            return replacer(gamelist3, 8, 2)
        elif pos == 9:
            return replacer(gamelist3, 14, 2)
        else:
            return False    
    
#Lists where the users choices (either X or O will go, currently numbered so that user can choose, each number represents box in 3 x 3 set)
gamelist1 = [" ", " ", "1", " ", " ", "|", " ", " ", "2", " ", " ", "|", " ", " ", "3", " ", " "]
gamelist2 = [" ", " ", "4", " ", " ", "|", " ", " ", "5", " ", " ", "|", " ", " ", "6", " ", " "]
gamelist3 = [" ", " ", "7", " ", " ", "|", " ", " ", "8", " ", " ", "|", " ", " ", "9", " ", " "]

#counter to count number of moves that have been made
count = 0 

#start of game, prints initial game board 
print_game(gamelist1, gamelist2, gamelist3)


#start game 
while True :

    #check if input is valid 
    valid = False
    #so long as input is invalid keep asking user 
    while not valid:
        try:
            #Ask user to enter an integer between 1-9
            player1 = int(input("PLAYER 1 (O) Where do you want to make your move (1-9): "))
            #raises and exception if something other than an integer between 1 and 9 was entered
            if player1 not in range (1,10):
                raise Exception
            #Calls function to modify game board with user choice, also returns whether a valid input was submitted
            valid = postion(player1, 1)
            #increase move counter
            count = count + 1 
        except Exception:
            #If user enters a non integer or a number not between 1 and 9, catches the error and prints out message
            print ("Must be a NUMBER between 1 and 9, pick again")
    
    #Print updated game board
    print_game(gamelist1, gamelist2, gamelist3)

    #Check if someone won or tied, if they did print the associated message and break out of the loop ending the game
    if checkwin(gamelist1, gamelist2, gamelist3, count)[1]:
        print (checkwin(gamelist1, gamelist2, gamelist3, count)[0])
        break

    #Player two now makes a move, steps are the same, valid set back to false as input must be checked again
    valid = False
    while not valid:
        try:
            player2 = int(input("PLAYER 2 (X) Where do you want to make your move (1-9): "))
            if player2 not in range (0,10):
                raise Exception
            valid = postion(player2, 2)
            count = count + 1 
        except Exception:
            print ("Must be a NUMBER between 1 and 9, pick again")

    print_game(gamelist1, gamelist2, gamelist3)

    if checkwin(gamelist1, gamelist2, gamelist3, count)[1]:
        print (checkwin(gamelist1, gamelist2, gamelist3, count)[0])
        break
        



        


    




