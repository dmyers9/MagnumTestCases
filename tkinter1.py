import glob

from tkinter import *

master = Tk()

master.configure(backgroun='light grey')

Label(master, text="Folder Path", backgroun='light grey').grid(row=1)
Label(master, text="/*.txt", backgroun='light grey').grid(row=1, column=3)

Label(master, text="Output File Name", backgroun='light grey').grid(row=3)
Label(master, text=".txt", background='light grey').grid(row=3, column=3)

Label(master, text="Test Cases", background = 'light grey').grid(row=0, column=1)

Label(master, text="", background ='light grey').grid(row=2, column=1)

e1 = Entry(master, width = 80)
e2 = Entry(master, width = 80)

e1.grid(row=1, column=1)
e2.grid(row=3, column=1)


def close_window():
    master.destroy()

def create_file():

    b1.configure(state = DISABLED)
    b1.configure(fg = 'grey')
    
    b2.configure(state = DISABLED)
    b2.configure(fg = 'grey')
    

    folder_path = e1.get()
    print (folder_path)
    output_file_name = e2.get()

    folder_path += "/*.txt"
    output_file_name += ".txt"

    print (folder_path)

    doc = glob.glob(folder_path)

    # Lists that I need to make into a doc file, or just clean up in general
    number_list = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]


    keyword_list = ["able", "access", "add", "adjust", "after", "apply", "assign",
                    "change", "change", "check", "choose", "clear", "click", "close",
                    "commit", "confirm", "configure", "connect", "copy", "create",
                    "delete", "disable", "disconnect", "do", "download",
                    "edit", "enable", "enter", "ensure", "export",
                    "filter", "fire",
                    "go",
                    "hit", "hold",
                    "import", "import/export", "in", "insert", "install", "issue",
                    "load", "locate", "lock", "log", "loggin", "login", "logout",
                    "make",
                    "navigate",
                    "open",
                    "power", "press", "protect", "pull",
                    "reboot", "reconnect", "record", "refresh", "re-load", "reload", "remove",
                    "rename", "repeat", "replace", "reset", "restart", "right-click", "run", 
                    "save", "search", "select", "send", "set", "setup", "shutdown",
                    "specify", "start", "stop", "sudo", "switch",
                    "tap", "then", "toggle", "turn", "type",
                    "undo", "unlock", "unselect", "unset", "upgrade", "upload", "use", "using",
                    "verify",
                    "again,"]

    response_list = ["correctly", "update", "updates", "able", "contains"]

    file = open(output_file_name, "w")

    index = -1



    for z in range(0, len(doc)):  # Goes through every doc in the folder

        actionCount = 0
        responseCount = 0
        count = 0 # for first time writing responses/actions

        tempLine = ""

        with open(doc[z], 'r') as f:
            myFile = [line.strip() for line in f]  # Reads in all the lines and puts them into a list

        for n in range(0, len(myFile)-1):
            myFile[n] = myFile[n].lower()         # Makes all the words lowercase in the list

        ######################
        #   Finding Title    #
        ######################

        for x in range(0, len(myFile[0])):      # Finding where the title starts, and changing the list
            letter = myFile[0][x]
            if letter == ":":
                index = x + 1
                break

        ######################
        #  There is a Title  #
        ######################
        
        if index != 0:

            tempLine = ""
           
            for i in range(index, len(myFile[0])):  # Loop to get rid everything before ":"
                tempLine += myFile[0][i]


            myFile[0] = tempLine    # Making the list take the new title config

            print (myFile)          # Prints the whole text file in console

            file.write(myFile[0]); file.write("\t\t\t\t");  # Writes the title

            # If the document is longer than 3 lines
            if len(myFile) > 3:
            
                for z in range(3, len(myFile)):  # To make sure there is a step
                    if len(myFile[z]) > 0:
                        letter = myFile[z][0]
                        if letter == "#" or letter in number_list:  # If there is a step
                            index = z + 1
                            print ("Index: "); print (index);
                            break
                    else:
                        index = 0

            else:
                index = 0
            


            if (index == 0) or (index > len(myFile)-1): # If ony TITLE
           
                print ("NO") # Title only

                
                words = myFile[0].split()
                

                for w in range(0, len(words)):      # Finding index of keyword/action word
                    if words[w] in keyword_list:
                        index = w
                        break
                
                words1 = [None] * (len(words)-index)

                if index < len(words):
                    print("Action")
                    print(index)
                    print (len(words))
                    for n in range(index, len(words)):
                        words1[n-index] = words[n]


                    print(' '.join(words1))

                file.write(' '.join(words1)); file.write("\t"); file.write("Successful"); file.write("\n");


            # If there are steps/actions  
            else:
                for y in range(index-1, len(myFile)-1):   # going through the rest of the lines
                    words = []
                    print (myFile[y])
                    words = myFile[y].split()
                    print (words)
                    print (len(words))
                    
                    words1 = [None] * (len(words) -1)

                    ############

                    if len(words) > 1:   
                        for a in range(0, len(words)-1):
                            words1[a] = words[a+1]

                        myFile[y] = ' '.join(words1)
                        print(myFile[y])
                        #############

                        if words1[0]:
                            print ("Non-Existent")
                        # print (words[0]) ##
                            if words1[0] in keyword_list:                    # If first word is an action
                                print ("Action")

                                if actionCount == 1 and responseCount == 0:
                                    file.write("Successful"); file.write("\t");
                                    actionCount = 0
                                    responseCount = 0

                                actionCount += 1
                                if count >= 1:
                                    file.write("\n\t\t\t\t");

                                count += 1
                                
                            else:                                           # If first word is not an actio
                                print ("Response")

                                responseCount += 1

                            file.write(myFile[y]); file.write("\t");

                if actionCount == 1 and responseCount == 0:
                    file.write("Successful"); file.write("\t");
                    actionCount = 0
                    responseCount = 0

                file.write("\n")
                    
        else:
                
            print("SHOULD NEVER GET HERE")


    file.close()

    b1.configure(state = NORMAL)
    b1.configure(fg = 'black')
    
    b2.configure(state = NORMAL)
    b2.configure(fg = 'black')


b1 = Button(master, text="Create", command=create_file, width = 10, height = 2)
b1.grid(row=4, column=1)

b2 = Button(master, text="Quit", command=close_window, width = 10, height = 2)
b2.grid(row=5, column=3)


Label(master, text="File will be located in the same file the program is saved in", background= 'light blue').grid(row=5, column=1)
  

mainloop( )
