from tkinter import *
import random as rand
from tkinter import messagebox

bingoList = [
    "Unnecessary/Unfunny\nPhysical Assault",                # 1
    "Cardboard cutout little\ngirl with big weapon",        # 2
    "Pretending to be Meta",                                # 3
    "We lost the plot",                                     # 4
    "Least Interesting\nInteresting Character",             # 5
    "Legal Loli",                                           # 6
    "The joke is tits",                                     # 7
    "Walked in on the bath",                                # 8
    "See slavery\nbuys a slave",                            # 9
    "First girl on screen\nis the clear winner",            # 10
    "Used to be a neet",                                    # 11
    "Tolkien races only",                                   # 12
    "The female form is\napparently terrifying",            # 13
    "Protagonist Unit:\n39573071",                          # 14
    "No I never of this TONE\nWhy do you ask?",             # 15
    "If MC didn't do it,\nit didn't happen",                # 16
    "Poor World Building",                                  # 17
    "Bad voice acting",                                     # 18
    "Bad CGI",                                              # 19
    "Confusing Character\nDesign",                          # 20
    "Over Explanation",                                     # 21
    "Under Explanation",                                    # 22
    "Stupid one-liner",                                     # 23
    "Obvious villain\nis obvious",                          # 24
    "Video Game Interface",                                 # 25
    "Video Game Stats",                                     # 26
    "More than one \"Conquest\"\nappears in first episode", # 27
    "Inexplicable Cat"                                      # 28
    ]

def BingoBoard():
    displayList = []
    workingList = []
    for i in bingoList:
        workingList.append(i)
    
    for item in range(0, 24):
        randomInteger = rand.randint(0, len(workingList)-1)
        if item == 12:
            displayList.append("Free")
        displayList.append(workingList[randomInteger])
        workingList.remove(workingList[randomInteger])

    CheckBox_0_0.config(text=displayList[0], background="light grey")
    CheckBox_0_1.config(text=displayList[1], background="light grey")
    CheckBox_0_2.config(text=displayList[2], background="light grey")
    CheckBox_0_3.config(text=displayList[3], background="light grey")
    CheckBox_0_4.config(text=displayList[4], background="light grey")
    CheckBox_1_0.config(text=displayList[5], background="light grey")
    CheckBox_1_1.config(text=displayList[6], background="light grey")
    CheckBox_1_2.config(text=displayList[7], background="light grey")
    CheckBox_1_3.config(text=displayList[8], background="light grey")
    CheckBox_1_4.config(text=displayList[9], background="light grey")
    CheckBox_2_0.config(text=displayList[10], background="light grey")
    CheckBox_2_1.config(text=displayList[11], background="light grey")
    CheckBox_2_2.config(text=displayList[12], background="light green")
    CheckBox_2_3.config(text=displayList[13], background="light grey")
    CheckBox_2_4.config(text=displayList[14], background="light grey")
    CheckBox_3_0.config(text=displayList[15], background="light grey")
    CheckBox_3_1.config(text=displayList[16], background="light grey")
    CheckBox_3_2.config(text=displayList[17], background="light grey")
    CheckBox_3_3.config(text=displayList[18], background="light grey")
    CheckBox_3_4.config(text=displayList[19], background="light grey")
    CheckBox_4_0.config(text=displayList[20], background="light grey")
    CheckBox_4_1.config(text=displayList[21], background="light grey")
    CheckBox_4_2.config(text=displayList[22], background="light grey")
    CheckBox_4_3.config(text=displayList[23], background="light grey")
    CheckBox_4_4.config(text=displayList[24], background="light grey")

    cb00.set(False)
    cb01.set(False)
    cb02.set(False)
    cb03.set(False)
    cb04.set(False)

    cb10.set(False)
    cb11.set(False)
    cb12.set(False)
    cb13.set(False)
    cb14.set(False)

    cb20.set(False)
    cb21.set(False)
    cb22.set(True)
    cb23.set(False)
    cb24.set(False)

    cb30.set(False)
    cb31.set(False)
    cb32.set(False)
    cb33.set(False)
    cb34.set(False)

    cb40.set(False)
    cb41.set(False)
    cb42.set(False)
    cb43.set(False)
    cb44.set(False)

