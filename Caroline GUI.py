import Tkinter, tkFont

root = Tkinter.Tk()
root.title('Sin')

canvas = Tkinter.Canvas(root, height = 750, width = 1400, relief = Tkinter.RAISED, bg = 'white')
#canvas.grid()
'''
scrollbar = Tkinter.Scrollbar(root)
scrollbar.grid(row = 0, column = 6, rowspan = 4, sticky = Tkinter.N + Tkinter.S)

editor = Tkinter.Text(master=canvas, width = 45, height = 10, yscroll = scrollbar.set)

scrollbar.config(command = editor.yview)
'''