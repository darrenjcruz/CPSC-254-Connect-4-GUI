import connectfour
import tkinter
from tkinter import *  
from PIL import ImageTk,Image 
import random
import sqlite3

_DEFAULT_FONT = ('Helvetica', 20)
COLORS = ["purple", "blue", "green", "orange", 'black']
COLOR = random.choice(COLORS)

class ConnectFourApp:
    
    def __init__(self):
        #ConnectFour Object
        self._ConnectFour = connectfour.ConnectFour()
        self._playerOne = ""
        self._playerTwo = ""

        #Tkinter Gui
        self._root_window = tkinter.Tk()
        self._root_window.geometry("960x1000")
        self._root_window.resizable(width = False, height = False)
        self._root_window.title("Connect Four")
        
        #creating label widget 
        welcomeTitle = tkinter.Label(self._root_window, text = "Welcome to our Connect Four app!")
        welcomeTitle.place(x = 410, y = 500)
        enterButton = tkinter.Button(self._root_window, text = "Enter The App",
                                    padx = 50, pady = 5, fg = "yellow", bg = "red",
                                    font = 15, command = self.mainMenu)
        enterButton.place(x = 400, y = 550)


    def mainMenu(self):
        '''
        Presents a menu for the user to navigate through.
        '''
        #This clears the screen so the new info can be displayed by itself 
        for widgets in self._root_window.winfo_children():
            widgets.destroy()

        #Buttons
        tutorialButton = tkinter.Button(self._root_window, text = "Tutorial",
                                    padx = 50, pady = 5, fg = "yellow", bg = "red",
                                    font = 15, command = self.tutorialButton)
        tutorialButton.place(x = 420, y = 450, width=150)
        playButton = tkinter.Button(self._root_window, text = "Play",
                                    padx = 50, pady = 5, fg = "yellow", bg = "red",
                                    font = 15, command = self.playButton)
        playButton.place(x = 420, y = 500, width=150)
        leaderboardButton = tkinter.Button(self._root_window, text = "Leaderboard",
                                    padx = 50, pady = 5, fg = "yellow", bg = "red",
                                    font = 15, command = self.leaderboardButton)
        leaderboardButton.place(x = 420, y = 550, width=150)
        exitButton = tkinter.Button(self._root_window, text = "Exit",
                                    padx = 50, pady = 5, fg = "yellow", bg = "red",
                                    font = 15, command = self.exitButton)
        exitButton.place(x = 420, y = 600, width=150)

        #Create leaderboard database if it doesn't exist yet
        connectToDatabase = sqlite3.connect("leaderboard.db")
        cursorForDatabase = connectToDatabase.cursor()
        cursorForDatabase.execute("CREATE TABLE IF NOT EXISTS leaderboard (userName text, winCount integer)")
        connectToDatabase.commit()
        connectToDatabase.close()


        # Create Submit Player 1 Function for database
        def submit_player_one():
            '''
            Enters Player one's name into the leaderboard with 0 wins and sets Player one's name in class object
            '''
            # Create a database or connect to one
            connectToDatabase = sqlite3.connect('leaderboard.db')

            # Create a database cursor
            cursorForDatabase = connectToDatabase.cursor()

            self._playerOne = playerOneEntry.get().strip()

            # Insert into table
            cursorForDatabase.execute("SELECT * FROM leaderboard WHERE (userName = ?)", (self._playerOne,))
            entry = cursorForDatabase.fetchone()

            if entry is None:
                cursorForDatabase.execute("INSERT INTO leaderboard (userName, winCount) VALUES(?, ?)", (self._playerOne, 0))

            # Commit changes
            connectToDatabase.commit()

            # Close connection
            connectToDatabase.close()

            playerOneEntry.delete(0, END)
            
            return


        # Create Submit Player 2 Function for database
        def submit_player_two():
            '''
            Enters Player two's name into the leaderboard with 0 wins and sets Player two's name in class object
            '''

            # Create a database or connect to one
            connectToDatabase = sqlite3.connect('leaderboard.db')

            # Create a database cursor
            cursorForDatabase = connectToDatabase.cursor()

            self._playerTwo = playerTwoEntry.get().strip()

            # Insert into table
            cursorForDatabase.execute("SELECT * FROM leaderboard WHERE (userName = ?)", (self._playerTwo,))
            entry = cursorForDatabase.fetchone()

            if entry is None:
                cursorForDatabase.execute("INSERT INTO leaderboard (userName, winCount) VALUES(?, ?)", (self._playerTwo, 0))
            # Commit changes
            connectToDatabase.commit()

            # Close connection
            connectToDatabase.close()

            playerTwoEntry.delete(0, END)

            return


        #Player One entry
        playerOneEntry = tkinter.Entry(self._root_window, width=30)
        playerOneEntry.place(x = 240, y = 525, width=150)
        playerOneLabel = tkinter.Label(self._root_window, text="Player 1")
        playerOneLabel.place(x = 240, y = 500, width=150)
        playerOneButton = tkinter.Button(self._root_window, text = "Submit", padx = 50, pady=5,
                                    fg = "yellow", bg = "red", font = 15, command = submit_player_one)
        playerOneButton.place(x = 240, y = 550, width=150)

        #Player Two entry
        playerTwoEntry = tkinter.Entry(self._root_window, width=30)
        playerTwoEntry.place(x = 600, y = 525, width=150)
        playerTwoLabel = tkinter.Label(self._root_window, text="Player 2")
        playerTwoLabel.place(x = 600, y = 500, width=150)
        playerTwoButton = tkinter.Button(self._root_window, text = "Submit", padx = 50, pady=5,
                                    fg = "yellow", bg = "red", font = 15, command = submit_player_two)
        playerTwoButton.place(x = 600, y = 550, width=150)

        return

        
    def exitButton(self):
        '''
        Exits the ConnectFour App
        '''
        for widgets in self._root_window.winfo_children():
            widgets.destroy()  
        quit()
        return


    def nextButton(self):
        '''
        Next button for Tutorial Page
        '''
        for widgets in self._root_window.winfo_children():
            widgets.destroy()  
        self.mainMenu()

        return


    def previousButton(self):
        '''
        Previous button for Tutorial Page
        '''
        for widgets in self._root_window.winfo_children():
            widgets.destroy()
        self.mainMenu()

        return
        

    def tutorialButton(self):
        '''
        Takes the user to a tutorial page
        '''
        def pic2():
            '''
            clears the screen and displays picture 2
            '''
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic3)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= self.tutorialButton)
            self.previousButton.pack()
            TutorialMessage2 = tkinter.Label(self._root_window, text="You can check the leaderboard to see who has the most wins! ")
            TutorialMessage2.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img2 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep2.png"))
            img2label = Label(self._root_window, image = img2, width=850, height=870)
            img2label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img2)

            return


        def pic3():
            '''
            clears the screen and displays picture 3
            '''
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic4)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic2)
            self.previousButton.pack()
            TutorialMessage3 = tkinter.Label(self._root_window, text="Click on Play to start the game! ")
            TutorialMessage3.pack()
            
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img3 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep3.png"))
            img3label = Label(self._root_window, image = img3, width=850, height=870)
            img3label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img3)

            return


        def pic4():
            '''
            clears the screen and displays picture 4
            '''
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic5)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic3)
            self.previousButton.pack()
            TutorialMessage4 = tkinter.Label(self._root_window, text="Click on the column you want to drop your piece in! ")
            TutorialMessage4.pack()
            
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img4 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep4.png"))
            img4label = Label(self._root_window, image = img4, width=850, height=870)
            img4label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img4)

            return

        def pic5():
            '''
            clears the screen and displays picture 5
            '''
            for widgets in self._root_window.winfo_children():
                widgets.destroy()

            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic6)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic4)
            self.previousButton.pack()
            TutorialMessage5 = tkinter.Label(self._root_window, text="If you want to exit the game, click the return to main menu button. ")
            TutorialMessage5.pack()
            
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img5 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep5.png"))
            img5label = Label(self._root_window, image = img5, width=850, height=870)
            img5label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img5)  
            
            return

        def pic6():
            '''
            clears the screen and displays picture 6
            '''
            for widgets in self._root_window.winfo_children():
                widgets.destroy()

            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic7)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic5)
            self.previousButton.pack()
            TutorialMessage6 = tkinter.Label(self._root_window, text="If you want to reset the game, click the reset button. ")
            TutorialMessage6.pack()
            
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img6 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep6.png"))
            img6label = Label(self._root_window, image = img6, width=850, height=870)
            img6label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img6) 
            
            return


        def pic7():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic8)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic6)
            self.previousButton.pack()
            TutorialMessage7 = tkinter.Label(self._root_window, text="If you want to change the color of the frame, click the change background button. ")
            TutorialMessage7.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img7 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep7.png"))
            img7label = Label(self._root_window, image = img7, width=850, height=870)
            img7label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img7) 

        def pic8():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic9)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic7)
            self.previousButton.pack()
            TutorialMessage8 = tkinter.Label(self._root_window, text="Red will start first, and then it will alternate between the two colors. ")
            TutorialMessage8.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img8 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep8.png"))
            img8label = Label(self._root_window, image = img8, width=850, height=870)
            img8label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img8) 

        def pic9():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic10)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic8)
            self.previousButton.pack()
            TutorialMessage9 = tkinter.Label(self._root_window, text="The game will end when one of the players has 4 in a row. ")
            TutorialMessage9.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img9 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep9.png"))
            img9label = Label(self._root_window, image = img9, width=850, height=870)
            img9label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img9) 

        def pic10():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic11)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic9)
            self.previousButton.pack()
            TutorialMessage10 = tkinter.Label(self._root_window, text="The winner will be announced at the end of the game. The game can be reset to play again.")
            TutorialMessage10.pack()
            TutorialMessage10_2 = tkinter.Label(self._root_window, text="The leaderboard will be updated with the new winner.")
            TutorialMessage10_2.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img10 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep10.png"))
            img10label = Label(self._root_window, image = img10, width=850, height=870)
            img10label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img10)   

        def pic11():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic12)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic10)
            self.previousButton.pack()
            TutorialMessage11 = tkinter.Label(self._root_window, text="If there is a tie, the game will end in a draw. ")
            TutorialMessage11.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img11 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep11.png"))
            img11label = Label(self._root_window, image = img11, width=850, height=870)
            img11label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img11)         

        def pic12():
            #clears the screen and prints out the next picture
            for widgets in self._root_window.winfo_children():
                widgets.destroy()
            self.nextButton = tkinter.Button(self._root_window, text="Previous ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic11)
            self.nextButton.pack()
            self.previousButton = tkinter.Button(self._root_window, text="Exit ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= self.mainMenu)
            self.previousButton.pack()
            TutorialMessage12 = tkinter.Label(self._root_window, text="You can reset as many times as you want to rack up wins on the leaderboard! ")
            TutorialMessage12.pack()
            #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
            img12 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep12.png"))
            img12label = Label(self._root_window, image = img12, width=850, height=870)
            img12label.pack()
            self._canvas.create_image(20, 20, anchor=NW, image=img12)

        for widgets in self._root_window.winfo_children():
            widgets.destroy()
            
        self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic2)
        self.nextButton.pack()
        self.previousButton = tkinter.Button(self._root_window, text="Exit ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= self.mainMenu)
        self.previousButton.pack()
        TutorialMessage1 = tkinter.Label(self._root_window, text="Welcome to the tutorial for Connect Four! You will be presented with a series of pictures that will explain the rules of the game ")
        TutorialMessage1.pack()
        TutorialMessage1_2 = tkinter.Label(self._root_window, text="You will be presented with a series of pictures that will explain the rules of the game")
        TutorialMessage1_2.pack()
        TutorialMessage1_3 = tkinter.Label(self._root_window, text="You are able to input the player names in these entry boxes ")
        TutorialMessage1_3.pack()
        
        #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
        img1 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep1.png"))
        img1label = Label(self._root_window, image = img1, width=850, height=870)
        img1label.pack()
        self._canvas.create_image(20, 20, anchor=NW, image=img1)
        
        return

        for widgets in self._root_window.winfo_children():
            widgets.destroy()
            
        self.nextButton = tkinter.Button(self._root_window, text="Next ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= pic2)
        self.nextButton.pack()
        self.previousButton = tkinter.Button(self._root_window, text="Exit ", padx=50, pady=5, fg="yellow", bg="red", font=15, command= self.mainMenu)
        self.previousButton.pack()
        TutorialMessage1 = tkinter.Label(self._root_window, text="Welcome to the tutorial for Connect Four! You will be presented with a series of pictures that will explain the rules of the game ")
        TutorialMessage1.pack()
        TutorialMessage1_2 = tkinter.Label(self._root_window, text="You will be presented with a series of pictures that will explain the rules of the game")
        TutorialMessage1_2.pack()
        TutorialMessage1_3 = tkinter.Label(self._root_window, text="You are able to input the player names in these entry boxes ")
        TutorialMessage1_3.pack()
        
        #This is how images are printed out to the GUI, the pack is what prints it out onto the stack
        img1 = ImageTk.PhotoImage(Image.open("ProjectTutorialStep1.png"))
        img1label = Label(self._root_window, image = img1, width=850, height=870)
        img1label.pack()
        self._canvas.create_image(20, 20, anchor=NW, image=img1)
        
        return


    def playButton(self):
        '''
        Displays the game
        '''
        for widgets in self._root_window.winfo_children():
            widgets.destroy()
        self.game()

        return

    def leaderboardButton(self):
        '''
        Takes the user to a leaderboard window
        '''
        leaderboard_Window = tkinter.Toplevel(self._root_window)
        leaderboard_Window.title("LEADERBOARD")
        leaderboard_Window.geometry("400x400")

        # Create a database or connect to one
        connectToDatabase = sqlite3.connect('leaderboard.db')

        # Create a database cursor
        cursorForDatabase = connectToDatabase.cursor()

        # Query the database
        cursorForDatabase.execute("SELECT *, oid FROM leaderboard")
        records = cursorForDatabase.fetchall()
        #print(records)

        # Sort Python List by High Score

        sortRecords = []
        sortRecords = records.sort(reverse = True, key = lambda x: x[1])

        # Loop through results
        printRecords = ''
        for record in records:
            printRecords += str(record[0]) + "\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\n"

        headerLabel = tkinter.Label(leaderboard_Window, text = "Username" + "\t" + "Win Totals" + "\t" + "User ID" + "\n")
        headerLabel.grid(row=1, column=0, columnspan=2)

        queryLabel = tkinter.Label(leaderboard_Window, text=printRecords)
        queryLabel.grid(row=2, column = 0, columnspan = 2)

        # Commit changes
        connectToDatabase.commit()

        # Close connection
        connectToDatabase.close()

        return

    def game(self):
        '''
        Runs the game of ConnectFour.
        '''
        #Frame is the window that the game is played on
        self._frame = tkinter.Frame(master = self._root_window, bd = 0, padx=5, pady=10)
        self._canvas = tkinter.Canvas(master = self._frame, bd = 0, background = "#F8F8FF")
        self._canvas.pack()

        #Title Label
        self._ConnectFour_title_frame = tkinter.Frame(master = self._root_window, bd = 0)
        self._ConnectFour_title_frame.grid(row = 1, column = 1, columnspan = 7)
        self._ConnectFour_title_canvas = tkinter.Canvas(master = self._ConnectFour_title_frame, width = 840, height=0, bd = 0)
        self._ConnectFour_title_canvas.pack()
        self._ConnectFour_title_label = tkinter.Label(master = self._ConnectFour_title_frame, text = 'ConnectFour', font = _DEFAULT_FONT, bd = 0)
        self._ConnectFour_title_label.pack()

        #Game Board Numbers
        self._1_button_frame = tkinter.Frame(master = self._root_window)
        self._1_button_frame.grid(row = 8, column = 1, columnspan = 7)
        self._1_button_canvas = tkinter.Canvas(master = self._1_button_frame, width = 840, height = 50, bd = 0)
        self._1_button_canvas.pack()
        self._1_button = tkinter.Button(master = self._root_window, text = '1', font = _DEFAULT_FONT,
                                        command=self.move1)
        self._1_button.place(x=85, y=800)
        self._2_button = tkinter.Button(master = self._root_window, text = '2', font = _DEFAULT_FONT,
                                        command=self.move2)
        self._2_button.place(x=210, y=800)
        self._3_button = tkinter.Button(master = self._root_window, text = '3', font = _DEFAULT_FONT,
                                        command=self.move3)
        self._3_button.place(x=330, y=800)
        self._4_button = tkinter.Button(master = self._root_window, text = '4', font = _DEFAULT_FONT,
                                        command=self.move4)
        self._4_button.place(x=450, y=800)
        self._5_button = tkinter.Button(master = self._root_window, text = '5', font = _DEFAULT_FONT,
                                        command=self.move5)
        self._5_button.place(x=570, y=800)
        self._6_button = tkinter.Button(master = self._root_window, text = '6', font = _DEFAULT_FONT,
                                        command=self.move6)
        self._6_button.place(x=690, y=800)
        self._7_button = tkinter.Button(master = self._root_window, text = '7', font = _DEFAULT_FONT,
                                        command=self.move7)
        self._7_button.place(x=810, y=800)

        self.print_board()
        self._ConnectFour.winning_player()              

        #Message Area

        self._message_label = tkinter.Label(master = self._root_window, text = "", font = _DEFAULT_FONT)
        self._message_label.grid(row = 9, column = 1, columnspan = 7)

        if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
            self._message_label.config(text = self.endgame_statement())
            return

        elif self._ConnectFour.turn == connectfour.RED:
            if self._playerOne == "":
                self._message_label.config(text = "It is Red's turn")
            else:
                self._message_label.config(text = "It is {}'s (R) turn".format(self._playerOne))                
        elif self._ConnectFour.turn == connectfour.YELLOW:
            if self._playerTwo == "":
                self._message_label.config(text = "It is Yellow's turn")
            else:
                self._message_label.config(text = "It is {}'s (Y) turn".format(self._playerTwo))

        return


    def endgame_statement(self):
        '''
        The message for endgame
        '''
        message = ""

        # Create a database or connect to one
        connectToDatabase = sqlite3.connect('leaderboard.db')

        # Create a database cursor
        cursorForDatabase = connectToDatabase.cursor()

        if self._ConnectFour.winner == connectfour.RED:
            
            if self._playerOne != "":
                # Update record table
                cursorForDatabase.execute("UPDATE leaderboard SET winCount = winCount + 1 WHERE (userName = ?)", (self._playerOne,))

                message = "Congratulations! The winner is : {} (R)".format(self._playerOne)

            else:
                message = "Congratualtions! The winner is : Red"

        elif self._ConnectFour.winner == connectfour.YELLOW:
            
            if self._playerTwo != "":
                cursorForDatabase.execute("UPDATE leaderboard SET winCount = winCount + 1 WHERE (userName = ?)", (self._playerTwo,))
                message = "Congratulations! The winner is : {} (Y)".format(self._playerTwo)
            
            else:
                message = "Congratulations! The winner is : Yellow"

        else:
            message = "It's a Draw!"

        # Commit changes
        connectToDatabase.commit()

        # Close connection
        connectToDatabase.close()

        return message

    def reset(self):
        '''
        Resets the game
        '''
        self._message_label.config(text = "")
        self._ConnectFour = connectfour.ConnectFour()
        self.print_board()
        self._ConnectFour.winning_player()
        self.game()

        return

    def change_background(self):
        '''
        Changes the background of the board
        '''
        global COLOR 
        temp = random.choice(COLORS)
        if(COLOR != temp):
            COLOR = temp
        else:
            while COLOR == temp:
                temp = random.choice(COLORS)
            COLOR = temp
        self._game_canvas.config(background = COLOR)

        return COLOR
        
    def print_board(self):
        #Frame configuration
        self._0_button_frame = tkinter.Frame(master = self._root_window)
        self._0_button_frame.grid(row = 10, column = 1, columnspan = 7)
        self._0_button_canvas = tkinter.Canvas(master = self._0_button_frame, width = 840, height = 50, bd = 0)
        self._0_button_canvas.pack()

        #Button Layout
        changeBackground = tkinter.Button(master = self._root_window, text = 'Change Background', font = ('Helvetica', 12), command=self.change_background)
        changeBackground.place(x=85, y=900)
        exitToMainMenu = tkinter.Button(master = self._root_window, text = 'Main Menu', font = ('Helvetica', 12), command=self.mainMenu)
        exitToMainMenu.place(x=430, y=900)
        resetButton = tkinter.Button(master = self._root_window, text = 'Reset', font = ('Helvetica', 12), command=self.reset)
        resetButton.place(x=810, y=900)

        #Game Layout
        self._game_frame = tkinter.Frame(master = self._root_window, padx=50, pady=20)
        self._game_frame.grid(row = 2, column = 1, rowspan = 6, columnspan = 7)
        self._game_canvas = tkinter.Canvas(master = self._game_frame, width = 840, height = 720, background = COLOR)
        self._game_canvas.pack()

        #Lines
        self._game_canvas.create_line(0, 2, 840, 2, fill="black")
        self._game_canvas.create_line(0, 120, 840, 120, fill="black")
        self._game_canvas.create_line(0, 240, 840, 240, fill="black")
        self._game_canvas.create_line(0, 360, 840, 360, fill="black")
        self._game_canvas.create_line(0, 480, 840, 480, fill="black")
        self._game_canvas.create_line(0, 600, 840, 600, fill="black")
        self._game_canvas.create_line(0, 720, 840, 720, fill="black")
        self._game_canvas.create_line(120, 0, 120, 720, fill="black")
        self._game_canvas.create_line(240, 0, 240, 720, fill="black")
        self._game_canvas.create_line(360, 0, 360, 720, fill="black")
        self._game_canvas.create_line(480, 0, 480, 720, fill="black")
        self._game_canvas.create_line(600, 0, 600, 720, fill="black")
        self._game_canvas.create_line(720, 0, 720, 720, fill="black")
        self._game_canvas.pack()

        #creates the circles: 7 columns and 6 rows. Syntax: my_canvas.create_oval(x1, y1, x2, y2, fill="color")
        #all circles frames in white awaiting to be filled
        x1 = 10
        y1 = 710
        x2 = 110
        y2 = 610
        for row in range(connectfour.BOARD_ROWS):
            for col in range(connectfour.BOARD_COLUMNS):
                if self._ConnectFour.board[col][row] == ' ':
                    self._game_canvas.create_oval(x1+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y1-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    x2+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y2-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    width = 3, fill = "white")
                elif self._ConnectFour.board[col][row] == 'R':
                    self._game_canvas.create_oval(x1+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y1-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    x2+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y2-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    width = 3, fill = "red")
                elif self._ConnectFour.board[col][row] == 'Y':
                    self._game_canvas.create_oval(x1+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y1-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    x2+(120*((connectfour.BOARD_COLUMNS-1) - col)),
                                                    y2-(120*((connectfour.BOARD_ROWS-1) - row)),
                                                    width = 3, fill = "yellow")

        return
      

    def move1(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(6)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()     
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move2(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(5)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move3(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(4)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move4(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(3)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move5(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(2)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move6(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(1)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def move7(self):
        '''
        Drops a piece in the respective column
        '''
        try:
            self._ConnectFour.drop(0)
        except connectfour.InvalidMoveError:
            self._message_label.config(text = "That is an invalid move. Please try another column.")
        else:
            self.print_board()
            self._ConnectFour.winning_player()    
            if self._ConnectFour.winner != connectfour.NONE or self._ConnectFour._any_valid_moves_left() == False:
                self._message_label.config(text = self.endgame_statement())
                return
            else:
                self._message_label.config(text = self.turn_statement())

        return


    def turn_statement(self):
        '''
        Returns a statement that says who's turn it is.
        '''
        if self._ConnectFour.turn == connectfour.RED:
            if self._playerOne == "":
                self._message_label.config(text = "It is Red's turn")
            else:
                self._message_label.config(text = "It is {}'s (R) turn".format(self._playerOne))                
        else:
            if self._playerTwo == "":
                self._message_label.config(text = "It is Yellow's turn")
            else:
                self._message_label.config(text = "It is {}'s (Y) turn".format(self._playerTwo))

        return


    def run(self):
        self._root_window.mainloop()
        return

if __name__ == '__main__':
    ConnectFourApp().run()
