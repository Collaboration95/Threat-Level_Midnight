import time , os.path
def Show_And_Get_Options():
    # This shows the different options and returns the "Chosen one"
    while True:
        # This loops until the user selects a valid option or throws his system off a cliff
        for key in options:
            print(key , options[key])
        # For loop to loop through the dictionary and display options
        A = int(input("Please choose an option") )
        # Takes an input for option
        
        # checks if option is valid
        if A in options:
            return A
        else:
            print("Well looks like you are one of those dumb users we have to be on the lookout for\n ")
            print("CHOOSE A VALID OPTION")

def Read_Scores():
    # This function is to read the scores of the users stored in a text file named users_scores.txt
    #It is located under 2.0 in the menu

    # This function checks for file path and reads scores from file path
    if (os.path.isfile("CDTASSIGNMENT/users.txt")):
            with open('CDTASSIGNMENT/users.txt') as f: 
                for i in f:
                    print(i)
            f.close()


    # If file does not exit , this else block creates a file and writes an empty message in it
    else:

        f= open("CDTASSIGNMENT/users.txt","w+")
        f.write("Nothing Here yet folks")
        f.close()

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        pass
    elif N==2:
        Read_Scores()
    elif N==3:
        pass
    else:
        if(input("Enter anything if you do not want to exit this godawful game")):
            exit()
        else:
            # This line rescursively calls the routing function with the output of the Show_And_Get_Option function
            Routing_function(Show_And_Get_Options)

def Main():
    # This is the first function that gets called , it provides the options

    print("Welcome to the most useless game you will ever get to play ")

    print("Choose from our wide array of options")
    
    
    # Gets option input
    N = Show_And_Get_Options()

    # Calls the routing function to get routed to the appropriate function
    Routing_function(N)

options = dict()
options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}


# This calls the main function indefinitely 
while True:
    Main()