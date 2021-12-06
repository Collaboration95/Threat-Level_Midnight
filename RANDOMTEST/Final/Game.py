import time , os.path , random , os 
from tkinter import *
from Image_SizeFinder import *
from functools import partial

def Show_And_Get_Options(Current_Options:dict,offset=0)->int:
    # Show_And_Get_Options_GUI_A
    # This function is the gui version of its namesake
    root1 = Tk()
    for key in Current_Options:
        MyButton = Button(root1,text="{} : {}".format(key , Current_Options[key]),command = partial(Show_And_Get_Options_GUI_B,key+offset))
        MyButton.pack()
   
    Mybutton2 = Button(root1,text="Close this",command = root1.destroy)
    Mybutton2.pack()
    root1.mainloop()

def Show_And_Get_Options_GUI_B(Chosen_Option:int):
    # Routing_function(Chosen_Option)
    if Chosen_Option<5:
        Routing_function(Chosen_Option)
    else:
        
        Routing_function_Admin_Controls(Chosen_Option-4)
def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        The_Game_Setup()
    elif N==2:
        Gui_Read_Scores()
    elif N==3:
        Admin_Controls()
    else:
        Gui_Exit_Function()
        # if(input("Enter anything if you do not want to exit this  game : ")):
        #     # This line rescursively calls the routing function with the output of the Show_And_Get_Option function

        #     # This will encounter a massive error in my current system but its all fine and dandy because there is no way for tkinter to give input to access this code
        #     Routing_function(Show_And_Get_Options(options))
        # else:
        #     # This exits the program , thats it 
        #     exit("\n-----Have a good Day------\n")

def Gui_Exit_Function():
    
    # This function is the GUI equivalent of the exit function in the text based program
    exit_root = Tk()
    
    MyLabel = Button(exit_root,text="Are you Sure You want to exit the game")
    MyLabel.pack()

    Mybutton = Button(exit_root,text="Yes",command=Gui_RedButton)
    Mybutton.pack()

    Mybutton2 = Button(exit_root,text="No",command = partial(Show_And_Get_Options,options))
    Mybutton2.pack()

    Mybutton3 = Button(exit_root,text="close this",command = exit_root.destroy)
    Mybutton3.pack()
    exit_root.mainloop()
    pass

def Gui_RedButton():
    root1 = Tk()
    Mylabel = Label(root1,text="For the love of god , do not press that big red button")
    Mylabel.pack()
    Mybutton = Button(root1,text="The big red button",command=exit)
    Mybutton.pack()
    root1.mainloop()
    pass