def CheckBingo():
    if cb00.get() == True:
        CheckBox_0_0.config(background="light green")
    else:
        CheckBox_0_0.config(background="light gray")
    
    if cb01.get() == True:
        CheckBox_0_1.config(background="light green")
    else:
        CheckBox_0_1.config(background="light gray")
    
    if cb02.get() == True:
        CheckBox_0_2.config(background="light green")
    else:
        CheckBox_0_2.config(background="light gray")
    
    if cb03.get() == True:
        CheckBox_0_3.config(background="light green")
    else:
        CheckBox_0_3.config(background="light gray")
    
    if cb04.get() == True:
        CheckBox_0_4.config(background="light green")
    else:
        CheckBox_0_4.config(background="light gray")
    
    if cb10.get() == True:
        CheckBox_1_0.config(background="light green")
    else:
        CheckBox_1_0.config(background="light gray")
    
    if cb11.get() == True:
        CheckBox_1_1.config(background="light green")
    else:
        CheckBox_1_1.config(background="light gray")
    
    if cb12.get() == True:
        CheckBox_1_2.config(background="light green")
    else:
        CheckBox_1_2.config(background="light gray")
    
    if cb13.get() == True:
        CheckBox_1_3.config(background="light green")
    else:
        CheckBox_1_3.config(background="light gray")
    
    if cb14.get() == True:
        CheckBox_1_4.config(background="light green")
    else:
        CheckBox_1_4.config(background="light gray")
    
    if cb20.get() == True:
        CheckBox_2_0.config(background="light green")
    else:
        CheckBox_2_0.config(background="light gray")
    
    if cb21.get() == True:
        CheckBox_2_1.config(background="light green")
    else:
        CheckBox_2_1.config(background="light gray")
    
    if cb22.get() == True:
        CheckBox_2_2.config(background="light green")
    else:
        CheckBox_2_2.config(background="light gray")
    
    if cb23.get() == True:
        CheckBox_2_3.config(background="light green")
    else:
        CheckBox_2_3.config(background="light gray")
    
    if cb24.get() == True:
        CheckBox_2_4.config(background="light green")
    else:
        CheckBox_2_4.config(background="light gray")
    
    if cb30.get() == True:
        CheckBox_3_0.config(background="light green")
    else:
        CheckBox_3_0.config(background="light gray")
    
    if cb31.get() == True:
        CheckBox_3_1.config(background="light green")
    else:
        CheckBox_3_1.config(background="light gray")
    
    if cb32.get() == True:
        CheckBox_3_2.config(background="light green")
    else:
        CheckBox_3_2.config(background="light gray")
    
    if cb33.get() == True:
        CheckBox_3_3.config(background="light green")
    else:
        CheckBox_3_3.config(background="light gray")
    
    if cb34.get() == True:
        CheckBox_3_4.config(background="light green")
    else:
        CheckBox_3_4.config(background="light gray")

    if cb40.get() == True:
        CheckBox_4_0.config(background="light green")
    else:
        CheckBox_4_0.config(background="light gray")
    
    if cb41.get() == True:
        CheckBox_4_1.config(background="light green")
    else:
        CheckBox_4_1.config(background="light gray")
    
    if cb42.get() == True:
        CheckBox_4_2.config(background="light green")
    else:
        CheckBox_4_2.config(background="light gray")
    
    if cb43.get() == True:
        CheckBox_4_3.config(background="light green")
    else:
        CheckBox_4_3.config(background="light gray")
    
    if cb44.get() == True:
        CheckBox_4_4.config(background="light green")
    else:
        CheckBox_4_4.config(background="light gray")
    


    # This will check every case for bingo
    # Verticle
    if cb00.get() == True and cb10.get() == True and cb20.get() == True and cb30.get() == True and cb40.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb01.get() == True and cb11.get() == True and cb21.get() == True and cb31.get() == True and cb41.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb02.get() == True and cb12.get() == True and cb22.get() == True and cb32.get() == True and cb42.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb03.get() == True and cb13.get() == True and cb23.get() == True and cb33.get() == True and cb43.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb04.get() == True and cb14.get() == True and cb24.get() == True and cb34.get() == True and cb44.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    
    # Horizontal
    elif cb00.get() == True and cb01.get() == True and cb02.get() == True and cb03.get() == True and cb04.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb10.get() == True and cb11.get() == True and cb12.get() == True and cb13.get() == True and cb14.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb20.get() == True and cb21.get() == True and cb22.get() == True and cb23.get() == True and cb24.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb30.get() == True and cb31.get() == True and cb32.get() == True and cb33.get() == True and cb34.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb40.get() == True and cb41.get() == True and cb42.get() == True and cb43.get() == True and cb44.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")

    # Diagonal
    elif cb00.get() == True and cb11.get() == True and cb22.get() == True and cb33.get() == True and cb44.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")
    elif cb40.get() == True and cb31.get() == True and cb22.get() == True and cb13.get() == True and cb04.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")

    # 4 Corners
    elif cb00.get() == True and cb04.get() == True and cb40.get() == True and cb44.get() == True:
        messagebox.showinfo("Bingo", "BINGO!!!!!")

