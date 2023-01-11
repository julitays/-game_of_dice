from tkinter import *

root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Сделай бросок.')
root.resizable(height = False, width= False)
root.iconphoto(True, PhotoImage(file=('/home/julitay/-game_of_dice/icons/icon.png')))
font = PhotoImage(file=('/home/julitay/-game_of_dice/icons/pngegg.png'))
Label(root, image=font).pack()

root.mainloop()

