from tkinter import*
from tkinter import messagebox
#global variables = accesible by every function
current_player="X"
board=[""]*9   # this means list has 9 separate strings
Buttons=[]
game_over=False


def create_window():
    window=Tk()
    window.title("Tic Tac Toe")
    window.geometry("400x700")
    window.resizable(False,False)
    return window


def create_board(window):
    global Buttons
    board_frame=Frame(window)
    board_frame.pack(pady=10)


    for i in range(9):
        row=i//3   # // returns only integer value and removes decimal part
        col=i%3    # these are used to get grid quickly like 00 01 02/10 11 12/20 21 22
        button=Button(board_frame,text="",width=6,height=3,font=("Ariel",18,"bold"),command=lambda pos=i : create_control(pos))
        button.grid(row=row,column=col,padx=2,pady=2)   # lambda used when function has parameter so that it is called when button is clicked
        Buttons.append(button)  #adds the buttons to the list  


def check_winner():
    global game_over
    winning_combinations=[[0,1,2],[3,4,5],[6,7,8],
                          [0,3,6],[1,4,7],[2,5,8],   #num in bracket represent board positions where the current player choice is stored
                          [0,4,8],[2,4,6]]
    for comb in winning_combinations:
        if (board[comb[0]] == board[comb[1]] == board[comb[2]]!=""):
            game_over=True                   
            messagebox.showinfo("Game Over",f"Player {board[comb[0]]} wins! ")  
            return True  
        if ""not in board:
               game_over=True
               messagebox.showinfo("Game over"," Its a tie")    
               return True


def create_control(position):
    global current_player
    if game_over or board[position]!="":  # this cjecks if a button is pressed or not. If it is pressed then it will return
        return
    board[position]=current_player  # stores current player at i position of button in list
    Buttons[position].config(text=current_player,state="disabled") #stores the button in the list and displayes current player symbol
    if not check_winner():
        if current_player=="X":
            current_player="O"
        else:
            current_player="X"
        status_label.config(text=f"Current player :{current_player}")


def clear():
    global current_player, board , game_over , status_label
    current_player="X"
    board=[""]*9
    game_over=False
    status_label.config(text=f"Current player :{current_player}") 
    #button reset
    for button in Buttons:
        button.config(text="",state="normal")


def player_control(window):
    global status_label
    status_label=Label(window,text=f"Current player:{current_player}",font=("Ariel",12))
    status_label.pack(pady=5)
    reset_button=Button(window,text="New Game",font=("Ariel",12),command=clear)
    reset_button.pack()


def main():
    root=create_window()
    Topic=Label(root,text="Tic-Tac-Toe",font=("Ariel",16,"bold"))
    Topic.pack(side=TOP,pady=10)
    create_board(root)                      
    player_control(root)
    root.mainloop()


main()