def Routing_function_Admin_Controls(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        Gui_List_HighScores()
    elif N==2:
        Gui_Sort_By_Players()
        pass
    elif N==4:
        Gui_Reset_Scores()
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

def Gui_Read_Scores():
    
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
        
        root = Tk()
        Mylabel =Label(root,text="The Content of the file is: ")
        Mylabel.pack()
        # Printing the contents of the file
        if (len(Contents)!=0):
            for i in Contents:
                Mylabel1 =Label(root,text=i,anchor=W)
                Mylabel1.pack()
                # print(i)

        
        else:
            Mylabel1 =Label(root,text="---Empty File--- ")
            Mylabel1.pack()
            # print("\n ---Empty File--- \n")
        
        # Get used to these two lines below , they are the lines used to create a button to  close the current window
        Mybutton3 = Button(root,text="close this",command = root.destroy)
        Mybutton3.pack()   
        
        root.mainloop()

    # If file does not exit , this else block creates a file and writes an empty message in it
    else:
        f= open(Scores_File_Path,"a")
        f.write("-------Nothing Here yet folks-------\n")
        f.write("\n")
        f.write(" Users Scores")
        f.close()
        
        root = Tk()
        Mylabel = Label(root,text="------Nothing Here yet folks------")
        Mylabel.pack()
        Mybutton3 = Button(root,text="close this",command = root.destroy)
        Mybutton3.pack()
        root.mainloop()
       
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
        k = int(input("Please enter the password , You extremely clumsy user"))
        if (k!=Password):
            while True:
                # Locks the user/Dumb Admin in an infinite loop
                print("\nare you sure you are supposed to be here\n")
    return None

# def List_HighScores()->None:

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

def Gui_List_HighScores()->None:
    # This function is to list the highscores of those playing the game 

    # Opening the file and loading all the text into a list
    with open (Scores_File_Path, "r") as f:

        Text_Container = f.readlines()
    
    # Stripping the endline character
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')
    
    # Checking if any data has been entered in the file ( if the game has been played atleast once )
    if len(Text_Container)<4:
        root = Tk()
        Mylabel = Label(root,text="----No Data Has Been Entered-----")
        Mylabel.pack()
        root.mainloop()
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
    root = Tk()
    Mylabel = Label(root,text="-----H-I-G-H-S-C-O-R-E-S--")
    Mylabel.pack()
    for i in range(len(Player_Names)):
        Mylabel1 = Label(root,text=" {}. {} : {}".format(i+1,Player_Names[i],Player_Scores[i]))
        Mylabel1.pack()
        # print("     {}. {} : {}".format(i+1,Player_Names[i],Player_Scores[i]))
        # This code breaks out of the loop if more 10 scores are already displayed
        if i>8:
            break
    Mybutton2 = Button(root,text="Close this",command = root.destroy)
    Mybutton2.pack()
    root.mainloop()

def Admin_Controls():
    #This is the function for the admin controls
    
    # This function checks the password ( Only admins are allowed to access this )
    Check_Password()
    root = Tk()
    MyLabel = Label(root,text="Now you have root access , which in this case gives you the  illusion of choice")
    MyLabel.pack()
    MyButton = Button(root,text="Click to Close me & Continue",command=root.destroy)
    MyButton.pack()
    
    
    
    # Notes by the programmer to the programmer:
    # Create a function to rank players by their highscores
    # Create another fucntion to output all the scores of a particular player

    # displays the entire dictionary
    # Getting the chosen option by passing the Admin Option dictionary to the Show and get options function
    Show_And_Get_Options(Admin_options,4)
    root.mainloop()


    # Commenting out all the show and get options since i am directly calling it from the get options function
    # Calling the Routing Function using the Option given by Show and get options function
    # Routing_function_Admin_Controls(Option)

# def Reset_Scores() ->None:
#     # This function can be called by Selecting Admin Controls > Selecting Reset Scores
#     # This function is to reset scores of the game
#     # The code opens the text file in which all the data is stored and writes an empty character instead of it 
#     # Hence Clearing it
#     f = open(Scores_File_Path,"w")
#     f.write("")
#     f.close()
    

#     # This function is used after reset scores to intialize the txt file again
#     Special_Modify_Scores()

#     return None    



def Gui_Reset_Scores()->None:
    # This function is to reset scores of the game
    # The code opens the text file in which all the data is stored and writes an empty character instead of it 
    f = open(Scores_File_Path,"w")
    f.write("")
    f.close()

    Special_Modify_Scores()
    root = Tk()
    Mylabel = Label(root,text="----All data has been reset , have another day-----")
    Mylabel.pack()
    MyButton = Button(root,text="Close this",command = root.destroy)
    MyButton.pack()
    root.mainloop()
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

# def Sort_By_Players()->None:
#     # This function is to sort by player high_scores
#     with open (Scores_File_Path, "r") as f:
#         Text_Container = f.readlines()

#     # Stripping the elements of the list containg the txt file of "\n" cuz it causes annoying problems
#     for i in range(len(Text_Container)):
#         Text_Container[i]=Text_Container[i].strip('\n')

#     # Checking if any data has been entered ( Has the game been played ?)
#     if len(Text_Container)<4:
#         print("\n---Insufficient Data Entered----\n")
#         return None

#     # Stripping the list of first  3 lines now the list will contain only the Name Score pair
#     L =Text_Container[3:]
#     # Initializing the list which is going to contain the player names
#     Player_Names = []
#     Player_Scores = []

#     # Seperating the user name and scores into different lists
#     for i in range(len(L)):
#         Name_Score = L[i].split()
#         Player_Names.append(Name_Score[0])
#         Player_Scores.append(int(Name_Score[1]))
    

#     # Finding the no of unique names in the list
#     Player_Names_Unique = list(set(Player_Names))

#     # Initializing a dictionary for storing player highscores
#     Player_High_Scores = dict()

#     # Loading the unique names into a dictionary with value pairs as 0 
#     for i in range(len(Player_Names_Unique)):
#         Player_High_Scores[Player_Names_Unique[i]] = 0

#     # Passing the empty base dict along with list of player names and scores to another function
#     Player_High_Scores = Set_Up_Dict(Player_High_Scores,Player_Names,Player_Scores)
    
#     # printing the  highscore per player 
#     print("\nThe High Scores for the players are :\n")
#     for key in Player_High_Scores:
#         print("{} {}".format(key , Player_High_Scores[key]))
#     pass


def Gui_Sort_By_Players()->None:
    # This function is to sort by player high_scores
    with open (Scores_File_Path, "r") as f:
        Text_Container = f.readlines()

    # Stripping the elements of the list containg the txt file of "\n" cuz it causes annoying problems
    for i in range(len(Text_Container)):
        Text_Container[i]=Text_Container[i].strip('\n')
    # Checking if any data has been entered ( Has the game been played ?)
    
    
    if len(Text_Container)<4:
        root = Tk()
        Mylabel = Label(root,text="--Insufficient Data Entered----")
        Mylabel.pack()
        MyButton = Button(root,text="Close this prompt",commmand = root.destroy)
        MyButton.pack()
        root.mainloop
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
    
    root = Tk()
    # printing the  highscore per player
    # Mylabel =Label(root,text="The High Scores for the players are : ")
    # Mylabel.pack()

    print("\nThe High Scores for the players are :\n")
    # for key in Player_High_Scores:
    #     Mylabel1 = Label(root,text ="{} {}".format(key , Player_High_Scores[key]))
    #     Mylabel1.pack()

    MyButton = Button(root,text="Close this prompt",commmand = root.destroy)
    MyButton.pack()
    root.mainloop()


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
    for i in range(0,len(Formatted),8):
        DictionaryLoader["Q"] = Formatted[i]
        DictionaryLoader["Options"] = Formatted[i+1:i+5]
        DictionaryLoader["AnswerKey"] = Formatted[i+5]
        DictionaryLoader["Points"] = int(Formatted[i+6])
        DictionaryLoader["File_Path"] = Formatted[i+7]
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


        
        
        # checks if the file path exists
       
    
        if (os.path.isfile(Q_list[i]["File_Path"])):
            # Tkinter has this awesome feature where you cannot automatically close the windows with a timer , time.sleep() freezes the whole program 
  
            # This is the code for presenting the image 
            root = Tk()
            # this code basically calls the a function that i found on the internet to find the image size 
            ImageSize = [0,0]
            ImageSize[0] , ImageSize[1]= get_image_size(Q_list[i]["File_Path"])

            # Creating a "canvas"   
            canv = Canvas(root, width=ImageSize[0], height=ImageSize[1], bg='white')
            canv.pack()
            # Variable for the image
            img = PhotoImage(file=Q_list[i]["File_Path"])
            
            # Allocating the image in the canvas and anchoring it to the top left
            canv.create_image(0,0, anchor="nw", image=img)

            # Creating a button to ease the closing of the function
            MyButton = Button(root,text="Close Window Before Entering Input",command=root.destroy)
            MyButton.pack()

            # basically like an even listener ( a program constantly running in the background waiting for button clicks and stuff)
            root.mainloop()
        else:
            print("\n Oh No ! , there is no image for this question\n")

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

    
    Show_And_Get_Options(options)

    # Calls the routing function to get routed to the appropriate function
    # Commenting all the show and get options right now since i am directly calling that 
    # Routing_function(N)

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

Questions_File_Path = "Final/Resources/Questions.txt"    
Scores_File_Path = "Final/Resources/users.txt"
options = dict()
options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}
Password = 3200
Admin_options =   {1:"Sort By High scores",2:"Sort By Player Performance",3:"List Players",4:"Reset Scores",}

# This calls the main function indefinitely 
# while True:
#     Main() 
Main()