root = Tk()
root.title("Bad Anime Bingo")

# Button
GenerateButton = Button(root, text="New All", command=BingoBoard)
QuitButton = Button(root, text="Quit Sibelius", command=root.destroy)

# Checkbox
cb00 = BooleanVar()
cb01 = BooleanVar()
cb02 = BooleanVar()
cb03 = BooleanVar()
cb04 = BooleanVar()

cb10 = BooleanVar()
cb11 = BooleanVar()
cb12 = BooleanVar()
cb13 = BooleanVar()
cb14 = BooleanVar()

cb20 = BooleanVar()
cb21 = BooleanVar()
cb22 = BooleanVar()
cb23 = BooleanVar()
cb24 = BooleanVar()

cb30 = BooleanVar()
cb31 = BooleanVar()
cb32 = BooleanVar()
cb33 = BooleanVar()
cb34 = BooleanVar()

cb40 = BooleanVar()
cb41 = BooleanVar()
cb42 = BooleanVar()
cb43 = BooleanVar()
cb44 = BooleanVar()

w = 20
h = 6

CheckBox_0_0 = Checkbutton(root, variable=cb00, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_0_1 = Checkbutton(root, variable=cb01, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_0_2 = Checkbutton(root, variable=cb02, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_0_3 = Checkbutton(root, variable=cb03, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_0_4 = Checkbutton(root, variable=cb04, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_1_0 = Checkbutton(root, variable=cb10, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_1_1 = Checkbutton(root, variable=cb11, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_1_2 = Checkbutton(root, variable=cb12, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_1_3 = Checkbutton(root, variable=cb13, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_1_4 = Checkbutton(root, variable=cb14, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_2_0 = Checkbutton(root, variable=cb20, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_2_1 = Checkbutton(root, variable=cb21, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_2_2 = Checkbutton(root, variable=cb22, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_2_3 = Checkbutton(root, variable=cb23, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_2_4 = Checkbutton(root, variable=cb24, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_3_0 = Checkbutton(root, variable=cb30, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_3_1 = Checkbutton(root, variable=cb31, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_3_2 = Checkbutton(root, variable=cb32, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_3_3 = Checkbutton(root, variable=cb33, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_3_4 = Checkbutton(root, variable=cb34, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_4_0 = Checkbutton(root, variable=cb40, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_4_1 = Checkbutton(root, variable=cb41, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_4_2 = Checkbutton(root, variable=cb42, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_4_3 = Checkbutton(root, variable=cb43, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)
CheckBox_4_4 = Checkbutton(root, variable=cb44, relief="solid", border=1.0, borderwidth=1.0, width=w, height=h, background="light grey", command=CheckBingo)

# Placement
CheckBox_0_0.grid(row=0, column=0)
CheckBox_0_1.grid(row=0, column=1)
CheckBox_0_2.grid(row=0, column=2)
CheckBox_0_3.grid(row=0, column=3)
CheckBox_0_4.grid(row=0, column=4)

CheckBox_1_0.grid(row=1, column=0)
CheckBox_1_1.grid(row=1, column=1)
CheckBox_1_2.grid(row=1, column=2)
CheckBox_1_3.grid(row=1, column=3)
CheckBox_1_4.grid(row=1, column=4)

CheckBox_2_0.grid(row=2, column=0)
CheckBox_2_1.grid(row=2, column=1)
CheckBox_2_2.grid(row=2, column=2)
CheckBox_2_3.grid(row=2, column=3)
CheckBox_2_4.grid(row=2, column=4)

CheckBox_3_0.grid(row=3, column=0)
CheckBox_3_1.grid(row=3, column=1)
CheckBox_3_2.grid(row=3, column=2)
CheckBox_3_3.grid(row=3, column=3)
CheckBox_3_4.grid(row=3, column=4)

CheckBox_4_0.grid(row=4, column=0)
CheckBox_4_1.grid(row=4, column=1)
CheckBox_4_2.grid(row=4, column=2)
CheckBox_4_3.grid(row=4, column=3)
CheckBox_4_4.grid(row=4, column=4)

GenerateButton.grid(row=5, column=0, columnspan=2)
QuitButton.grid(row=5, column=3, columnspan=2)

root.mainloop()
