import time , os.path
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
            print("CHOOSE A VALID OPTION")

def Read_Scores():
    # This function is to read the scores of the users stored in a text file named users_scores.txt
    #It is located under 2.0 in the menu

    # This function checks for file path and reads scores from file path
    if (os.path.isfile("users.txt")):
            with open('users.txt') as f: 
                for i in f:
                    print(i)
            f.close()
    

    # If file does not exit , this else block creates a file and writes an empty message in it
    else:
        print("Nothing Here yet folks")
        f= open("users.txt","w+")
        f.write("-------Nothing Here yet folks-------")
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
    f = open("users.txt","w")
    f.write("")
    f.close()
    print("All data has been reset , have a nonconsequential day")
    return None
    


def Routing_function_Admin_Controls(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        pass
    elif N==2:
        pass
    elif N==3:
        Reset_Scores()
    else:
        print("I am to lazy to code edge cases right now")

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
            exit("Reality is often disappointing")

def Main():
    # This is the first function that gets called , it provides the options

    print("Welcome to the most useless game you will ever get to play ")

    print("Choose from our wide array of options")
    
    
    # Gets option input
    N = Show_And_Get_Options(options)

    # Calls the routing function to get routed to the appropriate function
    Routing_function(N)

options = dict()
options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}
Password = 3200
Admin_options =   {1:"Sort By High scores",2:"Sort By Player Performance",3:"Reset Scores"}
# This calls the main function indefinitely 
while True:
    Main()