import time , os.path
import os    

def Show_And_Get_Options(Current_Options:dict)->int:
    # This functions accepts a dictionary of the available options and returns the integer (Key) of the option
    # This shows the different options and returns the "Chosen one"
    while True:
        # This loops until the user selects a valid option or throws his system off a cliff
        for key in Current_Options:
            print("{} : {}".format(key , Current_Options[key]))
        # For loop to loop through the dictionary and display options
        A = int(input("Please choose an option") )
        # Takes an input for option
        
        # checks if option is valid
        if A in Current_Options:
            return A
        else:
            print("Well looks like you are one of those dumb users we have to be on the lookout for\n ")
            print("----CHOOSE A VALID OPTION-----")

def Read_Scores():
    # This function is to read the scores of the users stored in a text file named users_scores.txt
    #It is located under 2.0 in the menu

    # This if block checks if path exists and that file is not empty
    if (os.path.isfile(Scores_File_Path) and os.path.getsize(Scores_File_Path) > 0):
            
        with open(Scores_File_Path, "r") as f: 
            # Loading the contents of the files into a list
            Contents = f.readlines()
    

        Written_to_File = Contents
        # Calling the games played function to find out number of lines  of user input data
        Games_Played = No_Of_Players()
        # Changing only the first line of the text file
        Written_to_File[0] = "The number of games played is {} \n".format(Games_Played)

        # Opening and updating textfile with new contents
        f= open(Scores_File_Path,"w+")
        f.writelines(Written_to_File)
        f.close()

        # Somehow there exists a magical "\n" at the end of each line and the for loop also adds another endline , 
        # to avoid that im stripping "\n"
        for i in range(len(Contents)):
            Contents[i]=Contents[i].strip('\n')
        # Checking if there is anything in the file
        

        # Printing the contents of the file
        if (len(Contents)!=0):
            for i in Contents:
                print(i)
        else:
            print("\n ---Empty File--- \n")
            
    

    # If file does not exit , this else block creates a file and writes an empty message in it
    else:
        print("------Nothing Here yet folks------")
        f= open(Scores_File_Path,"a")
        f.write("-------Nothing Here yet folks-------\n")
        f.write("\n")
        f.write(" Users Scores")
        
        f.close()

def Check_Password():
    # The Below block of code checks for the correct password and locks the user  
    # if password is twice in a row

    # For password , see variable below ( like wayy below) 
    k = int(input("Please enter the password"))
    if (k != Password):
        k = int(input("Please enter the password , YOU MORON"))
        if (k!=Password):
            while True:
                # Locks the user/Dumb Admin in an infinite loop
                print("are you sure you are supposed to be here")

def List_HighScores()->None:
    # This function is to list the highscores of those playing the game 

    # Opening the file and loading all the text into a list
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()
    
    # Stripping the endline character
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')
    
    # Checking if any data has been entered in the file ( if the game has been played atleast once )
    if len(Text_Container)<4:
        print("\n---No Data has been entered----\n")
        return None
    
    #Creating a new list with text starting from the 4th line of the text file
    L =Text_Container[3:]
    
    # Initializing the list which is going to contain the player names
    Player_Names = []
    
    # Initializing the list in which player scores are going
    Player_Scores = []

    # Using the split function to everyline into player name and scores , and appending player name to a new list
    for i in range(len(L)):
        Name_Score = L[i].split()
        Player_Names.append(Name_Score[0])
        Player_Scores.append(int(Name_Score[1]))


    # Using Bubble sort to arrange scores in descending order
    for i in range(len(Player_Scores)):
        for j in range(len(Player_Scores)-1):
            if Player_Scores[j]<Player_Scores[j+1]:
                Player_Scores[j],Player_Scores[j+1] = Player_Scores[j+1] , Player_Scores[j]
            # Swapping player names also so as no not get data mismatched
                Player_Names[j],Player_Names[j+1] = Player_Names[j+1] , Player_Names[j]


    # Printing the list (Player Names)
    print("-----H-I-G-H-S-C-O-R-E-S-----\n")

    for i in range(len(Player_Names)):
        
        print("     {}. {} : {}".format(i+1,Player_Names[i],Player_Scores[i]))

        # This code breaks out of the loop if more 10 scores are already displayed
        if i>8:
            break

def Admin_Controls():
    #This is the function for the admin controls
    
    # This function checks the password ( Only admins are allowed to access this )
    Check_Password()

    print("Now you have root access , which in this case gives you access to a wide variety of admin only tools like the illusion of choice")
    
    # Notes by the programmer to the programmer:
    # Create a function to rank players by their highscores
    # Create another fucntion to output all the scores of a particular player

    # displays the entire dictionary
    # Getting the chosen option by passing the Admin Option dictionary to the Show and get options function
    Option = Show_And_Get_Options(Admin_options)
    # Calling the Routing Function using the Option given by Show and get options function
    Routing_function_Admin_Controls(Option)

def Reset_Scores() ->None:
    # This function can be called by Selecting Admin Controls > Selecting Reset Scores
    # This function is to reset scores of the game
    # The code opens the text file in which all the data is stored and writes an empty character instead of it 
    # Hence Clearing it
    f = open(Scores_File_Path,"w")
    f.write("")
    f.close()
    print("----All data has been reset , have a nonconsequential day-----")
    return None    

def List_Players():
    # Opening the file and loading all the text into a list
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()
    # Stripping the endline character
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')
    if len(Text_Container)<4:
        print("\n---No Data has been entered----\n")
        return None
    #Creating a new list with text starting from the 4th line of the text file
    L =Text_Container[3:]
    # Initializing the list which is going to contain the player names
    Player_Names = []

    # Using the split function to everyline into player name and scores , and appending player name to a new list
    for i in range(len(L)):
        Name_Score = L[i].split()
        Player_Names.append(Name_Score[0])

    # Converting the list into set to destroy duplicate elements and converting back into list
    Player_Names = list(set(Player_Names))

    # finding no of players by the length of the list 
    print("The number of players is {}".format(len(Player_Names)))
    # Printing the list (Player Names)
    print("The players are:")
    for i in range(len(Player_Names)):
        print("{} : {}".format(i+1,Player_Names[i]))

def Routing_function_Admin_Controls(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        List_HighScores()
    elif N==2:
        pass
    elif N==4:
        Reset_Scores()
    elif N==3:
        List_Players()
    else:
        print("----I am to lazy to code edge cases right now----")

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        print("Code under construction")
    elif N==2:
        Read_Scores()
    elif N==3:
        Admin_Controls()
    else:
        if(input("Enter anything if you do not want to exit this godawful game")):
            # This line rescursively calls the routing function with the output of the Show_And_Get_Option function
            Routing_function(Show_And_Get_Options(options))
        else:
            # This exits the program , thats it 
            exit("-----Reality is often disappointing------")

def Main():
    # This is the first function that gets called , it provides the options

    print("Welcome to the most useless game you will ever get to play")

    print("Choose from our wide array of options")
    
    
    # Gets option input
    N = Show_And_Get_Options(options)

    # Calls the routing function to get routed to the appropriate function
    Routing_function(N)
def No_Of_Players():
    "This function is used to find the number of games played and is to be added to the first line of the text file"
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()
    if (len(Text_Container)>4):
        New_List = Text_Container[3:]
    else:
        return 0
    No_of_games_played = len(New_List)
    return No_of_games_played
Scores_File_Path = "users.txt"
options = dict()
options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}
Password = 3200
Admin_options =   {1:"Sort By High scores",2:"Sort By Player Performance",3:"List Players",4:"Reset Scores",}

# This calls the main function indefinitely 
while True:
    Main()