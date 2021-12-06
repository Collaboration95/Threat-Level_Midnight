
from tkinter import *



root = Tk()

# def Print_Function(a:int):
#     print(a)
def Answers(a:int):
    print(a)
# def Admin_Gui():
#     Admin_root = Tk()

#     for key in Admin_options:
#         MyButton = Button(Admin_root,text="{} : {}".format(key,options[key]))
#         MyButton.pack()
    
#     Admin_root.mainloop()


def Main_GUI():
    for key in options:

        MyButton = Button(root,text="{} : {}".format(key,options[key]),command= lambda: Answers(key))
        MyButton.pack()



    


root.mainloop()

Main_GUI()

options =   {1:"New Games",2:"See Scores",3:"Admin (Top-secrety stuff)",4:"Crawl under a rock for eternity"}
Admin_options =   {1:"Sort By High scores",2:"Sort By Player Performance",3:"List Players",4:"Reset Scores",}
