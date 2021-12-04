import time , os.path , random , os

def Show_And_Get_Options(Current_Options:dict)->int:
    # This functions accepts a dictionary of the available options and returns the integer (Key) of the option
    # This shows the different options and returns the "Chosen one"
    while True:
        # This loops until the user selects a valid option or throws his system off a cliff
        for key in Current_Options:
            print("{} : {}".format(key , Current_Options[key]))
        print("\n")
        # For loop to loop through the dictionary and display options
        A = int(input("Please choose an option") )
        # Takes an input for option

        # checks if option is valid
        if A in Current_Options:
            return A
        else:
            print("Well looks like you are one of those dumb users we have to be on the lookout for\n ")
            print("----CHOOSE A VALID OPTION-----")
            print("\n")

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        The_Game_Setup()
    elif N==2:
        Read_Scores()
    elif N==3:
        Admin_Controls()
    else:
        if(input("Enter anything if you do not want to exit this godawful game : ")):
            # This line rescursively calls the routing function with the output of the Show_And_Get_Option function
            Routing_function(Show_And_Get_Options(options))
        else:
            # This exits the program , thats it 
            exit("\n-----Reality is often disappointing------\n")
            
def Routing_function_Admin_Controls(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        List_HighScores()
    elif N==2:
        Sort_By_Players()
        pass
    elif N==4:
        Reset_Scores()
    elif N==3:
        List_Players()
    # else:
    #     print("\n----I am to lazy to code edge cases right now----\n")

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
        Games_Played = No_Of_Games_Played()
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
        
        print("\n------Nothing Here yet folks------\n")
        f= open(Scores_File_Path,"a")
        f.write("-------Nothing Here yet folks-------\n")
        f.write("\n")
        f.write(" Users Scores")
        f.close()
def Special_Modify_Scores():
    # After Reset Scores(), this function is used to fill the first 3 lines of the txt files again
    if (os.path.isfile(Scores_File_Path) or os.path.getsize(Scores_File_Path) <2):
        f= open(Scores_File_Path,"a")
        f.write("-------Nothing Here yet folks-------\n")
        f.write("\n")
        f.write(" Users Scores")
        f.close()

    pass
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
                print("\nare you sure you are supposed to be here\n")

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
    print("\n-----H-I-G-H-S-C-O-R-E-S-----\n")

    for i in range(len(Player_Names)):
        print("     {}. {} : {}".format(i+1,Player_Names[i],Player_Scores[i]))
        # This code breaks out of the loop if more 10 scores are already displayed
        if i>8:
            break

def Admin_Controls():
    #This is the function for the admin controls
    
    # This function checks the password ( Only admins are allowed to access this )
    Check_Password()

    print("\nNow you have root access , which in this case gives you the  illusion of choice\n")
    
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
    print("\n----All data has been reset , have a nonconsequential day-----\n")

    # This function is used after reset scores to intialize the txt file again
    Special_Modify_Scores()

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
    print("\nThe number of players is {}\n".format(len(Player_Names)))
    # Printing the list (Player Names)
    print("The players are:")
    for i in range(len(Player_Names)):
        print("{} : {}".format(i+1,Player_Names[i]))

def Sort_By_Players()->None:
    # This function is to sort by player high_scores
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()

    # Stripping the elements of the list containg the txt file of "\n" cuz it causes annoying problems
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')

    # Checking if any data has been entered ( Has the game been played ?)
    if len(Text_Container)<4:
        print("\n---Insufficient Data Entered----\n")
        return None

    # Stripping the list of first  3 lines now the list will contain only the Name Score pair
    L =Text_Container[3:]
    # Initializing the list which is going to contain the player names
    Player_Names = []
    Player_Scores = []

    # Seperating the user name and scores into different lists
    for i in range(len(L)):
        Name_Score = L[i].split()
        Player_Names.append(Name_Score[0])
        Player_Scores.append(int(Name_Score[1]))
    

    # Finding the no of unique names in the list
    Player_Names_Unique = list(set(Player_Names))

    # Initializing a dictionary for storing player highscores
    Player_High_Scores = dict()

    # Loading the unique names into a dictionary with value pairs as 0 
    for i in range(len(Player_Names_Unique)):
        Player_High_Scores[Player_Names_Unique[i]] = 0

    # Passing the empty base dict along with list of player names and scores to another function
    Player_High_Scores = Set_Up_Dict(Player_High_Scores,Player_Names,Player_Scores)
    
    # printing the  highscore per player 
    print("\nThe High Scores for the players are :\n")
    for key in Player_High_Scores:
        print("{} {}".format(key , Player_High_Scores[key]))
    pass

def Set_Up_Dict(Set_Up_Player_High_Scores:dict, Set_Up_Player_Names:list,Set_Up_Player_Scores:list)->dict:
    # Looping through each element of list player names and checking if the corresponding stored value in the dictionary is
    #  greater than what matches is stored in the corresponding list which stores player's scores per game
    # if you are little bit confused with the implementation of it , just let me know - Guru
    for i in range(len(Set_Up_Player_Names)):
            if Set_Up_Player_High_Scores[Set_Up_Player_Names[i]] < Set_Up_Player_Scores[i]:
                Set_Up_Player_High_Scores[Set_Up_Player_Names[i]] =  Set_Up_Player_Scores[i]
            else:
                continue    
    # returning the formatted dictionary
    return Set_Up_Player_High_Scores

def The_Game_Setup():
    # You have finally arrived at the main function that plays the game 

    # Loading the accepted input into a list 
    Accepted_Inputs = ("yes","y","iamalooser")
    # Asking for an input
    Continue_Prompt = input("Please Enter Y/y/yes/iamalooser if you want to play the game")
    # Checking if the entered prompt is not present in the list , if not present the user is kicked out of the function again

    if (Continue_Prompt.lower() not in Accepted_Inputs):
        print("Don't have a good day , have a great day")
        return None

    User_Name =  input("Please Input your name")
    with open (Questions_File_Path, "r") as f:
        Text_Container = f.readlines()
        
    # Stripping the endline character
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')
 
    # using list comprehension to remove the first empty line from the list
    Formatted = [x for x in Text_Container if x]

    # Loading the elements of the list into elements of a dictionary which will be elements of a list
    Questions_List = []
    DictionaryLoader = dict()
    for i in range(0,len(Formatted),7):
        DictionaryLoader["Q"] = Formatted[i]
        DictionaryLoader["Options"] = Formatted[i+1:i+5]
        DictionaryLoader["AnswerKey"] = Formatted[i+5]
        DictionaryLoader["Points"] = int(Formatted[i+6])
        # .copy() is used to dereference the dict pointer , this loads the dict variables into a list  
        Questions_List.append(DictionaryLoader.copy())
    # Questions_List is a list containing dictionaries as its elements  , which contain questions , options etc
    
    # Shuffles the  list containing the questions
    random.shuffle(Questions_List)
    
    # Calling the Game session function to 
    Game_Session(Questions_List,User_Name)

def Game_Session(Q_list:list,User_name:str):
    # This function contains all the game logic that needs to be run for each game session\
    # Asking No of question for the input
    No_Of_Q = int(input("Enter a number below {} for the number of questions you want to play".format(len(Q_list))))
    # Using the while loop to enforce no of questions less than total no of questions

    while (No_Of_Q>len(Q_list)):
        No_Of_Q = int(input("Enter a number below {} for the number of questions you want to play".format(len(Q_list))))

    User_Score = 0

    # for i in range(0,No_Of_Q):
    #     print(i)
        # print(Q_list[i])
    for i in range(No_Of_Q):

        # Printing the Question
        print(Q_list[i]["Q"])

        # Loading the options into a list
        Options_list_temp = Q_list[i]["Options"]
        
        # printing the options
        for j  in range(len(Options_list_temp)):
            print(Options_list_temp[j]) 

        
        Ans = input("Please Enter Your answer")
        if Ans == Q_list[i]["AnswerKey"]:
            User_Score+=Q_list[i]["Points"]
            print("\nYou got it right\n")
    # Getting a normalized function of the score
    User_Score = Normalized_Score(User_Score,No_Of_Q)
    print("You have got {} points !".format(User_Score))

    # Calling function write_scores to display 
    Write_Scores(User_name, User_Score)

def Write_Scores(UserName,UserScore)->None:
    # "This function is to save scores to file"
    with open (Scores_File_Path,"a") as f:
        String_Written = "{} {}".format(UserName,UserScore)
        f.write("\n")
        f.write(String_Written)

    return None

def Normalized_Score(Score:int,No_of_Q:int)->int:
    # Since iam an idiot who makes stuff harder than it has to be , i am adding useless functionality to the thing
    # This function is to normalize the scores since different players might play different amount of games

    # Im bad at math , using basic average and multiplying by 10 to get normalized score of everyone
    Normal_Score = int(round(10*(Score/No_of_Q),0))
    return Normal_Score

def Main():
    # This is the first function that gets called , it provides the options

    print("Welcome to the most useless game you will ever get to play")

    print("Choose from our wide array of options")
    
    
    # Gets option input
    N = Show_And_Get_Options(options)

    # Calls the routing function to get routed to the appropriate function
    Routing_function(N)

def No_Of_Games_Played():
    # "This function is used to find the number of games played and is to be added to the first line of the text file"
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()
    if (len(Text_Container)>3):
        New_List = Text_Container[3:]
    else:
        return 0
    No_of_games_played = len(New_List)
    return No_of_games_played

Questions_File_Path = "Questions.txt"    
Scores_File_Path = "users.txt"
options = dict()
options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}
Password = 3200
Admin_options =   {1:"Sort By High scores",2:"Sort By Player Performance",3:"List Players",4:"Reset Scores",}

# This calls the main function indefinitely 
while True:
    Main() 